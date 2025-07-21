from django.shortcuts import render
from .models import CustomUser
from rest_framework import viewsets
from .serializers import UserSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all() #iterates through the entire list and return everything
    serializer_class = UserSerializer #serialize the data 