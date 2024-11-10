from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_image = models.ImageField(upload_to='photo/%y/%m/%d')
    quantity = models.DecimalField(max_digits=8, decimal_places=2)
    unite_price = models.DecimalField(max_digits=8, decimal_places=2)
    pr_date = models.DateField(auto_now_add=True)
    ex_date = models.DateField(null=True, blank=True)
    product_state = models.BooleanField(default=True)

    def __str__ (self):
        return self.product_name
    
    # class Meta:
    #     verbose_name = 'المنتجات'