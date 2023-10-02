"""Auxiliary module for '/start', button creation"""
from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder



def get_yes_no_kb() -> ReplyKeyboardMarkup:
    """Function for creating two buttons"""
    keyb = ReplyKeyboardBuilder()
    keyb.button(text="Да")
    keyb.button(text="Нет")
    keyb.adjust(2)
    return keyb.as_markup(resize_keyboard=True)
