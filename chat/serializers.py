from rest_framework import serializers
from .models import ChatModel, MessageModel


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageModel
        fields = '__all__'


class ChatSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True,read_only=True)

    class Meta:
        model = ChatModel
        fields = ('id','user1', 'user2', 'messages')
