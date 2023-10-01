from rest_framework import viewsets
from rest_framework import status
from .models import CustomUser
from .serializers import SignUpSerializer
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from dj_rest_auth.serializers import LoginSerializer, PasswordChangeSerializer, PasswordResetSerializer


class LoginViewSet(ViewSet):
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        return Response({'message': 'Custom login view'})


class PasswordChangeViewSet(ViewSet):
    serializer_class = PasswordChangeSerializer

    def create(self, request, *args, **kwargs):
        return Response({'message': 'Custom password change view'})


class PasswordResetViewSet(ViewSet):
    serializer_class = PasswordResetSerializer

    def create(self, request, *args, **kwargs):
        return Response({'message': 'Custom password reset view'})


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = SignUpSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            message = {'message': 'You have signed up successfully'}
            return Response(message, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
