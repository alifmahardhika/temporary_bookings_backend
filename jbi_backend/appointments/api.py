from appointments.models import Appointment
from rest_framework import viewsets, permissions, generics, status
from .serializers import AppointmentSerializer, GetJBISerializer
from accounts.models import UserDetails, User, JBIDetails
from rest_framework.response import Response


class AppointmentViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        return self.request.user.user_appointments.all()

    def perform_create(self, serializer):
        serializer.save(user_creator=self.request.user)


class GetJBIViewset(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        details = UserDetails.objects.get(role="JBI")
        user = details.user
        jbi_details = JBIDetails.objects.get(jbi_username=user.username)
        return Response(
            {
                "user_id": user.id,
                "name": user.username,
                "lembaga": jbi_details.nama_lembaga,
                "phone": details.phone,
                "email": user.email,
                "gender": details.gender,
                "is_available": not jbi_details.is_nonactive,
                "diluar_jadwal": jbi_details.diluar_jadwal,
                "note": jbi_details.note,
            }
        )