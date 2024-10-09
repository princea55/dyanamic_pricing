from rest_framework import serializers

from .models import (
    SeasonalProduct,
    BulkProduct,
    PercentageDiscount,
    FixedAmountDiscount,
    Order
)


class SeasonalProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeasonalProduct
        fields = ['id', 'name', 'base_price', 'season_discount']


class BulkProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BulkProduct
        fields = ['id', 'name', 'base_price', 'bulk_quantity', 'bulk_discount']


class PercentageDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = PercentageDiscount
        fields = ['id', 'name', 'percentage']


class FixedAmountDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = FixedAmountDiscount
        fields = ['id', 'name', 'amount']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'product', 'bulk_product', 'quantity', 'percentage_discount', 'fixed_amount_discount',
                  'get_total_price']
