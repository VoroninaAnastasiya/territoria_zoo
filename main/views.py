from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from cart.cart import Cart
from cart.forms import CartAddProductForm
from .models import Animal, Brand, Sales, CategoryProduct, Product, Article
from .zalivka import *

# Create your views here.
def get_page(request):
    products_queryset = Product.objects.all().prefetch_related('productcount_set') # select_related, завис.-главная
    animals = Animal.objects.all()
    products = products_queryset.order_by('-top_product')[:8]
    new_products = products_queryset.order_by('-id')[:10]
    articles = Article.objects.all()
    brands = Brand.objects.all()

    cart_product_form = CartAddProductForm()

    context = {
        "animals": animals,
        "products": products,
        "new_products": new_products,
        "articles": articles,
        "brands": brands,
        "cart_product_form": cart_product_form,
    }
    return render(request, 'index.html', context)


# def get_information_about_product_page(request, id):
#     product = Product.objects.filter(id=id).first()
#     context = {
#         "product_data": product,
#     }
#     return render(request, 'information_about_product.html', context)


    # post = get_object_or_404(Post,id=id)

def get_result_search(request):
    context = {}
    if request.method == "POST":
        if len(request.POST.get('search')) > 2:
            result = Product.objects.filter(name__icontains=request.POST.get('search'))
            print(result)
            context['result'] = result

        else:
            context['error'] = 'Введите более 3 символов'
    return render(request, 'result_search.html', context)

def get_basket(request):

    cart = Cart(request)
    context= {
        'cart': cart,
    }
    return render(request,'basket.html', context)


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('main')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('basket')



    #@property #декоратор
    #def discounted_price(self):
    #    return round(float(self.price) * 0.9, 2)  # для товаров со скидкой 10%

    # @property
    # def discounted_price(self):
    #     return self.price * (1 - self.discount / 100) # для товаров с любой скидкой








# from .models import Animal, Brand, Sales, CategoryProduct, Product
# from .zalivka import *