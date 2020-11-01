from django.contrib import admin
from .models import Appointment

# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    fields = ("status",)
    list_display = ("id", "status", "created", "last_update")


admin.site.register(Appointment, AppointmentAdmin)
