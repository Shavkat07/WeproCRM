from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers
from .models import CustomUser
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token


class UserDetailSerializer(UserDetailsSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'avatar')
        read_only_fields = ('email',)


class SignUpUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, write_only=True, style={'input_type': 'password'})
    password2 = serializers.CharField(min_length=8, write_only=True, style={'input_type': 'password'})
    avatar = serializers.CharField(required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'password2', 'avatar')

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
        avatar = validated_data.pop('avatar', None)
        user = super().create(validated_data)
        user.set_password(password)
        if avatar:
            user.avatar = avatar
        user.save()
        Token.objects.create(user=user)
        return user
