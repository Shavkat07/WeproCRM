from django.db import models
from category.models import *




class Service(models.Model):
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name='service')  # Web Developing
    name = models.CharField(max_length=255)  # Backend
    stack = models.CharField(max_length=255)  # Python
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'
