from django.db import models

# Create your models here.

CITY_CHOICES= [
    ('mumbai', 'MUMBAI'),
    ('delhi', 'DELHI'),
    ('chennai', 'CHENNAI'),
    ('bangalore', 'BANGALORE'),
    ('kolkata', 'KOLKATA'),
    ]

class Automate_Email(models.Model):
    Receiver_name = models.CharField(max_length=50)
    Email = models.EmailField(max_length = 100)
    City = models.CharField(max_length = 30,choices=CITY_CHOICES)
    Time = models.TimeField()

