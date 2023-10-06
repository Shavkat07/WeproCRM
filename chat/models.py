from django.db import models
from django.conf import settings


class ChatModel(models.Model):
    user1 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user1')
    user2 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user2')

    def __str__(self):
        return f'{self.user1} and {self.user2}'


class MessageModel(models.Model):
    text = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    chat = models.ForeignKey(ChatModel, on_delete=models.CASCADE, related_name='messages')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.chat
