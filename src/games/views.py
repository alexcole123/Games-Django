from django.shortcuts import render
from requests import get

from utils.app_config import AppConfig

# Home view:
def home(request): # View Function (request is an object containing request data)
    context = { "active": "home" }
    return render(request, "home.html", context)

#About view:
def about(request):
    context = { "active": "about" }
    return render(request, "about.html", context)

# Weather View
# Weather View
def weather(request):
    weatherObject = get(AppConfig.weather_url).json()
    description = weatherObject["weather"][0]["description"]
    temperature = weatherObject["main"]["temp"]
    icon_code = weatherObject["weather"][0]["icon"]
    context = { "active": "weather", "description": description, "temperature": temperature, "icon_code": icon_code}
    return render(request, "weather.html", context)
