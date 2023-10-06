from rest_framework.routers import SimpleRouter

from .views import ServiceViewSet, CategoryViewSet, ServiceImageViewSet


router = SimpleRouter()
router.register('categories', CategoryViewSet)
router.register('service', ServiceViewSet)
router.register('service_images', ServiceImageViewSet)
urlpatterns = [

]
