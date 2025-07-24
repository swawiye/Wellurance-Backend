from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, ResponderTeam, Emergency, EmergencyReport, IncidentUpdate, ResponderAssignment, Vehicle, LocationUpdate, Notification, ChatMessage

# Register your models here.
admin.site.register(CustomUser, UserAdmin)
admin.site.register(ResponderTeam)
admin.site.register(Emergency)
admin.site.register(EmergencyReport)
admin.site.register(IncidentUpdate)
admin.site.register(ResponderAssignment)
admin.site.register(Vehicle)
admin.site.register(LocationUpdate)
admin.site.register(Notification)
admin.site.register(ChatMessage)