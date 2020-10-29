from rest_framework import serializers
from bookings.models import Bookings

class BookingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        fields = ('id', 'user', 'date', 'time', 'interpreter', 'status')
        extra_kwargs = {'user': {'read_only': True}}