from django.test import TestCase

from .models import (
    SeasonalProduct,
    BulkProduct,
    PercentageDiscount,
    FixedAmountDiscount,
    Order
)


class PricingTest(TestCase):

    def test_seasonal_product_discount(self):
        product = SeasonalProduct.objects.create(name="Winter Jacket", base_price=1000, season_discount=20)
        self.assertEqual(product.get_price(), 800)

    def test_bulk_product_discount(self):
        product = BulkProduct.objects.create(name="Notebook", base_price=100, bulk_quantity=10, bulk_discount=10)
        self.assertEqual(product.get_price(12), 90)
        self.assertEqual(product.get_price(5), 100)

    def test_percentage_discount(self):
        discount = PercentageDiscount.objects.create(name="Summer Sale", percentage=15)
        price_after_discount = discount.apply_discount(200)
        self.assertEqual(price_after_discount, 170)

    def test_fixed_amount_discount(self):
        discount = FixedAmountDiscount.objects.create(name="Winter Clearance", amount=30)
        price_after_discount = discount.apply_discount(100)
        self.assertEqual(price_after_discount, 70)

        price_after_discount_zero = discount.apply_discount(20)
        self.assertEqual(price_after_discount_zero, 0)

    def test_order_total_price_with_seasonal_product(self):
        product = SeasonalProduct.objects.create(name="Winter Jacket", base_price=1000, season_discount=20)
        order = Order.objects.create(product=product, quantity=2)
        self.assertEqual(order.get_total_price(), 1600)

    def test_order_total_price_with_bulk_product(self):
        bulk_product = BulkProduct.objects.create(name="Pack of Notebooks", base_price=100, bulk_quantity=10,
                                                  bulk_discount=10)
        order = Order.objects.create(bulk_product=bulk_product, quantity=12)
        self.assertEqual(order.get_total_price(), 1080)

    def test_order_with_percentage_discount(self):
        product = SeasonalProduct.objects.create(name="Winter Jacket", base_price=1000, season_discount=20)
        percentage_discount = PercentageDiscount.objects.create(name="Summer Sale", percentage=10)
        order = Order.objects.create(product=product, quantity=1, percentage_discount=percentage_discount)
        self.assertEqual(order.get_total_price(), 720)

    def test_order_with_fixed_amount_discount(self):
        product = SeasonalProduct.objects.create(name="Winter Jacket", base_price=1000, season_discount=20)
        fixed_discount = FixedAmountDiscount.objects.create(name="Winter Clearance", amount=50)
        order = Order.objects.create(product=product, quantity=1, fixed_amount_discount=fixed_discount)
        self.assertEqual(order.get_total_price(), 750)
