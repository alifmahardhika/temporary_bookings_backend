from rest_framework import routers
from .api import InterpreterViewSet

router = routers.DefaultRouter()
router.register('api/v1/interpreters', InterpreterViewSet, 'interpreters')

urlpatterns = router.urls