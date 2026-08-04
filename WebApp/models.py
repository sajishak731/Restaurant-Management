from django.db import models
from AdminApp.models import FoodDb

# Create your models here.


class CustomerDb(models.Model):
    customer_name = models.CharField(max_length=100, blank=True, null=True)
    customer_email = models.CharField(max_length=100, blank=True, null=True)
    customer_phone = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)


# class CartDb(models.Model):
#     UserName=models.CharField(max_length=100,blank=True,null=True)
#     food_name=models.CharField(max_length=100,blank=True,null=True)
#     Quantity=models.IntegerField(blank=True,null=True)
#     Price=models.IntegerField(blank=True,null=True)
#     Total_Price=models.IntegerField(blank=True,null=True)
#     food_image=models.ImageField(upload_to="cart images",null=True,blank=True)

class CartDbModel(models.Model):
    UserName = models.CharField(max_length=100)
    food = models.ForeignKey(FoodDb, on_delete=models.CASCADE)
    Quantity = models.PositiveIntegerField(default=1)
    Total_Price = models.IntegerField()

class OrderModel(models.Model):
    UserName = models.CharField(max_length=100)
    Name=models.CharField(max_length=100,blank=True,null=True)
    Food = models.ForeignKey(FoodDb, on_delete=models.CASCADE)
    Quantity = models.PositiveIntegerField()
    Total_Price = models.IntegerField()
    Email = models.EmailField()
    Phone = models.CharField(max_length=15)
    Address = models.TextField()
    Payment = models.CharField(max_length=50)

    Ordered_Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.UserName

#
# class OrderDb(models.Model):
#     First_Name=models.CharField(max_length=100,blank=True,null=True)
#     Last_Name=models.CharField(max_length=100,blank=True,null=True)
#     Email=models.CharField(max_length=100,blank=True,null=True)
#     Place=models.CharField(max_length=100,blank=True,null=True)
#     Address=models.CharField(max_length=500,blank=True,null=True)
#     Mobile=models.CharField(max_length=100,blank=True,null=True)
#     State=models.CharField(max_length=100,blank=True,null=True)
#     Pin=models.CharField(max_length=100,blank=True,null=True)
#     Total_Price=models.IntegerField(blank=True,null=True)
#     UserName=models.CharField(max_length=100,blank=True,null=True)


class RegistrationDb(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    password =models.CharField(max_length=100, blank=True, null=True)
    confirm_password =models.CharField(max_length=100, blank=True, null=True)
