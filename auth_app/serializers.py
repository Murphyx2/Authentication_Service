from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from auth_app.models import CustomUser


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Remove user_id from token
        if 'user_id' in token:
            del token['user_id']

        # Custom fields
        token['username'] = user.username
        token['email'] = user.email
        token['groups'] = list(user.groups.values_list('name', flat=True))
        token['unique_id'] = str(user.unique_id)
        return token


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        from django.contrib.auth.models import Group
        user_group, _ = Group.objects.get_or_create(name='Users')
        user.groups.add(user_group)
        return user
