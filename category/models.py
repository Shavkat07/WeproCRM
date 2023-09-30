from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=355)  # Web Developing
    description = models.TextField(null=True, blank=True) #  asdfasfasdfasdf
