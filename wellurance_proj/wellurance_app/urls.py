from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ResponderTeamViewSet, EmergencyViewSet, EmergencyReportViewSet, IncidentUpdateViewSet, ResponderAssignmentViewSet, VehicleViewSet, LocationUpdateViewSet, NotificationViewSet, ChatMessageViewSet

# Define the router
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', ResponderTeamViewSet)
router.register(r'emergencies', EmergencyViewSet)
router.register(r'reports', EmergencyReportViewSet)
router.register(r'updates', IncidentUpdateViewSet)
router.register(r'assignments', ResponderAssignmentViewSet)
router.register(r'vehicles', VehicleViewSet)
router.register(r'locations', LocationUpdateViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'messages', ChatMessageViewSet)

# Define the url patterns
urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]