from rest_framework import serializers
from .models import Register

class RegSerializer(serializers.ModelSerializer):
    class Meta: #serialize all the fields
        model = Register
        fields = '__all__'