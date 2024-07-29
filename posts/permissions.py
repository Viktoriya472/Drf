from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Только авторизованные пользователи могут видеть список
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        # Разрешение на запись разрешено только автору поста
        return obj.author == request.user
