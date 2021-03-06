from rest_framework import permissions


class UserPermissions(permissions.BasePermission):
    """Used by Viewset to check permissions for API requests"""

    def has_permission(self, request, view):
        """Check permissions When an object does not yet exist (POST)"""
        # Fallback to has_object_permission unless it's a POST
        if request.method != 'POST':
            return True

        return request.user.has_perm('VIEW_USERS')

    def has_object_permission(self, request, view, obj):
        """Check permissions When an object does exist (PUT, GET)"""
        if request.user.has_perm('EDIT_USERS'):
            return True

        if obj.id == request.user.id and \
                request.method in permissions.SAFE_METHODS:
            return True

        if request.method == 'GET' and \
                request.user.has_perm('VIEW_USERS'):
            return True

        return False
