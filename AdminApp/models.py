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
    staff_salary = models.CharField(max_length=100, blank=True, null=True)
    staff_email = models.CharField(max_length=100, blank=True, null=True)
    staff_phone = models.CharField(max_length=100, blank=True, null=True)
    profile_image = models.ImageField(upload_to="Profile images", null=True, blank=True)
    role = models.CharField(max_length=100, blank=True, null=True)


class TableDB(models.Model):
    Table_no=models.CharField(max_length=100, blank=True, null=True)
    Capacity=models.IntegerField(null=True,blank=True)
    active=models.CharField(max_length=100,blank=True,null=True)

class ReservationDB(models.Model):
    customer_name = models.CharField(max_length=100,blank=True,null=True)
    customer_phone = models.CharField(max_length=100, blank=True, null=True)
    Reser_date=models.CharField(max_length=100, blank=True, null=True)
    Reser_time=models.CharField(max_length=100, blank=True, null=True)
    table_num=models.IntegerField(null=True,blank=True)
    status = models.CharField(max_length=100,blank=True,null=True)


class TableBooking(models.Model):
    UserName = models.CharField(max_length=100)
    Table_no = models.CharField(max_length=100)
    Capacity = models.IntegerField()
    Booking_Date = models.DateField()
    Booking_Time = models.TimeField()
    Members = models.IntegerField()
    Status = models.CharField(max_length=50, default="Booked")


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"




