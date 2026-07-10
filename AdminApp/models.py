from django.db import models

# Create your models here.



class CategoryDb(models.Model):
    category_name = models.CharField(max_length=100,blank=True,null=True)
    description = models.CharField(max_length=100,blank=True,null=True)
    category_image =models.ImageField(upload_to="category images",null=True,blank=True)
    status = models.CharField(max_length=100,blank=True,null=True)

class FoodDb(models.Model):
    category_name = models.CharField(max_length=100, blank=True, null=True)
    food_name = models.CharField(max_length=100, blank=True, null=True)
    avialable = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    food_image = models.ImageField(upload_to="food images", null=True, blank=True)
    price = models.IntegerField( blank=True, null=True)

class StaffDb(models.Model):
    staff_name = models.CharField(max_length=100, blank=True, null=True)
    staff_age = models.CharField(max_length=100, blank=True, null=True)
    staff_Address = models.CharField(max_length=100, blank=True, null=True)
    staff_salary = models.CharField(max_length=100, blank=True, null=True)
    staff_email = models.CharField(max_length=100, blank=True, null=True)
    staff_phone = models.CharField(max_length=100, blank=True, null=True)
    profile_image = models.ImageField(upload_to="Profile images", null=True, blank=True)
    role = models.CharField(max_length=100, blank=True, null=True)


