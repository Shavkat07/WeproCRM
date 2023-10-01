
from rest_framework.routers import SimpleRouter

from .views import ServiceViewSet, CategoryViewSet

router = SimpleRouter()
router.register('service', ServiceViewSet)
router.register('categories', CategoryViewSet)

urlpatterns = [

]