"""Auxiliary module for transmitting pressure values"""
import os
from urllib.request import urlopen
import json
from dotenv import load_dotenv, find_dotenv
import requests

def get_city_data():
    """Function for getting the city name"""
    load_dotenv(find_dotenv())
    url = "http://ipinfo.io/json"
    response = urlopen(url)
    city = json.load(response)["city"]
    return city


def get_pressure_data():
    """Function for getting the pressure value"""
    load_dotenv(find_dotenv())
    url = "http://ipinfo.io/json"
    response = urlopen(url)
    city = json.load(response)["city"]
    res = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv("API_KEY")}&units=metric',
        timeout=10,
    )

    if res.status_code == 200:
        data = json.loads(res.text)
        pressure = int(data["main"]["pressure"])
        return pressure

    else:
        return None
