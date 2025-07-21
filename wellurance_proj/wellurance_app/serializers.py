from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta: #serialize all the fields
        model = CustomUser
        fields = '__all__'