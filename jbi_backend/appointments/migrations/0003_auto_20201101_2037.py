# Generated by Django 3.1.2 on 2020-11-01 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appointments', '0002_appointment_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='booked_jbi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jbi_appointments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='appointment',
            name='user_creator',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_appointments', to=settings.AUTH_USER_MODEL),
        ),
    ]
