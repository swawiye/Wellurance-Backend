from rest_framework import serializers
from .models import CustomUser, ResponderTeam, Emergency, EmergencyReport, IncidentUpdate, ResponderAssignment, Vehicle, LocationUpdate, Notification
import re

class UserSerializer(serializers.ModelSerializer):
    class Meta: #serialize all the fields
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'role', 'phone', 'is_verified', 'address'] # 'profile_pic', 'location'
        extra_kwargs = {'password' : {'write_only':True}}

    def create(self, validated_data):
        user = CustomUser(
            username =validated_data['username'], 
            email = validated_data['email'],
            phone = validated_data['phone'],
            role = validated_data.get('role', 'CIVILIAN'),
            is_verified = validated_data.get('is_verified', False), 
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


    def validate_pass(self, value):
        pattern = r"/^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$/"
        if not re.match(pattern, value):
            raise serializers.ValidationError("Password must be at least 8 characters and include uppercase, lowercase, number and special character")
        return value
    
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

class ResponderTeamSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True, read_only=True)
    class Meta:
        model = ResponderTeam
        fields = '__all__'

class EmergencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Emergency
        fields = '__all__'

class EmergencyReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergencyReport
        fields = '__all__'
        read_only_fields = ['reporter']

class IncidentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncidentUpdate
        fields = '__all__'

class ResponderAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponderAssignment
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class LocationUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationUpdate
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

