from django.shortcuts import render
from .models import Product
# Create your views here.


def product_list(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def search_list(request):
    
    return render(request, 'search_list.html')