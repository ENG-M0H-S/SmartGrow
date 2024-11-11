from django.shortcuts import render
from .models import Plants
# Create your views here.
def PlantsView(request):
    plants = Plants.objects.all()
    return render(request, 'plants/plants.html', {'plants':plants})

def DetailsView(request):
    return render(request, 'plants/details.html')
