from django.urls import path

from .views import get_page_coockie

urlpatterns = [
    path('', get_page_coockie),
]