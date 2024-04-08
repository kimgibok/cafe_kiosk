from django.db import models
from datetime import date


# Create your models here.
class DrinkType(models.Model):
    type_name = models.CharField(max_length=100)

    def __str__(self):
        return self.type_name

# 음료 및 디저트 모델
class Drink(models.Model):
    type = models.ForeignKey(DrinkType, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    inventory = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Order(models.Model):
    # customer_id = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True) # customer_id가 사라지면 null로
    order_date = models.DateTimeField(auto_now_add=True)
    total_price = models.IntegerField(default=0)

    def __str__(self):
        return f"주문번호 {self.id}"

# 주문 상세 모델
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.drink.name} 주문 (주문: {self.order.id})"

# 결제 모델
class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)
    PAYMENT_CHOICES = [
        ('cash', '현금'),
        ('card', '카드'),
    ]
    payment_method = models.CharField(max_length=50, choices=PAYMENT_CHOICES)
    # total_price = models.IntegerField()

    def __str__(self):
        return f"{self.order} 결제"


class TodaySales(models.Model):
    order_date = models.DateField(default=date.today, unique=True)
    total_sales = models.IntegerField()

    def __str__(self):
        return f"{self.order_date} - 총 매출: {self.total_sales}"