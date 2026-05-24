---
title: Permissions
description: Built-in permission classes, custom permissions, dynamic per-action permissions, and permission flow.
order: 10
tags: [drf, permissions, security]
---

# Chapter 10: Permissions

## 10.1 What are Permissions?

```text

Authentication = "WHO are you?" → "I am John"
Permissions    = "WHAT can you do?" → "John can read but not delete"

Real-world analogy:
You work at a company.
- Intern: Can read documents
- Employee: Can read and edit documents
- Manager: Can read, edit, and delete documents
- Admin: Can do everything

Same logic for your API:
- Anonymous user: Can only view public data
- Regular user: Can view and create
- Owner: Can view, create, edit, and delete their own data
- Admin: Can do everything
```

## 10.2 Built-in Permission Classes

```python

from rest_framework.permissions import (
    AllowAny,                    # Anyone (no login needed)
    IsAuthenticated,             # Must be logged in
    IsAdminUser,                 # Must be staff (is_staff=True)
    IsAuthenticatedOrReadOnly,   # Logged in = full access, not = read only
    DjangoModelPermissions,      # Uses Django's model permissions
)

# SETTING PERMISSIONS GLOBALLY (all views):
# config/settings.py
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

# SETTING PERMISSIONS PER VIEW:
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Override global setting

# SETTING PERMISSIONS FOR FUNCTION-BASED VIEWS:
@api_view(['GET'])
@permission_classes([AllowAny])
def public_view(request):
    return Response({'message': 'Anyone can see this'})
```

## 10.3 Custom Permissions

```python

# books/permissions.py

from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission:
    - ANYONE can do GET, HEAD, OPTIONS (read operations)
    - Only the OWNER can do POST, PUT, PATCH, DELETE (write operations)
    """
    
    # Message shown when permission is denied
    message = "You do not have permission to modify this resource."
    
    def has_object_permission(self, request, view, obj):
        """
        Called for EACH object.
        'obj' is the model instance being accessed.
        
        has_permission() → Checked BEFORE getting the object (view-level)
        has_object_permission() → Checked AFTER getting the object (object-level)
        """
        # SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
        # These are "read-only" methods — always allowed
        if request.method in SAFE_METHODS:
            return True
        
        # For write operations, check if user is the owner
        # Assumes the model has an 'owner' field
        return obj.owner == request.user

class IsAdminOrReadOnly(BasePermission):
    """
    Admin users can do anything.
    Non-admin users can only read.
    """
    
```

    def has_permission(self, request, view):
        # Read operations allowed for everyone
        if request.method in SAFE_METHODS:
            return True
        # Write operations only for admin
        return request.user and request.user.is_staff

class IsVerifiedUser(BasePermission):
    """Only email-verified users can access"""

    message = "Please verify your email first."

    def has_permission(self, request, view):
        return (
            request.user and
            request.user.is_authenticated and
            hasattr(request.user, 'email_verified') and
            request.user.email_verified
        )
## 10.4 Dynamic Permissions per Action

```python

from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def get_permissions(self):
        """
        Return different permissions based on the action.
        
        - list/retrieve: Anyone can view
        - create: Must be logged in
        - update/delete: Must be the owner
        """
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        elif self.action == 'create':
            permission_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update']:
            permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
        elif self.action == 'destroy':
            permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
        else:
            permission_classes = [IsAuthenticated]
        
        return [permission() for permission in permission_classes]
```

has_permission vs has_object_permission:

has_permission(self, request, view):
  → Called FIRST, for ALL requests
  → Checks: "Can this user access this VIEW at all?"
  → Doesn't have access to the specific object
  → Used for: checking if user is logged in, is admin, etc.

has_object_permission(self, request, view, obj):
  → Called SECOND, only for single-object views (retrieve/update/delete)
  → Checks: "Can this user access THIS SPECIFIC object?"
  → Has access to the actual database object (obj)
  → Used for: checking if user is the owner of this object

  IMPORTANT: has_object_permission is ONLY called if has_permission
  returns True first! If has_permission returns False,
  has_object_permission is never called.
### 🎯 Interview Point

**How does DRF permission checking work?**

DRF checks has_permission() first — this is a view-level check.
If it returns True, and the view accesses a specific object, DRF then checks has_object_permission() — this is an object-level check.
If ANY permission class returns False, the request is denied.
If has_permission() returns False, has_object_permission() is never called.
Multiple permission classes are combined with AND logic — ALL must pass.
