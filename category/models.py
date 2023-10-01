from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=355)  # Web Developing
    description = models.TextField(null=True, blank=True)  # asdfasfasdfasdf

    def __str__(self):
        return f'{self.name}'
