"""Module determining weather data."""
import json
import os
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
import requests


router = Router()


@router.message(Command("weather"))
async def get_weather_data(message: Message):
    """Function for determining the city"""
    await message.answer("Я готов рассказать тебе о погоде, напиши название города")


@router.message()
async def get_chosen_city(message: Message):
    """Function for determining weather data"""
    city_text = message.text.strip().lower()
    print(city_text)
    res = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={city_text}&appid={os.getenv("API_KEY")}&units=metric',
        timeout=10,
    )
    # await state.update_data(res.status_code == 200)
    print(res.status_code)
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        print(data)
        await message.reply(f"Сейчас погода: {temp}, \n" f"ощущается как {feels_like}")
    else:
        await message.answer(f"Уверен что правильно написал: {city_text}? Попробуй ещё")
