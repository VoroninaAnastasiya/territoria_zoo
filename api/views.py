from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import  Response

from api.models import Author
from api.serializers import AnimalSerializer, ProductSerializer, AuthorSerializer
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
    products_serializer = ProductSerializer(products, many=True)
    return Response(products_serializer.data)


@api_view(['POST'])
def animal_add(request: Request):
    print(request.data)
    new_animal = AnimalSerializer(data=request.data)
    if new_animal.is_valid(raise_exception=True):
        print(new_animal.validated_data)
        animal = Animal(name=new_animal.validated_data.get('name'), image=new_animal.validated_data.get('image'))
        animal.save()
    else:
        print(new_animal.errors)
    return Response()

# @api_view(['GET', 'POST'])
# def get_author(request):
#     author = Author.objects.all()
#     author_serializer = AuthorSerializer(author, many=True)
#     print(author_serializer)
#     return Response()

def getFile2(request):
    pass