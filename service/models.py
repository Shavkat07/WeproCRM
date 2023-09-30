from django.contrib.auth.models import User
from django.db import models
from category.models import *

moe = User.objects.all()


class Service(models.Model):
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name='service')  # Web Developing
    name = models.CharField(max_length=255)  # Backend
    stack = models.CharField(max_length=255)  # Python
    description = models.TextField()
