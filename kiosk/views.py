from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.http import HttpResponse, Http404 , HttpResponseRedirect
from django.db.models import Max

from kiosk.models import Drink, DrinkType, Order, OrderItem
from django.db.models import F

class cafe_menuLV(ListView):
    model = DrinkType
    template_name = 'kiosk/cafe_menu.html'
    


class CreateOrderItemView(CreateView):
    model = OrderItem
    fields = ['quantity']
    template_name = 'kiosk/orderitem_create.html'

    def get_latest_order(self):
    # 가장 최근에 생성된 주문을 가져오는 함수
        latest_order = Order.objects.latest('order_date')
        return latest_order
    
    def form_valid(self, form):
        order = self.get_latest_order()
        form.instance.order = get_object_or_404(Order, pk=order.pk)
        form.instance.drink = get_object_or_404(Drink, pk=self.kwargs['pk'])
        return super().form_valid(form)
    

    success_url = reverse_lazy('kiosk:menu_list')
