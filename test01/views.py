import django_filters
from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Difinition
from .serializer import DifinitionSerializer

# Create your views here.
class DifinitionViewSet(viewsets.ModelViewSet):
    queryset = Difinition.objects.all()
    serializer_class = DifinitionSerializer