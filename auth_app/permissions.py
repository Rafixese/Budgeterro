from rest_framework.permissions import BasePermission
from rest_framework.request import Request


class ObjCanUpdateUser(BasePermission):

    def has_object_permission(self, request: Request, view, obj):
        return request.user.has_perm('change_user', obj)
