from django.urls import path
from . import views

urlpatterns = [
    path('', views.PlantsView, name='plants'),
    path('details', views.DetailsView, name='details'),
    
]