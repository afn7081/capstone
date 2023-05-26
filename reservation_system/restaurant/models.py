from django.db import models

# Create your models here.
class booking(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30)
    number_of_guests=models.IntegerField()
    booking_date=models.DateTimeField()

class menu(models.Model):
    id = models.BigAutoField(primary_key=True)
    tiltle = models.CharField(max_length=30)
    price=models.DecimalField(decimal_places=4,max_digits=9)
    inventory=models.IntegerField()