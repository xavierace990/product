from django.shortcuts import render
from .models import Product
# Create your views here.
import requests

def product_list(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def search_list(request):
    
    return render(request, 'search_list.html')


def img_upload(image_file):
    api_key = 'c52a26345162b32e311cf76fea57be22'
    url = 'https://api.imgbb.com/1/upload'

    with open(image_file, 'rb') as file:
        payload = {
            'key': api_key,
            'image': file,
        }
        response = requests.post(url, files=payload)

    if response.status_code == 200:
        return response.json()['data']['url']
    else:
        return None
