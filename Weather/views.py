from django.shortcuts import render

# Create your views here.
import requests
import urllib.request
import json

def weather(request):
    if request.method == 'POST':
        city = request.POST['city']

        source = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=98cd4ff499ecc5c41ec2878673fc2efc'
        data_list = requests.get(source).json()
    

        data = {
            "country_code": str(data_list['sys']['country']),
            "coordinate": str(data_list['coord']['lon']) + ', '
            + str(data_list['coord']['lat']),

            "temp": str(data_list['main']['temp']) + ' °C',
            "pressure": str(data_list['main']['pressure']),
            "humidity": str(data_list['main']['humidity']),
            'main': str(data_list['weather'][0]['main']),
            'description': str(data_list['weather'][0]['description']),
            'icon': data_list['weather'][0]['icon'],
        }
        print(data)
    else:
        data = {}

    return render(request, "home.html", data)


    #98cd4ff499ecc5c41ec2878673fc2efc
    
   
        