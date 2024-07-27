from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, LocationViewSet, test_cors

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Define the schema view
schema_view = get_schema_view(
    openapi.Info(
        title="Company API",
        default_version='v1',
        description="API documentation for the Company Information Application",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@company.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'locations', LocationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('test-cors/', test_cors),
    # Swagger and ReDoc URLs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
