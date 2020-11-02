from rest_framework import serializers
from appointments.models import Appointment
from accounts.models import JBIDetails, UserDetails, User
from datetime import datetime

# non bidding
class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"

    def create(self, validated_data):
        """
        TODO Validasi datetime dengan schedule jbi
        """

        # check if user id valid
        try:
            user = User.objects.get(pk=validated_data["user_creator"])
            uid = validated_data["user_creator"]

        except User.DoesNotExist:
            return None

        # check if jbi id valid
        try:
            jbi = validated_data["booked_jbi"]
            if UserDetails.objects.get(user=jbi).role == "JBI":
                jbi_id = validated_data["booked_jbi"]
            else:
                # bad request
                return None

        except User.DoesNotExist:
            return None

        # validate start and end time
        # format datetime: yyyy-MM-ddThh:mm
        if validated_data["start_time"] < validated_data["end_time"]:
            # start datetime = before end
            appointment = Appointment.objects.create(
                user_creator=user,
                booked_jbi=jbi,
                start_time=validated_data["start_time"],
                end_time=validated_data["end_time"],
            )
            return appointment
        else:
            return None


class GetJBISerializer(serializers.ModelSerializer):
    class Meta:
        model = JBIDetails
        fields = "__all__"
