from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrAdminOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated

        if request.method in ['PUT', 'PATCH', 'DELETE']:
            return request.user.is_authenticated and (request.user == obj.owner or request.user.is_staff)

        if request.method == 'POST':
            return request.user.is_authenticated