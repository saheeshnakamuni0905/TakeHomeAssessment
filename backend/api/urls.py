# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, LocationViewSet, test_cors

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'locations', LocationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('test-cors/', test_cors),
]