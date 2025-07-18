from django.contrib.auth.models import AbstractUser #creating static users
from django.db import models

# Create your models here.
# User Models
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

class ResponderTeam(models.Model):
    TEAMS = (
        ('AMBULANCE', 'Ambulance'),
        ('FIRE', 'Firefighter'),
    )

    name = models.CharField(max_length=100)
    team = models.CharField(max_length=10, choices=TEAMS)
    members = models.ManyToManyField(User, related_name='teams')
    base_location = models.PointField()
    contact = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.get_team_display()} - {self.name}"