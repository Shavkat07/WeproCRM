from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import FileUploadParser

from .models import CustomUser
from .serializers import SignUpUserSerializer
from rest_framework.response import Response


class SignUpView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = SignUpUserSerializer
    parser_classes = (FileUploadParser,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            avatar = request.data.get('avatar')
            if avatar:
                serializer.validated_data['avatar'] = avatar
            serializer.save()
            response = {'message': 'You have signed up successfully'}

            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
