from django.db import models
from AdminApp.models import FoodDb, TableDB


# Create your models here.


class CustomerDb(models.Model):
    customer_name = models.CharField(max_length=100, blank=True, null=True)
    customer_email = models.CharField(max_length=100, blank=True, null=True)
    customer_phone = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)



class CartDbModel(models.Model):
    UserName = models.CharField(max_length=100)
    food = models.ForeignKey(FoodDb, on_delete=models.CASCADE)
    Quantity = models.PositiveIntegerField(default=1)
    Total_Price = models.IntegerField()

class OrderModel(models.Model):
    UserName = models.CharField(max_length=100)
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Phone = models.CharField(max_length=15)
    Address = models.TextField()
    Payment = models.CharField(max_length=50)
    Grand_Total = models.IntegerField()
    Ordered_Date = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    Order = models.ForeignKey(OrderModel, on_delete=models.CASCADE)
    Food = models.ForeignKey(FoodDb, on_delete=models.CASCADE)
    Quantity = models.IntegerField()
    Total_Price = models.IntegerField()


class RegistrationDb(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    password =models.CharField(max_length=100, blank=True, null=True)
    confirm_password =models.CharField(max_length=100, blank=True, null=True)



class BookingDB(models.Model):
    STATUS_CHOICES = [
        ("Booked", "Booked"),
        ("Confirmed", "Confirmed"),
        ("Completed", "Completed"),
        ("Cancelled", "Cancelled"),
    ]
    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    guests = models.IntegerField()
    table = models.ForeignKey(TableDB, on_delete=models.CASCADE)
    email = models.EmailField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Booked"
    )

    def __str__(self):
        return self.customer_name

