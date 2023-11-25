from django.db import models
from django.contrib.auth.models import User  # Import the User model

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

class Reservation(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Correct import
    reservation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} reserved {self.car.year} {self.car.make} {self.car.model} on {self.reservation_date}"

class Dealer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username

class CarPost(models.Model):
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Add any additional fields relevant to the car post

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"