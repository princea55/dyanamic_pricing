from rest_framework import viewsets

from .models import (
    SeasonalProduct,
    BulkProduct,
    PercentageDiscount,
    FixedAmountDiscount,
    Order
)
from .serializers import (
    SeasonalProductSerializer,
    BulkProductSerializer,
    PercentageDiscountSerializer,
    FixedAmountDiscountSerializer,
    OrderSerializer
)


class SeasonalProductViewSet(viewsets.ModelViewSet):
    queryset = SeasonalProduct.objects.all()
    serializer_class = SeasonalProductSerializer


class BulkProductViewSet(viewsets.ModelViewSet):
    queryset = BulkProduct.objects.all()
    serializer_class = BulkProductSerializer


class PercentageDiscountViewSet(viewsets.ModelViewSet):
    queryset = PercentageDiscount.objects.all()
    serializer_class = PercentageDiscountSerializer


class FixedAmountDiscountViewSet(viewsets.ModelViewSet):
    queryset = FixedAmountDiscount.objects.all()
    serializer_class = FixedAmountDiscountSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.save()
