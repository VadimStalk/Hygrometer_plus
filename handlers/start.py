"""Module /start"""
import datetime
from random import randint
from aiogram.filters import Command
from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
import tables.motivation as motivation
from keyboards.for_questions import get_yes_no_kb


router = Router()


@router.message(Command("start"))
async def start_message(message: Message):
    """Function welcome"""
    # await bot.send_message(message.chat.id, 'Hello')
    print(f"UserID: {message.from_user.id}, Name: {message.from_user.first_name}")
    week_dict = {
        0: "понедельник",
        1: "вторник",
        2: "среда",
        3: "четверг",
        4: "пятница",
        5: "суббота",
        6: "воскресенье",
    }

    now_hour = int(datetime.datetime.today().hour)
    if now_hour in range(5, 12, 1):
        greeting = "Доброе утро"
    if now_hour in range(12, 17, 1):
        greeting = "Добрый день"
    if now_hour in range(17, 23, 1):
        greeting = "Добрый вечер"
    if now_hour in range(23, 25):
        greeting = "Какой же чудный поздний вечер"
    if now_hour in range(0, 5, 1):
        greeting = "Приветствую, довольно поздно для бесед"

    count_desc = len(motivation.desc)
    rand_desc = randint(0, count_desc - 1)
    com_desc = motivation.desc.get(rand_desc)

    day = week_dict.get(datetime.datetime.today().weekday())

    count_dict = len(motivation.mot)
    rand = randint(0, count_dict - 1)
    comment = motivation.mot.get(rand)

    name = message.from_user.first_name
    await message.answer(
        f"{greeting}, дорогой(-ая) {name}!\n"
        f"Сегодня {com_desc} день - {day}!\n"
        f'Может вам доводилось задуматься об этом: "{comment}"\n\n'
        f"Вы довольны своей работой?",
        reply_markup=get_yes_no_kb(),
    )


@router.message(F.text.lower() == "да")
async def answer_yes(message: Message):
    """Function asking"""
    await message.answer("Это здорово!", reply_markup=ReplyKeyboardRemove())


@router.message(F.text.lower() == "нет")
async def answer_no(message: Message):
    """Function asking"""
    await message.answer(
        "Жаль... Может быть пора что-то менять?!", reply_markup=ReplyKeyboardRemove()
    )
