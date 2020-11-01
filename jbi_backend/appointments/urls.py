from rest_framework import routers
from .api import AppointmentViewset

router = routers.DefaultRouter()
router.register("api/v1/appointments", AppointmentViewset, "appointments")

urlpatterns = router.urls