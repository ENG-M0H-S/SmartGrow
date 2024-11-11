from django.db import models
from plants.models import Categories
# Create your models here.

class Product(models.Model):
    UNIT_CHOICES = [
            ('kg', 'كيلو'),
            ('box', 'سلة'),
            ('bundle', 'ربطة'),
            ('cup', 'قدح'),
            ('bag', 'كيس'),
        ]   

    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    product_image = models.ImageField(upload_to='photo/%y/%m/%d')
    quantity = models.DecimalField(max_digits=8, decimal_places=2)
    unit = models.CharField(max_length=100, choices=UNIT_CHOICES, default='kg')
    unite_price = models.DecimalField(max_digits=8, decimal_places=2)
    pr_date = models.DateField(auto_now_add=True)
    ex_date = models.DateField()
    product_state = models.BooleanField(default=True)

    def __str__ (self):
        return self.product_name
    


#دالة لانشاء قيمة حقل تلقائيا استنادا لحقل اخر 
    # def save(self, *args, **kwargs):
    #     if self.category:
    #         self.type = self.category.category_name
    #     super(Product, self).save(*args, **kwargs)

    
    #دالة لتغيير اسماء المودلز في العرض ويمكن استخدامها لتغيير اسماء الحقول
    # class Meta:
    #     verbose_name = 'المنتجات'