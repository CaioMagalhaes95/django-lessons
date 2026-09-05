from django.shortcuts import render
import requests

def index(request):
    if request.method == "POST":
        city1 = request.POST["city1"]
        weather_data1 = fetch_weather(city1)

        context = {
            "weather_data1": weather_data1,
        }
        return render(request, "app/index.html", context)

    return render(request, "app/index.html")

def fetch_weather(city):
    response = requests.get(
        "https://api.openweathermap.org/data/2.5/weather",
        params={
            "q": city,
            "appid": "API KEY",
            "units": "metric",
        },
        timeout=10,
    )
    response.raise_for_status()
    return response.json()