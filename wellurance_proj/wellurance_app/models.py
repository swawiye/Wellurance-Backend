from django.contrib.auth.models import AbstractUser, Group, Permission #creating static users
from django.db import models

# Create your models here.
# User Models
class CustomUser(AbstractUser):
    ROLES = (
        ('ADMIN', 'Administrator'),
        ('DISPATCHER', 'Dispatcher'),
        ('AMBULANCE', 'Ambulance Team'),
        ('FIRE', 'Firefighter Team'),
        ('CIVILIAN', 'Civilian'),
    )

    role = models.CharField(max_length=20, choices=ROLES, default='CIVILIAN')
    phone = models.CharField(max_length=15)
    # profile_pic = models.ImageField(upload_to='', null=True, blank=True) #install Pillow: python -m pip install pillow
    is_verified = models.BooleanField(default=False)
    # last_location = models.PointField(null=True, blank=True) #GeoDjango

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank= True,
        help_text='The group this user belongs to',
        related_name='wellurance_user_set',
        related_query_name='wellurance_user',

    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank= True,
        help_text='Set permissions for this user',
        related_name='wellurance_user_set',
        related_query_name='wellurance_user',
    )

    # Querries (role & location)
    class Meta:
        indexes = [
            models.Index(fields=['role']),
            # models.Index(fields=['location']),
        ]

class ResponderTeam(models.Model):
    TEAMS = (
        ('AMBULANCE', 'Ambulance'),
        ('FIRE', 'Firefighter'),
    )

    name = models.CharField(max_length=100)
    team = models.CharField(max_length=10, choices=TEAMS)
    members = models.ManyToManyField(CustomUser, related_name='teams')
    # base_location = models.PointField()
    contact = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.get_team_display()} - {self.name}"
    
# Emergency & Incident Models
class Emergency(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=50)
    responders = models.JSONField(default=list)

    def __str__(self):
        return self.name
