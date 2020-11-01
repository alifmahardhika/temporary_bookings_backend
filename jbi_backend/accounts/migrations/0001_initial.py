# Generated by Django 3.1.2 on 2020-11-01 15:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JBIDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_lembaga', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('email_lembaga', models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('diluar_jadwal', models.BooleanField(default=False)),
                ('is_nonactive', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_activated', models.BooleanField(default=False)),
                ('role', models.CharField(choices=[('JBI', 'JBI'), ('USER', 'USER')], default='USER', max_length=10)),
                ('gender', models.CharField(choices=[('L', 'L'), ('P', 'P'), ('-', '-')], default='-', max_length=1)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('user_photo', models.ImageField(upload_to='')),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
