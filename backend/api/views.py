from django.shortcuts import render
from rest_framework import viewsets
from .models import Company, Location
from .serializers import CompanySerializer, LocationSerializer

# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
