from .serializers import ChatSerializer, MessageSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, \
    RetrieveDestroyAPIView
from .models import MessageModel, ChatModel


class MessageListCreateApiView(ListCreateAPIView):
    queryset = MessageModel.objects.all()
    serializer_class = MessageSerializer


class MessageDetailsApiView(RetrieveUpdateDestroyAPIView):
    queryset = MessageModel.objects.all()
    serializer_class = MessageSerializer


class ChatApiView(ListCreateAPIView):
    queryset = ChatModel.objects.all()
    serializer_class = ChatSerializer


class ChatDetailsApiView(RetrieveUpdateDestroyAPIView):
    queryset = ChatModel.objects.all()
    serializer_class = ChatSerializer
