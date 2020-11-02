from django.contrib import admin
from .models import Appointment

# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    fields = ("status", "booked_jbi")
    list_display = (
        "id",
        "status",
        "user_creator",
        "booked_jbi",
        "start_time",
        "end_time",
        "created",
        "last_update",
    )


admin.site.register(Appointment, AppointmentAdmin)
