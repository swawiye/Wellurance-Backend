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
    responders = models.JSONField(default=list) #list of the responders needed

    def __str__(self):
        return self.name
    
class EmergencyReport(models.Model):
    STATUS = (
        'REPORTED', 'Reported',
        'ASSIGNED', 'Assigned',
        'IN_PROGRESS', 'In Progress',
        'RESOLVED', 'Resolved',
        'CANCELLED', 'Cancelled',
    )

    # location = models.PointField()
    address = models.TextField()
    description = models.TextField()
    status = models.CharField(max_length=100, choices=STATUS, default='REPORTED')
    time_stamp = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)

    class Meta:
        ordering = ['-time_stamp']
        indexes = [
            models.Index(fields=['status']),
            models.Index(fields=['time_stamp']),
        ]

    def __str__(self):
        return f"{self.emergency()} - {self.get_status_display()}"
    
class IncidentUpdate(models.Model):
    status = models.CharField(max_length=100, choices=EmergencyReport.STATUS)
    notes= models.TextField()
    time_stamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time_stamp']

class ResponderAssignment(models.Model):
    status = models.CharField(max_length=20, default='PENDING')
    notes= models.TextField(blank=True)
    assigned_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    assigned_at = models.DateTimeField(auto_now_add=True)
    responder_team = models.ForeignKey(ResponderTeam, on_delete=models.CASCADE)
    incident = models.ForeignKey(EmergencyReport, on_delete=models.CASCADE, related_name='assignments')

    class Meta:
        unique_together = ('incident' - 'responder team')


