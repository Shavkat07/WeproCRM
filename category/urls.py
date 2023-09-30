from django.urls import path
from . import views

urlpatterns = [
    # Добавить URL для списка услуг
    path('category/', views.CategoryViewSet.as_view(), name='service-list'),

    # Добавить URL для деталей конкретной услуги по ее ID
    # path('services/<int:pk>/', views.CategoryDetailViewSet.as_view(), name='service-detail'),
]