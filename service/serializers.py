from rest_framework import serializers

from .models import Service, Category, ServiceImages


class ServiceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceImages
        fields = ('service', 'image',)


class ServiceSerializer(serializers.ModelSerializer):
    images = ServiceImageSerializer(source='serviceimages_set', many=True, read_only=True)

    class Meta:
        model = Service
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    service = ServiceSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'
