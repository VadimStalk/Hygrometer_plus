"""Main module of the chatbot."""

import asyncio
import logging
import os
from dotenv import load_dotenv, find_dotenv
from aiogram import Bot, Dispatcher
from handlers import start, special_buttons, city_weather, weather, hygrometer


async def main():
    """Function that starts the chatbot"""
    logging.basicConfig(level=logging.INFO)
    load_dotenv(find_dotenv())
    bot = Bot(os.getenv("API_TOKEN"))
    dispatcher = Dispatcher()

    dispatcher.include_routers(
        start.router,
        hygrometer.router,
        special_buttons.router,
        city_weather.router,
        weather.router,
    )
    await bot.delete_webhook(drop_pending_updates=True)
    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
