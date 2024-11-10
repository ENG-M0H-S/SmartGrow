from django.contrib import admin
from .models import Categories,Plants
# Register your models here.

admin.site.register(Categories)

@admin.register(Plants)
class PlantsAdmin(admin.ModelAdmin):
    list_display = ['category', 'plant_name', 'water_requirement', 'fertillizer_requirement','harvest', 'informations', 'image']
    list_filter = ['category', 'plant_name', 'harvest']
    search_fields = ['plant_name', 'informations']
