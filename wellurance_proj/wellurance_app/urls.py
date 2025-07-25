from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegView, LoginView, UserViewSet, ResponderTeamViewSet, EmergencyViewSet, EmergencyReportViewSet, IncidentUpdateViewSet, ResponderAssignmentViewSet, VehicleViewSet, LocationUpdateViewSet, NotificationViewSet

# Define the router
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'teams', ResponderTeamViewSet, basename='teams')
router.register(r'emergencies', EmergencyViewSet, basename='emergencies')
router.register(r'reports', EmergencyReportViewSet, basename='reports')
router.register(r'updates', IncidentUpdateViewSet, basename='updates')
router.register(r'assignments', ResponderAssignmentViewSet, basename='assignments')
router.register(r'vehicles', VehicleViewSet, basename='vehicles')
router.register(r'locations', LocationUpdateViewSet, basename='locations')
router.register(r'notifications', NotificationViewSet, basename='notifications')

# Define the url patterns
urlpatterns = [
    path('', include(router.urls)),
    # path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('register/', RegView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]