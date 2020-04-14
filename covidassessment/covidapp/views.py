from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import CovidSerializer
from .models import Covid


class CovidViewSet(viewsets.ModelViewSet):
    queryset = Covid.objects.all().order_by('name')
    serializer_class = CovidSerializer

