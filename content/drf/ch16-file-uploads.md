---
title: Chapter 16 — File Uploads
description: ImageField, FileField, parsers, and serving media in Django REST Framework
order: 16
tags: [drf, file-upload, media, parsers]
---

# Chapter 16: File Uploads

APIs often accept images, documents, and attachments. DRF builds on Django's **FileField** / **ImageField** and uses **parser classes** to handle `multipart/form-data` and raw uploads.

## Definitions

| Term | Meaning |
|------|---------|
| **Parser** | Converts HTTP body into `request.data` / `request.FILES`. |
| **MultiPartParser** | Parses `multipart/form-data` (forms with files). |
| **FileUploadParser** | Parses raw file uploads to a single field. |
| **MEDIA_ROOT** | Filesystem path where uploads are stored. |
| **MEDIA_URL** | URL prefix to serve uploaded files in development. |

---

## 16.1 ImageField and FileField

### Model

```python
# models.py
from django.db import models

def user_avatar_path(instance, filename):
    return f'avatars/user_{instance.user_id}/{filename}'

class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to=user_avatar_path, blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
```

Install Pillow for `ImageField`:

```bash
pip install Pillow
```

### Serializer

```python
from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'bio', 'avatar', 'resume']
        read_only_fields = ['user']
```

### ViewSet

```python
from rest_framework import viewsets, permissions
from rest_framework.parsers import MultiPartParser, FormParser

class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
```

### Upload with curl

```bash
curl -X PATCH http://127.0.0.1:8000/api/profiles/1/ \
  -H "Authorization: Bearer <token>" \
  -F "avatar=@/path/to/photo.jpg" \
  -F "bio=Hello world"
```

### JSON response (avatar URL)

```json
{
    "id": 1,
    "user": 1,
    "bio": "Hello world",
    "avatar": "http://127.0.0.1:8000/media/avatars/user_1/photo.jpg",
    "resume": null
}
```

### Validation (size, extension)

```python
class ProfileSerializer(serializers.ModelSerializer):
    def validate_avatar(self, value):
        if value.size > 2 * 1024 * 1024:  # 2 MB
            raise serializers.ValidationError('Image must be under 2 MB.')
        if not value.content_type.startswith('image/'):
            raise serializers.ValidationError('File must be an image.')
        return value

    class Meta:
        model = Profile
        fields = ['id', 'bio', 'avatar', 'resume']
```

### Interview points

- File data lives in **`request.FILES`**, not JSON body — use **multipart** requests.
- `ImageField` requires **Pillow**; validates image format on save.
- Never trust client **content-type** alone — validate magic bytes in production.
- Store paths in DB, files on disk/S3 — not in the database BLOB (usually).

---

## 16.2 Parser Classes

Parsers determine how incoming request bodies are parsed.

### Default parsers

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ],
}
```

| Parser | Content-Type | Use |
|--------|--------------|-----|
| `JSONParser` | `application/json` | Normal JSON APIs |
| `FormParser` | `application/x-www-form-urlencoded` | HTML forms |
| `MultiPartParser` | `multipart/form-data` | File uploads |
| `FileUploadParser` | `multipart/form-data`, `application/octet-stream` | Raw file to `request.data['file']` |

### FileUploadParser example

```python
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework import status

class FileUploadView(APIView):
    parser_classes = [FileUploadParser]

    def put(self, request, filename, format=None):
        file_obj = request.data['file']
        with open(f'/tmp/{filename}', 'wb+') as f:
            for chunk in file_obj.chunks():
                f.write(chunk)
        return Response({'filename': filename}, status=status.HTTP_201_CREATED)
```

```bash
curl -X PUT http://127.0.0.1:8000/upload/example.txt \
  -H "Content-Type: application/octet-stream" \
  --data-binary @example.txt
```

### Per-action parsers on ViewSet

```python
class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    def get_parsers(self):
        if self.action in ('create', 'update', 'partial_update'):
            return [MultiPartParser(), FormParser()]
        return super().get_parsers()
```

### Base64 upload (alternative pattern)

Some mobile clients send base64 in JSON — handle in serializer (not built-in):

```python
import base64
from django.core.files.base import ContentFile

class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name=f'upload.{ext}')
        return super().to_internal_value(data)
```

### Interview points

- Wrong parser → **Unsupported media type** (415) or empty `request.data`.
- **Order matters:** first matching parser wins.
- Large uploads: configure **nginx** `client_max_body_size`, Django `DATA_UPLOAD_MAX_MEMORY_SIZE`.

---

## 16.3 Serving Media Files

### Development settings

```python
# settings.py
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

```python
# urls.py (project root — development only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myapp.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### Production: never use Django to serve media

Use **AWS S3**, **Cloudinary**, **Azure Blob**, or nginx/CDN:

```bash
pip install django-storages boto3
```

```python
# settings.py (production)
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_STORAGE_BUCKET_NAME = 'my-bucket'
AWS_S3_REGION_NAME = 'us-east-1'
AWS_DEFAULT_ACL = 'public-read'
AWS_QUERYSTRING_AUTH = False
```

```python
# Serializer returns full S3 URL automatically when using default storage
class ProfileSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(use_url=True)

    class Meta:
        model = Profile
        fields = ['avatar']
```

### Absolute URI in serializers

```python
class ProfileSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()

    def get_avatar(self, obj):
        if obj.avatar:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.avatar.url)
            return obj.avatar.url
        return None

    class Meta:
        model = Profile
        fields = ['avatar']
```

### Secure private files

For private documents, use **signed URLs** or an authenticated download view — do not expose `MEDIA_URL` publicly.

```python
class PrivateDocumentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        doc = get_object_or_404(Document, pk=pk, owner=request.user)
        return FileResponse(doc.file.open('rb'), as_attachment=True)
```

### Interview points

- **`DEBUG=True` + static()** is for development only.
- Use **django-storages** + CDN in production.
- Separate **user-generated media** from **static assets** (`STATIC_URL`).
- Consider **virus scanning** and **content moderation** for user uploads.

---

## Chapter summary

1. Model: `FileField` / `ImageField` with `upload_to`.
2. API: `MultiPartParser` + `FormParser` on the view.
3. Client: `multipart/form-data` with `-F` or `FormData`.
4. Deploy: S3/CDN for media; validate size and type server-side.
