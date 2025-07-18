from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import *

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all() #iterates through the entire list and return everything
    serializer_class = UserSerializer #serialize the data 