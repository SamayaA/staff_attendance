from rest_framework.permissions import BasePermission

class ControlPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'POST' and request.user.is_authenticated:
            return True
        # если метод равен не POST, то разрешение дается только тем, кто имеет доступ к административной панели
        else:
            return request.user.is_staff

# не администраторам можно только читать информацию
class EmployeePermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET' and request.user != None:
            return True
        return request.user == request.user.is_staff
             
class OtherPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'POST' and request.user.is_staff:
            return True
        # is user creator or admin
        return request.user == request.user.is_staff
