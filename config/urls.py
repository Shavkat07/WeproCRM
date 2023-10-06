from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from config.routers import DefaultRouter
from service.urls import router as service_router

router = DefaultRouter()
router.extend(service_router)

schema_view = get_schema_view(
    openapi.Info(
        title="WeproCRM",
        default_version='v1',
        description="Simple api for WeproCRM",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="shavkatkurbanov065@gmail.com"),
        license=openapi.License(name="Personal License"),
    ),

    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(router.urls)),
    path('api/users/', include('users.urls')),
    path('api/users/', include('dj_rest_auth.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)