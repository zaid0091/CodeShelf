---
title: Chapter 15 — Nested Serializers Deep Dive
description: Read-only and writable nested serializers for related objects
order: 15
tags: [drf, serializers, nested]
---

# Chapter 15: Nested Serializers Deep Dive

**Nested serializers** embed related objects inside a parent representation — e.g. a `Product` response that includes full `Category` data instead of only an ID.

## Definitions

| Term | Meaning |
|------|---------|
| **Nested serializer** | Another `Serializer` used as a field on a parent serializer. |
| **Depth** | How many relation levels `ModelSerializer` auto-expands (`Meta.depth`). |
| **Writable nested** | Creating/updating parent and children in one request. |

---

## 15.1 Nested Serializers (Read)

### Models

```python
class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    published_date = models.DateField(null=True, blank=True)
```

### Read-only nested representation

```python
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'email']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date']
```

### Response

```json
{
    "id": 1,
    "title": "Django for APIs",
    "author": {
        "id": 5,
        "name": "William Vincent",
        "email": "author@example.com"
    },
    "published_date": "2023-01-15"
}
```

### Using `depth` (quick but less control)

```python
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date']
        depth = 1  # nests one level of relations
```

**Caution:** `depth` nests **all** relations — can over-expose fields and cause N+1 queries.

### Optimize queries

```python
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.select_related('author').all()
    serializer_class = BookSerializer
```

### Reverse nested (parent includes children)

```python
class BookBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title']

class AuthorDetailSerializer(serializers.ModelSerializer):
    books = BookBriefSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'email', 'books']
```

```json
{
    "id": 5,
    "name": "William Vincent",
    "email": "author@example.com",
    "books": [
        {"id": 1, "title": "Django for APIs"},
        {"id": 2, "title": "Django for Beginners"}
    ]
}
```

### ManyToMany nested

```python
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'tags']
```

Use `prefetch_related('tags')` on the queryset.

### Interview points

- Nested serializers default to **read-only** unless you implement `create()`/`update()`.
- **N+1 problem:** always `select_related` / `prefetch_related` for nested lists.
- Prefer **explicit nested serializers** over high `depth` for security and performance.
- `SerializerMethodField` is an alternative for custom nested shapes.

---

## 15.2 Writable Nested Serializers

Creating or updating a parent with nested children in one payload requires custom `create()` and `update()` logic.

### Order with nested line items

```python
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='items')

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
```

```python
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'customer', 'items', 'created_at']
        read_only_fields = ['customer', 'created_at']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order

    def update(self, instance, validated_data):
        items_data = validated_data.pop('items', None)
        instance.customer = validated_data.get('customer', instance.customer)
        instance.save()

        if items_data is not None:
            instance.items.all().delete()
            for item_data in items_data:
                OrderItem.objects.create(order=instance, **item_data)
        return instance
```

### POST example

```json
{
    "items": [
        {"product": 1, "quantity": 2},
        {"product": 3, "quantity": 1}
    ]
}
```

```python
# views.py — set customer from request.user
class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)
```

### Writable nested with `@transaction.atomic`

```python
from django.db import transaction

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'items']

    @transaction.atomic
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        OrderItem.objects.bulk_create([
            OrderItem(order=order, **item) for item in items_data
        ])
        return order
```

### Partial update of nested items (advanced)

For PATCH with add/update/remove line items, consider:

- Separate endpoints for items (`/orders/1/items/`)
- `drf-writable-nested` package
- Explicit `id` in nested payload to match existing rows

```python
def update(self, instance, validated_data):
    items_data = validated_data.pop('items', [])
    for item_data in items_data:
        item_id = item_data.get('id')
        if item_id:
            item = instance.items.get(id=item_id)
            item.quantity = item_data.get('quantity', item.quantity)
            item.save()
        else:
            OrderItem.objects.create(order=instance, **item_data)
    return instance
```

### Validation across parent and children

```python
def validate(self, attrs):
    items = attrs.get('items', [])
    if not items:
        raise serializers.ValidationError({'items': 'At least one item is required.'})
    return attrs
```

### Interview points

- Writable nested is **not automatic** — you must implement `create`/`update`.
- Use **`transaction.atomic`** so partial failures do not leave orphan rows.
- REST purists often prefer **flat resources** with separate endpoints — easier to cache and permission.
- Updating M2M nested: `instance.tags.set(...)` after creating tag instances.
- **Idempotency** and **concurrency** are harder with large nested writes.

---

## Chapter summary

| Pattern | Complexity | Best for |
|---------|------------|----------|
| Read-only nested | Low | Rich GET responses |
| `depth = 1` | Low | Prototypes only |
| Custom `create`/`update` | High | Single-form order/checkout |
| Separate child endpoints | Medium | Production CRUD at scale |

Start with **read-only nested** serializers; add writable logic only when the product truly needs one-shot parent+child saves.
