from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    train_number = models.IntegerField()
    train_name = models.CharField(max_length=50)
    departure_station = models.CharField(max_length=100)
    arrival_station = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    class_type = models.CharField(max_length=30, null=True, default="Sleeper")

    def __str__(self):
        return f"{self.train_number}-{self.train_name}"
