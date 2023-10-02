from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import CustomUser
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token


class CustomUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, write_only=True, style={'input_type': 'password'})
    password2 = serializers.CharField(min_length=8, write_only=True, style={'input_type': 'password'})

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'password2')

    def validate(self, attrs):
        user_exists = CustomUser.objects.filter(username=attrs['username']).exists()
        if user_exists:
            raise ValidationError('User already exists')
        password = attrs.get('password')
        password2 = attrs.get('password2')

        if password != password2:
            raise ValidationError('Passwords do not match')

        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop('password')
        password2 = validated_data.pop('password2')
        if password != password2:
            raise ValidationError('Passwords do not match')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user

