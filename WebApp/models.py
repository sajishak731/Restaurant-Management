from django.db import models

# Create your models here.


class CustomerDb(models.Model):
    customer_name = models.CharField(max_length=100, blank=True, null=True)
    customer_email = models.CharField(max_length=100, blank=True, null=True)
    customer_phone = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)


class CartDb(models.Model):
    UserName=models.CharField(max_length=100,blank=True,null=True)
    food_name=models.CharField(max_length=100,blank=True,null=True)
    Quantity=models.IntegerField(blank=True,null=True)
    Price=models.IntegerField(blank=True,null=True)
    Total_Price=models.IntegerField(blank=True,null=True)
    food_image=models.ImageField(upload_to="cart images",null=True,blank=True)

class OrderDb(models.Model):
    First_Name=models.CharField(max_length=100,blank=True,null=True)
    Last_Name=models.CharField(max_length=100,blank=True,null=True)
    Email=models.CharField(max_length=100,blank=True,null=True)
    Place=models.CharField(max_length=100,blank=True,null=True)
    Address=models.CharField(max_length=500,blank=True,null=True)
    Mobile=models.CharField(max_length=100,blank=True,null=True)
    State=models.CharField(max_length=100,blank=True,null=True)
    Pin=models.CharField(max_length=100,blank=True,null=True)
    Total_Price=models.IntegerField(blank=True,null=True)
    UserName=models.CharField(max_length=100,blank=True,null=True)
class RegistrationDb(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    password =models.CharField(max_length=100, blank=True, null=True)
    confirm_password =models.CharField(max_length=100, blank=True, null=True)
