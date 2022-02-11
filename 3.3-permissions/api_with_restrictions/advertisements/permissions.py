from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthenticatedOrOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        method = request.method
        user = request.user
        if method in SAFE_METHODS:
            return True
        elif method == 'POST':
            return user.is_authenticated
        return user.is_staff or user == obj.creator
