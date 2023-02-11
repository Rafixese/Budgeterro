from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from guardian.shortcuts import assign_perm


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'required': True,
            },
            'email': {
                'required': True
            },
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        assign_perm('change_user', user, user)
        return user
