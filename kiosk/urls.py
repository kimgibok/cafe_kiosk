from django.urls import path

from . import views

app_name = 'kiosk'

urlpatterns = [
    path("", views.cafe_menuLV.as_view(), name='menu_list'),
    path("orderitem/", views.CreateOrderItemView.as_view(), name='menu_order'),
]