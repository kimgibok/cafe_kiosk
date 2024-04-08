from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.http import HttpResponse, Http404 , HttpResponseRedirect



from kiosk.models import Drink, DrinkType, Order, OrderItem
from django.db.models import F

class cafe_menuLV(ListView):
    model = DrinkType
    template_name = 'kiosk/cafe_menu.html'
    


class CreateOrderItemView(CreateView):
    model = OrderItem
    fields = ['quantity']
    template_name = 'kiosk/orderitem_create.html'

    def get_order(self):
        # 현재 세션에 저장된 주문을 가져오는 함수
        order_id = self.request.session.get('order_id')
        if order_id:
            return Order.objects.get(pk=order_id)
        return None

    def form_valid(self, form):
        # 폼이 유효한 경우 실행되는 메서드
        order = self.get_order()
        if order:
            form.instance.order = order
            return super().form_valid(form)
        else:
            # 세션에 활성 주문이 없는 경우에 대한 처리
            return HttpResponse("There is no active order. Please create an order first.")
