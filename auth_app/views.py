from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from auth_app.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'destroy':
            permission_classes = [IsAuthenticated, IsAdminUser]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
