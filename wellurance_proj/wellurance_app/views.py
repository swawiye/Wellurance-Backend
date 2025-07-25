from django.shortcuts import render
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.decorators import permission_required
from .models import CustomUser, ResponderTeam, Emergency, EmergencyReport, IncidentUpdate, ResponderAssignment, Vehicle, LocationUpdate, Notification
from rest_framework import viewsets, permissions, status
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import UserSerializer, ResponderTeamSerializer, EmergencySerializer, EmergencyReportSerializer, IncidentUpdateSerializer, ResponderAssignmentSerializer, VehicleSerializer, LocationUpdateSerializer, NotificationSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

# Create your views here.
class RegView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if not username or not email or not password:
            return Response({'error':'Username, email and password are required'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(request, username=username, email=email, password=password)

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'message':'Login successful', 'token':token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error':'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all() #iterates through the entire list and return everything
    serializer_class = UserSerializer #serialize the data 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=False, methods=['get'])
    def dispatchers(self, request):
        dispatchers = CustomUser.objects.filter(role='DISPATCHER')
        serializer = self.get_serializer(dispatchers, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def responders(self, request):
        responders = CustomUser.objects.filter(role__in=['AMBULANCE', 'FIRE'])
        serializer = self.get.get_serializer(responders, many=True)
        return Response(serializer.data)
    
    @permission_required('auth.change_user')
    def admin_dash(request):
        return render(request, 'http://localhost:5173/admindash')

        if request.user.groups.filter(role='DISPATCHER').exists():
            return render(request, 'http://localhost:5173/admindash')
        else:
            Response({'error':'Permission required'}, status=status.HTTP_401_UNAUTHORIZED)
    
class ResponderTeamViewSet(viewsets.ModelViewSet):
    queryset = ResponderTeam.objects.all() #iterates through the entire list and return everything
    serializer_class = ResponderTeamSerializer #serialize the data 
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post']) #pk=None
    def add_member(self, request):
        team = self.get_object()
        user_id = request.data.get('user_id')
        if not user_id:
            return Response({'error':'user_id is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = CustomUser.objects.get(pk=user_id)
            team.members.add(user)
            return Response({'status':'member added'})
        except CustomUser.DoesNotExist:
            return Response({'error':'User not found'}, status=status.HTTP_400_BAD_REQUEST)
        
class EmergencyViewSet(viewsets.ModelViewSet):
    queryset = Emergency.objects.all() #iterates through the entire list and return everything
    serializer_class = EmergencySerializer #serialize the data 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EmergencyReportViewSet(viewsets.ModelViewSet):
    queryset = EmergencyReport.objects.all()
    serializer_class = EmergencyReportSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(reporter=self.request.user)
    
# class EmergencyReportViewSet(viewsets.ModelViewSet):
#     queryset = EmergencyReport.objects.all() #iterates through the entire list and return everything
#     serializer_class = EmergencyReportSerializer #serialize the data 
#     permission_classes = [permissions.IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(reporter=self.request.user)

#     @action(detail=True, methods=['get'])
#     def updates(self, request, pk=None):
#         incident = self.get_object()
#         updates = incident.updates.all()
#         serializer = IncidentUpdateSerializer(updates, many=True)
#         return Response(serializer.data)
    
#     @action(detail=True, methods=['get'])
#     def assignments(self, request, pk=None):
#         incident = self.get_object()
#         assignments = incident.assignments.all()
#         serializer = ResponderTeamSerializer(assignments, many=True)
#         return Response(serializer.data)
    
#     @action(detail=True, methods=['get'])
#     def chat(self, request, pk=None):
#         incident = self.get_object()
#         messages = incident.messages.all()
#         serializer = ChatMessageSerializer(messages, many=True)
#         return Response(serializer.data)

class IncidentUpdateViewSet(viewsets.ModelViewSet):
    queryset = IncidentUpdate.objects.all() #iterates through the entire list and return everything
    serializer_class = IncidentUpdateSerializer #serialize the data 
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(updated_by=self.request.user)

class ResponderAssignmentViewSet(viewsets.ModelViewSet):
    queryset = ResponderAssignment.objects.all() #iterates through the entire list and return everything
    serializer_class = ResponderAssignmentSerializer #serialize the data 
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(assigned_by=self.request.user)

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all() #iterates through the entire list and return everything
    serializer_class = VehicleSerializer #serialize the data 
    permission_classes = [permissions.IsAuthenticated]

class LocationUpdateViewSet(viewsets.ModelViewSet):
    queryset = LocationUpdate.objects.all() #iterates through the entire list and return everything
    serializer_class = LocationUpdateSerializer #serialize the data 
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(responder=self.request.user)

class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer #serialize the data 
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)
    
    @action(detail=True, methods=['post'])
    def mark_as_read(self, request, pk=None):
        notification = self.get_object()
        notification.is_read = True
        notification.save()
        return Response({'status':'mark as read'})

