from rest_framework import routers
from .viewsets import *

router = routers.DefaultRouter()
router.register(r'transaction', TransactionViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'merchant',  MerchantViewSet)
router.register(r'keyword', KeywordViewSet)

urlpatterns = router.urls