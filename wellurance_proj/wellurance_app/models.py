from django.contrib.auth.models import AbstractUser #creating static users
from django.db import models

# Create your models here.
class User(AbstractUser):
    ROLES = (
        ('ADMIN', 'Administrator'),
        ('DISPATCHER', 'Dispatcher'),
        ('AMBULANCE', 'Ambulance Team'),
        ('FIRE', 'Firefighter Team'),
        ('CIVILIAN', 'Civilian'),
    )

    role = models.CharField(max_length=10, choices=ROLES, default='CIVILIAN')
    phone = models.CharField(max_length=15)
    profile_pic = models.ImageField(upload_to='profiles/', null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    last_location = models.PointField(null=True, blank=True) #GeoDjango

    # Querries (role & location)
    class Meta:
        indexes = [
            models.Index(fields=['role']),
            models.Index(fields=['location']),
        ]
        
class User(AbstractUser):
    ROLES = (
        ('ADMIN', 'Administrator'),
        ('DISPATCHER', 'Dispatcher'),
        ('AMBULANCE', 'Ambulance Team'),
        ('FIRE', 'Firefighter Team'),
        ('CIVILIAN', 'Civilian'),
    )

    role = models.CharField(max_length=10, choices=ROLES, default='CIVILIAN')
    phone = models.CharField(max_length=15)
    profile_pic = models.ImageField(upload_to='profiles/', null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    last_location = models.PointField(null=True, blank=True) #GeoDjango

    # Querries (role & location)
    class Meta:
        indexes = [
            models.Index(fields=['role']),
            models.Index(fields=['location']),
        ]

