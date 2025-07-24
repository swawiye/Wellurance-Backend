from rest_framework import serializers
from .models import CustomUser, ResponderTeam, Emergency, EmergencyReport, IncidentUpdate, ResponderAssignment, Vehicle, LocationUpdate, Notification, ChatMessage
import re

class UserSerializer(serializers.ModelSerializer):
    class Meta: #serialize all the fields
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'role', 'phone', 'is_verified'] # 'profile_pic', 'location'
        extra_kwargs = {'password' : {'write_only':True}}

    def create(self, validated_data):
        user = CustomUser(
            username =validated_data['username'], 
            email = validated_data['email'],
            phone = validated_data['phone'],
            role = validated_data('role', 'CIVILIAN'),
            is_verified = validated_data('is_verified', False), 
        )
        user.set_password(validated_data=['password'])
        user.save()


    def validatePass(password):
        pattern = r"/^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$/"
        match = re.match(pattern, password)

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

class ChatMessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    class Meta:
        model = ChatMessage
        fields = '__all__'
