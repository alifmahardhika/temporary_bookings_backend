from appointments.models import Appointment
from rest_framework import viewsets, permissions, generics, status
from .serializers import AppointmentSerializer, GetJBISerializer
from accounts.models import UserDetails, User, JBIDetails
from rest_framework.response import Response


class AppointmentViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        return self.request.user.user_appointments.all()

    def perform_create(self, serializer):
        serializer.save(user_creator=self.request.user)


class GetJBIViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = GetJBISerializer

    def get_queryset(self):
        return JBIDetails.objects.all()
