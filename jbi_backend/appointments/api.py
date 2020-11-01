from appointments.models import Appointment
from rest_framework import viewsets, permissions
from .serializers import AppointmentSerializer


class AppointmentViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        return self.request.user.user_appointments.all()

    def perform_create(self, serializer):
        serializer.save(user_creator=self.request.user)