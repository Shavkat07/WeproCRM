from rest_framework import serializers
from .models import Category
from service.serializers import ServiceSerializer


class CategorySerializer(serializers.ModelSerializer):
    service = ServiceSerializer(many=True)

    class Meta:
        model = Category
        fields = '__all__'
