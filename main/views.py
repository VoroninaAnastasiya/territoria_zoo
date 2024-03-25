from django.shortcuts import render

from .models import Animal, Brand, Sales, CategoryProduct, Product
from .zalivka import *

# Create your views here.
def get_page(request):
    products_queryset = Product.objects.all().prefetch_related('productcount_set') # select_related, завис.-главная
    animals = Animal.objects.all()
    products = products_queryset.order_by('-top_product')[:8]
    new_products = products_queryset.order_by('-id')[:10]

    context = {
        "animals": animals,
        "products": products,
        "new_products": new_products,
    }
    return render(request, 'index.html', context)






    #@property #декоратор
    #def discounted_price(self):
    #    return round(float(self.price) * 0.9, 2)  # для товаров со скидкой 10%

    # @property
    # def discounted_price(self):
    #     return self.price * (1 - self.discount / 100) # для товаров с любой скидкой








# from .models import Animal, Brand, Sales, CategoryProduct, Product
# from .zalivka import *