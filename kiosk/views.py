from django.shortcuts import render
from django.views.generic import ListView

from kiosk.models import Drink, DrinkType


class cafe_menuLV(ListView):
    model = DrinkType
    template_name = 'kiosk/cafe_menu.html'