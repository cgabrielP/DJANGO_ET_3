from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100,blank=False,null=False,default="");
    brand = models.CharField(max_length=50,default="");
    price = models.IntegerField();
    description = models.TextField()
    image = models.URLField();
    rating=models.DecimalField(max_digits=2, decimal_places=1);
    quantity=models.IntegerField(default=1);
    stock=models.IntegerField(default=1);

    def __str__(self):
        return self.name