from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=355)  # Web Developing
    description = models.TextField(null=True, blank=True)  # asdfasfasdfasdf
    image = models.ImageField(upload_to='categories/', null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Service(models.Model):
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name='service')  # Web Developing
    name = models.CharField(max_length=255)  # Backend
    stack = models.CharField(max_length=255)  # Python
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'


class ServiceImages(models.Model):
    service = models.ForeignKey(Service, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='service/', null=True, blank=True)

    def __str__(self):
        return f'Image for {self.service}'
