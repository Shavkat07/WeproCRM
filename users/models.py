from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    objects = UserManager()
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
