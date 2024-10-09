from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    SeasonalProductViewSet,
    BulkProductViewSet,
    PercentageDiscountViewSet,
    FixedAmountDiscountViewSet,
    OrderViewSet
)

router = DefaultRouter()
router.register(r'seasonal-products', SeasonalProductViewSet)
router.register(r'bulk-products', BulkProductViewSet)
router.register(r'percentage-discounts', PercentageDiscountViewSet)
router.register(r'fixed-amount-discounts', FixedAmountDiscountViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
