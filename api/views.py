from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import  Response

from api.serializers import AnimalSerializer, ProductSerializer
from main.models import Animal, Product


# Create your views here.
@api_view(['GET', 'POST'])
def get_animal_list(request: Request):
    animals = Animal.objects.all()
    serializer = AnimalSerializer(animals, many=True)
    print(serializer)
    return Response(serializer.data)


@api_view(['POST'])
def get_product_info(request: Request) -> Response[ProductSerializer]:
    """post data -> {"search_words": "ко"}; """
    print(request.data)
    search_data = request.data
    products = Product.objects.filter(name__icontains=search_data.get("search_words"))
    producs_serializer = ProductSerializer(products, many=True)
    return Response(producs_serializer.data)
