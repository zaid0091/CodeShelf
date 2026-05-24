---
title: Chapter 17 — Signals with DRF
description: Using Django signals alongside Django REST Framework for side effects and decoupling
order: 17
tags: [drf, signals, django]
---

# Chapter 17: Signals with DRF

**Signals** let decoupled receivers react to events (e.g. `post_save`) without putting all logic in serializers or views. DRF does not replace Django's signal system — they work together for emails, cache invalidation, audit logs, and search indexing.

## Definitions

| Term | Meaning |
|------|---------|
| **Signal** | Django dispatcher mechanism (`send`, `connect`). |
| **Receiver** | Callable connected to a signal. |
| **`post_save`** | Fired after a model instance is saved. |
| **`m2m_changed`** | Fired when a ManyToMany relation changes. |
| **`pre_save` / `post_delete`** | Other common model signals. |

---

## 17.1 Signals with DRF

### When to use signals vs DRF hooks

| Approach | Use when |
|----------|----------|
| `perform_create()` / `perform_update()` | Logic tied to **this API** only |
| Serializer `create()` / `update()` | Validation + persistence in one place |
| **Signals** | Side effects for **any** save (admin, shell, API, imports) |
| Celery tasks from signals | Async work (email, indexing) |

DRF view hooks example:

```python
class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
```

Signal example (runs for **all** saves):

```python
# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order

@receiver(post_save, sender=Order)
def order_created_handler(sender, instance, created, **kwargs):
    if created:
        send_order_confirmation_email(instance)
```

### Project structure

```python
# apps/orders/apps.py
from django.apps import AppConfig

class OrdersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orders'

    def ready(self):
        import orders.signals  # noqa: F401 — register receivers
```

```python
# settings.py
INSTALLED_APPS = [
    ...
    'orders.apps.OrdersConfig',  # not just 'orders'
]
```

### Common pattern: profile on user signup

```python
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()
```

Works whether the user is created via **registration API**, **admin**, or `createsuperuser`.

### Signals with API-created objects

```python
# models.py
class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

# signals.py
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

@receiver(pre_save, sender=Product)
def set_product_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)
```

```python
# views.py — DRF does not change signal behavior
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

### ManyToMany: use `m2m_changed`, not `post_save`

```python
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

@receiver(m2m_changed, sender=Product.tags.through)
def product_tags_changed(sender, instance, action, **kwargs):
    if action in ('post_add', 'post_remove', 'post_clear'):
        invalidate_product_cache(instance.pk)
```

M2M fields are not fully saved at `post_save` time — `m2m_changed` fires after the relation table updates.

### Avoiding duplicate work in serializers

If both serializer and signal send email, you get duplicates:

```python
# Bad: email in serializer AND signal

# Good: pick one layer
# Option A — signal only (all code paths)
@receiver(post_save, sender=Order)
def notify_order(sender, instance, created, **kwargs):
    if created:
        send_notification.delay(instance.id)

# Option B — perform_create only (API-only)
def perform_create(self, serializer):
    order = serializer.save(user=self.request.user)
    send_notification.delay(order.id)
```

### Async with Celery

```python
# tasks.py
from celery import shared_task

@shared_task
def send_order_confirmation_email(order_id):
    order = Order.objects.get(pk=order_id)
    ...

# signals.py
@receiver(post_save, sender=Order)
def queue_confirmation(sender, instance, created, **kwargs):
    if created:
        send_order_confirmation_email.delay(instance.id)
```

### DRF-specific: `django-rest-framework` signals

DRF exposes optional request lifecycle signals (less common than model signals):

```python
from rest_framework import signals

# Example: custom authentication might use request_started
```

Most courses focus on **Django model signals** with DRF views.

### Testing signals

```python
from django.test import TestCase
from unittest.mock import patch
from orders.models import Order

class OrderSignalTests(TestCase):
    @patch('orders.signals.send_order_confirmation_email.delay')
    def test_email_queued_on_create(self, mock_delay):
        Order.objects.create(user=self.user, total=100)
        mock_delay.assert_called_once()
```

```python
# APIClient integration test — signal still fires
from rest_framework.test import APITestCase

class OrderAPITests(APITestCase):
  def test_create_order_triggers_signal(self):
      with patch('orders.signals.send_order_confirmation_email.delay') as mock:
          self.client.post('/api/orders/', {'total': 50}, format='json')
          self.assertTrue(mock.called)
```

### Pitfalls

1. **Implicit flow** — hard to trace; prefer explicit service layer in large codebases.
2. **Import cycles** — keep signal modules thin; import models inside receivers if needed.
3. **`raw=True`** fixtures — skip side effects: `if kwargs.get('raw'): return`.
4. **`update_fields`** — partial saves may skip expected logic; check `kwargs.get('update_fields')`.

```python
@receiver(post_save, sender=Order)
def order_saved(sender, instance, created, update_fields=None, **kwargs):
    if kwargs.get('raw'):
        return
    ...
```

### Interview points

- Signals are **synchronous** by default — offload heavy work to **Celery**.
- **`created`** flag in `post_save` distinguishes insert vs update.
- DRF **`save()`** in serializers ultimately calls `Model.save()` — signals always fire.
- Critics say signals hide logic — **service layer** is a modern alternative.
- **`m2m_changed`** for M2M; **`post_save`** for FK and scalar fields.

---

## Chapter summary

- Connect receivers in `AppConfig.ready()`.
- Use signals for **cross-cutting, model-level** side effects.
- Use **`perform_create`** / **`perform_update`** for **API-specific** behavior.
- Queue emails and indexing with **async tasks**, not blocking signal handlers.

Signals complement DRF; they do not replace clear serializer and view design.
