from django.urls import path

from api.views import get_animal_list, get_product_info, animal_add, getFile2
from orders.views import order_create

urlpatterns = [
    path('get_animal_list/', get_animal_list),
    path('get_product_info/', get_product_info),
    path('animal_add/', animal_add),
    path('get_file2', getFile2, name='get_file'),
]