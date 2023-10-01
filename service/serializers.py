from rest_framework import serializers

from .models import Service, Category


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    service = ServiceSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'
