from rest_framework.permissions import BasePermission

class ControlPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        #Is not DRAFT
        if request.method == 'POST' and request.user.is_authenticated:
            return True
        # is user creator or admin
        else:
            return request.user.is_staff

class OtherPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        #Is not DRAFT
        if request.method == 'POST' and request.user.is_staff:
            return True
        # is user creator or admin
        return request.user == request.user.is_staff

#only to get inf
class EmployeePermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        #Is not DRAFT
        if request.method == 'GET' and request.user != None:
            return True
        # is user creator or admin
        return request.user == request.user.is_staff
             