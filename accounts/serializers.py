from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser, Profile

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return {'user': user}
        raise serializers.ValidationError('Invalid credentials.')

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'password', 'password_confirm')

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError("Passwords don't match.")
        return data

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = CustomUser.objects.create_user(**validated_data)
        Profile.objects.get_or_create(user=user, defaults={'national_code': ''})
        return user

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Profile
        fields = ('user', 'national_code')
