"""User permissions."""

# Django REST Framework
from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    """Allow access only to admins."""

    def has_permission(self, request, view):
        """Check user has admin privileges."""
        return request.user.is_admin == True


class IsAccountOwner(BasePermission):
    """Allow access only to objects owned by the requesting user."""

    def has_object_permission(self, request, view, obj):
        """Check obj and user are the same."""
        return request.user == obj
