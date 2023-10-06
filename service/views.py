from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from service.models import Service, Category, ServiceImages
from service.serializers import ServiceSerializer, CategorySerializer, ServiceImageSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, ]


class ServiceImageViewSet(viewsets.ModelViewSet):
    queryset = ServiceImages.objects.all()
    serializer_class = ServiceImageSerializer
    permission_classes = [IsAuthenticated]


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]
