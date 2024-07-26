from django.shortcuts import render
from rest_framework import viewsets
from .models import Company, Location
from .serializers import CompanySerializer, LocationSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view

# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

@api_view(['GET'])
def test_cors(request):
    return JsonResponse({'message': 'CORS headers are working!'})

