from django.conf.urls import url
from . import views


urlpatterns = [
    url('order_create', views.order_create, name='order_create'),
]