from django.http.request import host_validation_re
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import json
# urllib.request to make a request to api
import urllib.request


def home(request):
    if request.method == 'GET':
        city = 'Chicago'
        ''' api key might be expired use your own api_key
            place api_key in place of appid ="your_api_key_here "  '''
  
        # source contain JSON data from API
  
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+ city + '&appid=f3fa285f6ba80291a712261723272976').read()
  
        # converting JSON data to a dictionary
        list_of_data = json.loads(source)
  
        # data for variable list_of_data
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + 'k',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
        }
        print(data)
    else:
        data ='keshabh'
    return HttpResponse(data)
