from aiogram.types import Message
from aiogram import Router
from aiogram.filters import Command
from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder

router = Router()


@router.message(Command("special_buttons"))
async def special_buttons(message: Message):
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text="Запросить геолокацию", request_location=True),
        types.KeyboardButton(text="Запросить контакт", request_contact=True),
    )
    builder.adjust(2)
    await message.answer("Выберите действие:", reply_markup=builder.as_markup(resize_keyboard=True))


# @router.message(F.text.lower() == "Запросить геолокацию")
# async def answer_yes(message: Message):
#     await message.answer(
#         "Ваше местоположение!",
#         reply_markup=ReplyKeyboardRemove()
#     )

# @router.message(F.text.lower() == "Запросить контакт")
# async def answer_no(message: Message):
#     await message.answer(
#         "Ваши контакты",
#         reply_markup=ReplyKeyboardRemove()
#     )
