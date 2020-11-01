from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class JBIDetails(models.Model):
    nama_lembaga = models.CharField(
        max_length=100, blank=True, editable=True, default=None, null=True
    )
    email_lembaga = models.EmailField(
        blank=True, editable=True, default=None, null=True
    )
    last_updated = models.DateTimeField(auto_now=True)
    diluar_jadwal = models.BooleanField(default=False, editable=True)
    is_nonactive = models.BooleanField(default=False, editable=True)
    jbi_user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    jbi_username = models.CharField(max_length=30, blank=False, primary_key=True)


class UserDetails(models.Model):
    USER_ROLE = (
        ("JBI", "JBI"),
        ("USER", "USER"),
        ("ADMIN", "ADMIN"),
    )
    GENDER_OPTIONS = (
        ("L", "L"),
        ("P", "P"),
        ("-", "-"),
    )
    is_activated = models.BooleanField(default=False, editable=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    role = models.CharField(
        max_length=10,
        choices=USER_ROLE,
        default="USER",
        editable=True,
    )
    gender = models.CharField(
        max_length=1,
        choices=GENDER_OPTIONS,
        default="-",
        editable=True,
    )
    phone = models.CharField(max_length=15, blank=True)
    user_photo = models.ImageField(blank=True)
    last_updated = models.DateTimeField(auto_now=True)


@receiver(post_save, sender=User)
def create_user_details(sender, instance, created, **kwargs):
    if created:
        UserDetails.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_details(sender, instance, **kwargs):
    instance.userdetails.save()
