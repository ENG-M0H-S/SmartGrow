from django.contrib import admin
from .models import Product
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'product_image', 'quantity', 'unite_price', 'pr_date', 'ex_date', 'product_state']
    list_filter = ['product_state','pr_date', 'unite_price', 'quantity']
    search_fields = ['product_name',]
