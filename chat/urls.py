from django.urls import path
from .views import MessageListCreateApiView,MessageDetailsApiView,ChatApiView,ChatDetailsApiView


urlpatterns = [
    path('messages/', MessageListCreateApiView.as_view()),
    path('messages/<int:pk>/', MessageDetailsApiView.as_view()),
    path('list/', ChatApiView.as_view()),
    path('<int:pk>/', ChatDetailsApiView.as_view())
]
