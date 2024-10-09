from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)

    def get_price(self):
        return self.base_price

    class Meta:
        db_table = 'products'


class SeasonalProduct(Product):
    season_discount = models.DecimalField(max_digits=5, decimal_places=2)

    def get_price(self):
        return self.base_price * (1 - (self.season_discount / 100))

    class Meta:
        db_table = 'seasonal_product'


class BulkProduct(Product):
    bulk_quantity = models.PositiveIntegerField()
    bulk_discount = models.DecimalField(max_digits=5, decimal_places=2)

    def get_price(self, quantity):
        if quantity >= self.bulk_quantity:
            discount = (self.base_price * self.bulk_discount) / 100
            return self.base_price - discount
        return self.base_price

    class Meta:
        db_table = 'bulk_product'


class Discount(models.Model):
    name = models.CharField(max_length=100)

    def apply_discount(self, price):
        return price

    class Meta:
        db_table = 'discount'


class PercentageDiscount(Discount):
    percentage = models.DecimalField(max_digits=5, decimal_places=2)

    def apply_discount(self, price):
        discount_amount = (price * self.percentage) / 100
        return price - discount_amount

    class Meta:
        db_table = 'percentage_discount'


class FixedAmountDiscount(Discount):
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def apply_discount(self, price):
        return max(price - self.amount, 0)

    class Meta:
        db_table = 'fixedAmount_discount'


class Order(models.Model):
    product = models.ForeignKey(SeasonalProduct, on_delete=models.CASCADE, null=True, blank=True)
    bulk_product = models.ForeignKey(BulkProduct, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField()
    percentage_discount = models.ForeignKey(PercentageDiscount, on_delete=models.CASCADE, null=True, blank=True)
    fixed_amount_discount = models.ForeignKey(FixedAmountDiscount, on_delete=models.CASCADE, null=True, blank=True)

    def get_total_price(self):
        if self.product:
            price = self.product.get_price()
        elif self.bulk_product:
            price = self.bulk_product.get_price(self.quantity)
        else:
            price = 0

        if self.percentage_discount:
            price = self.percentage_discount.apply_discount(price)
        elif self.fixed_amount_discount:
            price = self.fixed_amount_discount.apply_discount(price)

        return price * self.quantity

    class Meta:
        db_table = 'orders'
