from django.db import models

# Create your models here.

class Categories(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__ (self):
        return self.category_name
    
class Plants(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    plant_name = models.CharField(max_length=150)
    water_requirement = models.IntegerField()
    fertillizer_requirement =models.IntegerField()
    harvest = models.IntegerField()
    informations = models.TextField()
    image = models.ImageField(upload_to='photo/%y/%m/%d')

    def __str__ (self):
        return self.plant_name