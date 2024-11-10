from django.shortcuts import render
from .models import Product

# Create your views here.
def ProductsView(request):
    products = Product.objects.all()
    return render(request, 'market/products.html', {'products':products})

def DetailsView(request):
    return render(request, 'market/details.html')