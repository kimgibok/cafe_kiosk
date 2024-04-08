from django.views.generic import TemplateView
from django.shortcuts import redirect
from kiosk.models import Order

class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get(self, request, *args, **kwargs):
        # GET 요청을 받았을 때 실행될 코드
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # POST 요청을 받았을 때 실행될 코드
        # 새로운 주문 생성
        order = Order.objects.create()
        # 생성된 주문의 ID를 사용하여 카페 메뉴 페이지로 리디렉션
        return redirect('kiosk:menu_list')