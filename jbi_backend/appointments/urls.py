from django.urls import path, include
from rest_framework import routers
from .api import AppointmentViewset, GetJBIViewset

router = routers.DefaultRouter()
router.register("api/v1/appointments", AppointmentViewset, "appointments")

urlpatterns = [
    path("api/v1/get-jbi-list", GetJBIViewset.as_view()),
]
urlpatterns += router.urls
