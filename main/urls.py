from django.urls import path

from orders.views import order_create
from .views import get_page, get_result_search, get_basket, cart_add, cart_remove, animal_add

urlpatterns = [
    path('', get_page, name='main'),
    # path('information_about_product/', get_information_about_product_page, name='products'),
    # path('product_data/<int:id>/', get_information_about_product_page, name='information_about_product'),
    path("result/", get_result_search, name='result'),
    path("basket/", get_basket, name='basket'),
    path('add/<int:product_id>/', cart_add, name='cart_add'),
    path('remove/<int:product_id>/', cart_remove, name='cart_remove'),
    path('order_create/', order_create, name='order_create'),
    path('animal_add/', animal_add, name='animal_add'),

]