---
title: Chapter 18 — Testing
description: Testing Django REST Framework APIs with APITestCase, APIClient, and authentication
order: 18
tags: [drf, testing, pytest, api]
---

# Chapter 18: Testing

Reliable APIs need automated tests for status codes, response shape, permissions, and edge cases. DRF provides **`APIClient`** and **`APITestCase`** — extensions of Django's test tools with HTTP method helpers and JSON encoding.

## Definitions

| Term | Meaning |
|------|---------|
| **APIClient** | Test client with `.get()`, `.post()`, `.patch()`, etc. |
| **APITestCase** | TestCase with `client` as APIClient and JSON helpers. |
| **force_authenticate** | Attach a user to the request without logging in. |
| **format='json'** | Encodes body as JSON and sets content type. |

---

## 18.1 Testing API Endpoints

### Setup

```python
# tests/test_products.py
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from products.models import Product, Category

class ProductAPITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(name='Electronics')
        cls.user = User.objects.create_user(username='tester', password='pass1234')
        cls.admin = User.objects.create_superuser(
            username='admin', password='admin123', email='admin@test.com'
        )
        cls.product = Product.objects.create(
            name='Laptop', category=cls.category, price=999.99
        )

    def setUp(self):
        self.list_url = '/api/products/'
        self.detail_url = f'/api/products/{self.product.pk}/'
```

### List and retrieve

```python
    def test_list_products_anonymous(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['name'], 'Laptop')

    def test_retrieve_product(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Laptop')
        self.assertEqual(response.data['category'], self.category.pk)
```

### Create (authenticated)

```python
    def test_create_product_requires_auth(self):
        payload = {'name': 'Phone', 'category': self.category.pk, 'price': 499}
        response = self.client.post(self.list_url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_product_authenticated(self):
        self.client.force_authenticate(user=self.user)
        payload = {'name': 'Phone', 'category': self.category.pk, 'price': 499}
        response = self.client.post(self.list_url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)
        self.assertEqual(response.data['name'], 'Phone')
```

### Update and delete

```python
    def test_partial_update(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.patch(
            self.detail_url,
            {'price': 899.99},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product.refresh_from_db()
        self.assertEqual(float(self.product.price), 899.99)

    def test_delete_product(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Product.objects.filter(pk=self.product.pk).exists())
```

### Validation errors

```python
    def test_create_invalid_price(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(
            self.list_url,
            {'name': 'Bad', 'category': self.category.pk, 'price': -10},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('price', response.data)
```

### Permissions

```python
    def test_non_admin_cannot_delete(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
```

### Login with credentials (session auth)

```python
    def test_login_session_auth(self):
        logged_in = self.client.login(username='tester', password='pass1234')
        self.assertTrue(logged_in)
        response = self.client.get('/api/me/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
```

### Token / JWT authentication in tests

```python
from rest_framework.authtoken.models import Token

def test_token_authentication(self):
    token, _ = Token.objects.get_or_create(user=self.user)
    self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
    response = self.client.get(self.list_url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
```

```python
# SimpleJWT
from rest_framework_simplejwt.tokens import RefreshToken

def test_jwt_authentication(self):
    refresh = RefreshToken.for_user(self.user)
    self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
    response = self.client.get(self.list_url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
```

### File upload tests

```python
from django.core.files.uploadedfile import SimpleUploadedFile

def test_upload_avatar(self):
    self.client.force_authenticate(user=self.user)
    image = SimpleUploadedFile(
        name='test.jpg',
        content=b'fake-image-content',
        content_type='image/jpeg'
    )
    response = self.client.patch(
        '/api/profiles/1/',
        {'avatar': image},
        format='multipart'
    )
    self.assertEqual(response.status_code, status.HTTP_200_OK)
```

### Reverse URL names (best practice)

```python
from django.urls import reverse

def test_list_url_reverse(self):
    url = reverse('product-list')
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
```

### Factory pattern (optional, with factory_boy)

```bash
pip install factory_boy
```

```python
import factory
from products.models import Product

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Sequence(lambda n: f'Product {n}')
    price = 10.00
    category = factory.SubFactory(CategoryFactory)
```

### Pytest style (optional)

```bash
pip install pytest pytest-django
```

```python
import pytest
from rest_framework.test import APIClient

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def auth_client(api_client, django_user_model):
    user = django_user_model.objects.create_user(username='u', password='p')
    api_client.force_authenticate(user=user)
    return api_client

@pytest.mark.django_db
def test_list_products(auth_client):
    response = auth_client.get('/api/products/')
    assert response.status_code == 200
```

### Run tests

```bash
python manage.py test products.tests
python manage.py test products.tests.ProductAPITests.test_list_products_anonymous

# pytest
pytest products/tests/ -v
```

### Interview points

- Use **`APITestCase`** (not plain `Client`) for DRF renderer/parser behavior.
- **`format='json'`** on POST/PATCH/PUT — otherwise use `format='multipart'` for files.
- **`force_authenticate`** skips login — fast and ideal for unit tests.
- Test **permissions**, **validation**, **pagination**, and **filtering** query params.
- Keep tests **independent** — `setUpTestData` for shared read-only data.
- **`self.assertNumQueries`** guards against N+1 regressions.

---

## Chapter summary

| Tool | Purpose |
|------|---------|
| `APITestCase` | Base class with `APIClient` |
| `force_authenticate` | Simulate logged-in user |
| `credentials()` | Set Authorization header |
| `format='json'` | JSON request bodies |
| `reverse()` | Stable URL resolution |

Test the **HTTP contract** your clients depend on — status, body, and headers — not only model state.
