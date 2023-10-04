"""Module determining weather data in a particular city."""
import os
from urllib.request import urlopen
import json
from aiogram import Router
from aiogram.filters import Command
from aiogram import types

import requests


router = Router()


@router.message(Command("city_weather"))
async def get_ip_and_weather_data(message: types.Message):
    """Function for determining the city and weather"""
    url = "http://ipinfo.io/json"
    response = urlopen(url)
    city = json.load(response)["city"]
    res = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv("API_KEY")}&units=metric',
        timeout=10,
    )

    if res.status_code == 200:
        data = json.loads(res.text)
        print(data)
        temp = data["main"]["temp"]
        answer = f"В городе {city} температура: {temp}°C"
        await message.answer(answer)

    else:
        print("Ошибка")
        await message.answer(f"Уверен что правильно написал: {city}? Попробуй ещё")
