# cafe_kiosk

## 메인 화면

## 테이블

- 음료 종류(아메리카노, 라떼, 논커피라뗴, 디저트) <br>
id - pk <br>
type_name<br>

- 상세 음료<br>
아메리카노: 아이스아메리카노, 뜨아, 꿀아메리카노<br>
라떼: 카페라떼, 카푸치노, 바닐라라뗴<br>
논커피라떼 : 딸기라떼, 초코라떼, 녹차라떼<br>
디저트: 허니브레드, 치즈케익, 초코케익<br>
id - pk<br>
name<br>
price<br>
inventory<br>
type - fk (음료)<br>

- 주문<br>
id -pk<br>
customer_id(넣을지 말지..)<br>
total_price<br>
order_date<br>

- 주문 상세<br>
id - pk<br>
order - fk(주문)<br>
drink - fk(상세 음료)<br>
quantity<br>

- 지불방법<br>
id - pk<br>
order - fk(주문)<br>
payment_method [현금,카드]<br>
total_price(넣을지 말지)<br>

- 하루 총 매출<br>
date<br>
total_sales<br>