from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    """
    Allows access only to users with superuser status.
    """
    def has_permission(self, request, view):
        """
        Check if the user has superuser status.
        """
        return request.user.is_superuser
