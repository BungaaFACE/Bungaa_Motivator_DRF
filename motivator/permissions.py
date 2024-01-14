from rest_framework.permissions import BasePermission


# actions: ['list', 'create', 'retrieve', 'update', 'partial_update', 'destroy']

def is_creator(object, request):
    return object.user == request.user

def is_su(request):
    return request.user.is_superuser


class IsCreatorClass(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        
    def has_object_permission(self, request, view, obj):
        if is_creator(obj, request):
            return True

class IsSuClass(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        
    def has_object_permission(self, request, view, obj):
        if is_su(request):
            return True


class IsPublicHabitClass(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        
    def has_object_permission(self, request, view, obj):
        return obj.is_public