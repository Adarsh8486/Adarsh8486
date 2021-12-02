from django.db import models

# Create your models here.
class registerUser(models.Model):
    Name = models.CharField(max_length = 256)
    Username = models.EmailField(max_length = 256)
    Password = models.CharField(max_length = 30)
    Re_password = models.CharField(max_length = 30)

    def __str__(self):
       return self.Name 

class Ingredients(models.Model):
    product = models.CharField(max_length=256)
    Quantity_of_product= models.IntegerField()
    cost = models.IntegerField()
    selling_price =models.IntegerField()

    def __str__(self):
       return self.product

