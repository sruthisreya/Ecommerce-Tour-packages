from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    email=models.EmailField(max_length=100,unique=True)
    phone_no=models.CharField(max_length=100)
    def __str__(self):
        return self.email 
class TourPackage(models.Model):
    name = models.CharField(max_length=200)  
    description = models.TextField()  
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    start_date=models.DateField()
    end_date=models.DateField()
    destination = models.CharField(max_length=200) 
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Bookingpackage(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    package=models.ForeignKey(TourPackage,on_delete=models.CASCADE)
    no_ofpeople=models.PositiveIntegerField()
    travel_date=models.DateField()
    book_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} {self.package.name}"