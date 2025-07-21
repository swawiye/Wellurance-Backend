from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

# Define the router
router = DefaultRouter()
router.register(r'users', UserViewSet) #register the tasks

# Define the url patterns
urlpatterns = [
    path('', include(router.urls)),
]