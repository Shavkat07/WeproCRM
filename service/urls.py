from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views
from .views import ServiceViewSet

router = SimpleRouter()
router.register('service', ServiceViewSet)

urlpatterns = [

]