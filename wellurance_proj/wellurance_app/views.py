from django.shortcuts import render
from .models import Register
from rest_framework import viewsets
from .serializers import RegSerializer

# Create your views here.
class RegViewSet(viewsets.ModelViewSet):
    queryset = Register.objects.all() #iterates through the entire list and return everything
    serializer_class = RegSerializer #serialize the data