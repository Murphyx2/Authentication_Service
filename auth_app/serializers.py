from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from auth_app.models import CustomUser
from auth_app.validations import validate_username


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Remove user_id from token
        if 'user_id' in token:
            del token['user_id']

        # Custom fields
        # Email serves username
        token['username'] = user.username
        token['groups'] = list(user.groups.values_list('name', flat=True))
        token['unique_id'] = str(user.unique_id)
        return token


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_username(self, value):
        # Validate if username is an email
        validate_username({"username": value})
        return value

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError(
                code="password_too_short",
                detail="Password must be at least 8 characters long."
            )
        return value

    def create(self, validated_data):
        username = validated_data['username']
        user = CustomUser.objects.create_user(
            username=username,
            email=username,
            password=validated_data['password'],
        )
        from django.contrib.auth.models import Group
        user_group, _ = Group.objects.get_or_create(name='Users')
        user.groups.add(user_group)
        return user
