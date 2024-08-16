from django.urls import path, include
from rest_framework.routers import DefaultRouter
from reports.views import MobilePspCustomerInfoViewSet

router = DefaultRouter()
router.register(r'mobile-psp-customer-info', MobilePspCustomerInfoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
