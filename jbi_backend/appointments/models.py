from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Appointment(models.Model):
    STATUS_OPTIONS = (
        # TODO define tiap status
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
    )
    status = models.SmallIntegerField(
        choices=STATUS_OPTIONS,
        default=0,
        editable=True,
    )
    last_update = models.DateTimeField(auto_now=True, blank=True, null=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    user_creator = models.ForeignKey(
        User,
        related_name="user_appointments",
        on_delete=models.CASCADE,
        null=True,
        editable=False,
    )
    booked_jbi = models.ForeignKey(
        User,
        related_name="jbi_appointments",
        on_delete=models.CASCADE,
        null=True,
        editable=True,
        blank=True,
    )
    start_time = models.DateTimeField(blank=False, editable=True)
    end_time = models.DateTimeField(blank=False, editable=True)
