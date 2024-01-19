from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class IsPublicHabit(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        return False

    def has_object_permission(self, request, view, obj):
        return obj.is_public
