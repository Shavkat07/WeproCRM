from dj_rest_auth.views import LogoutView
from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import CustomUserViewSet, LoginViewSet, PasswordChangeViewSet, PasswordResetViewSet

router = SimpleRouter()

router.register('signup', CustomUserViewSet)
router.register('login', LoginViewSet, basename='custom-login')
router.register('password/change', PasswordChangeViewSet, basename='custom-password-change')
router.register('password/reset', PasswordResetViewSet, basename='custom-password-reset')
# router.register('logout', LogoutView.as_view(), basename='logout')

urlpatterns = [

]
