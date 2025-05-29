from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    """
    Custom permission to only allow admin users to edit objects.
    Non-admin users can only read objects.
    """

    def has_permission(self, request, view):
        # Allow read-only access for non-admin users
        if request.method in SAFE_METHODS:
            return True
        # Allow write access for admin users
        return request.user.is_superuser