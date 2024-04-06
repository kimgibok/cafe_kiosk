from django.shortcuts import render
from django.views.generic import ListView

from kiosk.models import Drink, DrinkType

# class cafe_menuLV(ListView):
#     model = Drink
#     template_name = 'kiosk/cafe_menu.html'

#     def get_queryset(self):
#         # select_related를 사용하여 DrinkType과의 조인을 최적화
#         return Drink.objects.select_related('type').all()

class cafe_menuLV(ListView):
    model = DrinkType
    template_name = 'kiosk/cafe_menu.html'