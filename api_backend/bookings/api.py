from bookings.models import Bookings
from rest_framework import viewsets, permissions
from .serializers import BookingsSerializer

class BookingsViewset(viewsets.ModelViewSet):
    permission_classes=[
        permissions.IsAuthenticated
    ]
    serializer_class = BookingsSerializer
    def get_queryset(self):
        return self.request.user.bookings.all()


    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
