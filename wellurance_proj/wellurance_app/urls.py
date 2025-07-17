from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegViewSet

# Define the router
router = DefaultRouter()
router.register('users', RegViewSet) #register the tasks

# Define the url patterns
urlpatterns = [
    path('auth/register', RegViewSet.as_view(), name='register'),
]