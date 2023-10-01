from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import CustomUserViewSet, LoginViewSet, PasswordChangeViewSet, PasswordResetViewSet

router = SimpleRouter()

router.register('signup', CustomUserViewSet)
router.register(r'login', LoginViewSet, basename='custom-login')
router.register(r'password/change', PasswordChangeViewSet, basename='custom-password-change')
router.register(r'password/reset', PasswordResetViewSet, basename='custom-password-reset')

urlpatterns = [

]
