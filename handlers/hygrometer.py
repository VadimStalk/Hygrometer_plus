"""Main module of the hygrometer"""
from aiogram import Router, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
import tables.hygro_table as hygro_table
from pressure.pressure import get_city_data
from pressure.pressure import get_pressure_data

router = Router()

available_thermometer_readings = [str(key) for key in hygro_table.table]
STATIC_A = 0.0007947

class TempData(StatesGroup):
    """Class that stores states"""

    dry_thermometer_readings = State()
    wetted_thermometer_readings = State()


@router.message(Command("hygro"))
async def cmd_dry_tr(message: Message, state: FSMContext):
    """Function for requesting a dry value"""
    await message.answer(
        text="Давайте я рассчитаю относительную влажность воздуха(%).\n"
        "Укажите температуру сухого термометра(диапозон от -40.9 до 40.9 c шагом 0.1): "
    )
    # Устанавливаем пользователю состояние "темп. сухого термометра"
    await state.set_state(TempData.dry_thermometer_readings)


@router.message(TempData.dry_thermometer_readings, F.text.in_(available_thermometer_readings))
async def dry_tr_chosen(message: Message, state: FSMContext):
    """Function for getting the dry thermometer value"""
    await state.update_data(chosen_dry=float(message.text))
    await message.answer(
        text="Спасибо. Теперь, пожалуйста, укажите температуру \
            смоченного термометра(диапозон от -40.9 до 40.9 c шагом 0.1): "
    )
    await state.set_state(TempData.wetted_thermometer_readings)


@router.message(TempData.dry_thermometer_readings)
async def dry_chosen_incorrectly(message: Message):
    await message.answer(
        text="Похоже что такое значение отсутствует в моих списках.\n"
            "Возможно вы указали значение неверно.\n"
            "Пожалуйста, попробуйте ввести значение \n"
            "сухого термометра ещё раз(диапозон от -40.9 до 40.9 c шагом 0.1):")
    

@router.message(TempData.wetted_thermometer_readings, F.text.in_(available_thermometer_readings))
async def wetted_tr_chosen(message: Message, state: FSMContext):
    """Function for getting the wetted thermometer value"""
    city = get_city_data()
    user_data = await state.get_data()
    dry_temp = user_data["chosen_dry"]
    wetted_temp = float(message.text)
    pres = get_pressure_data()
    e_dry = hygro_table.table[dry_temp]
    e_wetted = hygro_table.table[wetted_temp]
    e_param = e_wetted - STATIC_A * (dry_temp - wetted_temp) * pres
    pres_rt_st = round(760/1013.25*pres, 2)
    ovv = round((100 * e_param / e_dry), 2)
    await message.answer(
        text=f"В вашем городе {city} атмосферное давление составляет: {pres_rt_st} мм рт.ст.\n"
        f"Вы ввели значение сухого термометра {dry_temp}.\n"
        f"Значение смоченного темометра {wetted_temp}.\n\n"
        "В результате рассчетов, исходя из переданных вами данных, \n"
        f"Относительная влажность воздуха(%):  {ovv}."
    )
    await state.clear()

@router.message(TempData.wetted_thermometer_readings)
async def wetted_chosen_incorrectly(message: Message):
    await message.answer(
        text="Похоже что такое значение отсутствует в моих списках.\n"
            "Возможно вы указали значение неверно.\n"
            "Пожалуйста, попробуйте ввести значение \n"
            "смоченного термометра ещё раз(диапозон от -40.9 до 40.9 c шагом 0.1):"
    )

