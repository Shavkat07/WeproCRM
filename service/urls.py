from django.urls import path
from . import views

urlpatterns = [
    # Добавить URL для списка услуг
    path('services/', views.ServiceListView.as_view(), name='service-list'),

    # Добавить URL для деталей конкретной услуги по ее ID
    path('services/<int:pk>/', views.ServiceDetailView.as_view(), name='service-detail'),
]