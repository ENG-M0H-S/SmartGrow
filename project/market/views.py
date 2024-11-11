from django.shortcuts import render
from .models import Product

# Create your views here.
def ProductsView(request):
    products = Product.objects.all().exclude(product_state=False)
    x= {'frutes':products.filter(category_id=2)}
    return render(request, 'market/products.html', x)

def DetailsView(request):
    return render(request, 'market/details.html')