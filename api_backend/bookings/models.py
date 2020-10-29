from django.db import models
from interpreters.models import Interpreter
from django.contrib.auth.models import User
# Create your models here.
class Bookings(models.Model):
    STATUS_OPTIONS = (
        ("ongoing", "ongoing"),
        ("canceled", "canceled"),
        ("completed", "completed"),
        ("rescheduled", "rescheduled"),
        ("in review", "in review"),
    )
    
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_OPTIONS,
        default='ongoing',
        editable=True,
    )
    interpreter = models.ForeignKey(Interpreter, on_delete=models.CASCADE)
    user = models.ForeignKey(
            User, related_name="bookings", on_delete=models.CASCADE, null=True)

