from django.contrib import admin

from .models import DrinkType, Drink, Order, OrderItem, Payment, TodaySales

admin.site.register(DrinkType)
admin.site.register(Drink)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Payment)
admin.site.register(TodaySales)
