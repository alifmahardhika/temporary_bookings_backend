from rest_framework import routers
from .api import BookingsViewset

router = routers.DefaultRouter()
router.register('api/v1/bookings', BookingsViewset, 'bookings')

urlpatterns = router.urls