from django.shortcuts import render

# Create your views here.
def get_page_coockie(request):
    print(request.COOKIES.get('colors'))
    return render(request, 'coockie.html')
