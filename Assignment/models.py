from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

import json
# urllib.request to make a request to api
import urllib.request
from django.conf import settings
from django.core.mail import send_mail



CITY_CHOICES= [
    ('mumbai', 'MUMBAI'),
    ('delhi', 'DELHI'),
    ('chennai', 'CHENNAI'),
    ('bangalore', 'BANGALORE'),
    ('kolkata', 'KOLKATA'),
    ]

def home(city):
        # source contain JSON data from API
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+ city + '&appid=f3fa285f6ba80291a712261723272976').read()
  
        # converting JSON data to a dictionary
        list_of_data = json.loads(source)

        # extracting temp in kelvin placed inside nested dictionary.
        temp_in_kelvin = list_of_data['main']['temp']
        temperature = temp_in_kelvin - 273.15
        return temperature
        


class Automate_Email(models.Model):
    Receiver_name = models.CharField(max_length=50)
    Email = models.EmailField(max_length = 100)
    City = models.CharField(max_length=30,choices=CITY_CHOICES)
    Time = models.TimeField()
    
    #when new data is fed from admin page, it returns the email_id back
    def  __str__(self):
         return self.Email

#receive the email id sent by above
# method for updating


@receiver(post_save, sender=Automate_Email)
def new_user_data(sender, instance, **kwargs):
    email_received = instance
    print(email_received)
    #fetch the city from the data of email_received
    data = Automate_Email.objects.filter(Email=email_received)[0]
    city=data.City
    receiver = data.Receiver_name
    temperature = home(city)
    if temperature < 10:
        emoji = '☃️'
    elif temperature >10 and temperature <15:
        emoji = '🥶'
    elif temperature >15 and temperature <25:
        emoji = '🌞'
    elif temperature >25 and temperature <35:
        emoji = '😰'
    else:
        emoji = '🔥'
    

    subject = 'Hi '+ receiver +', interested in our services'
    message = f''+city.upper()+' TEMPERATURE: '+str(round(temperature))+ ' °C ' + emoji
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email_received, ]
    send_mail( subject, message, email_from, recipient_list )
    

