from django.db import models

# Create your models here.
class Appointment(models.Model):
    STATUS_OPTIONS = (
        # TODO define tiap status
        (0, 0), 
        (1, 1),
        (2, 2),
        (3, 3),
        (4,4),
    )
    status = models.SmallIntegerField(
        choices=STATUS_OPTIONS,
        default=0,
        editable=True,
    )
    last_update = models.DateTimeField(auto_now=True, blank=True, null=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

