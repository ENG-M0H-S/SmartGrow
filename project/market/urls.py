from django.urls import path
from . import views

urlpatterns=[
    path('', views.ProductsView, name='products'),
    path('details', views.DetailsView, name='details'),
]