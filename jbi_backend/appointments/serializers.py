from rest_framework import serializers
from appointments.models import Appointment
from accounts.models import JBIDetails


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"


class GetJBISerializer(serializers.ModelSerializer):
    class Meta:
        model = JBIDetails
        fields = "__all__"