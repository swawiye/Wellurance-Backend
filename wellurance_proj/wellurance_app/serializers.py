from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta: #serialize all the fields
        model = User
        fields = '__all__'