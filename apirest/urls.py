from rest_framework import routers
from .viewsets import *

router = routers.DefaultRouter()
router.register(r'transaction', TransactionViewSet)
urlpatterns = router.urls