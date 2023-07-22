from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        API_KEY = 'acac3268bbf30e904f84e6c7e14d39be'
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid='+API_KEY).read()
        json_data = json.loads(res)
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp']) + 'K',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
        }

    else:
        city = ''
        data = {}
    return render(request, 'index.html', {'city': city, 'data': data})