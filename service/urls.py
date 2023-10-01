from rest_framework.routers import SimpleRouter

from .views import ServiceViewSet, CategoryViewSet

router = SimpleRouter()
router.register('categories', CategoryViewSet)
router.register('service', ServiceViewSet)

urlpatterns = [

]
