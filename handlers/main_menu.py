from aiogram import types, Dispatcher, Router
from aiogram.filters import Command

from keyboards.catalog_kb import catalog_menu
from keyboards.main_menu_kb import main_menu

router = Router()


@router.message(Command('start'))
async def send_welcome(message: types.Message):
    await message.answer("Привет) Вы попали в чат-помощник! Выберете раздел, который Вас интересует)", reply_markup=main_menu)


@router.message(lambda message: message.text == "Каталог")
async def show_catalog(message: types.Message):
    await message.answer("Добро пожаловать в каталог бренда JUTI. В данном разделе Вы можете изучить ассортимент в наличии или позиции доступные для предзаказа предстоящей коллекции.", reply_markup=catalog_menu)


@router.message(lambda message: message.text == "Назад")
async def go_back(message: types.Message):
    await message.answer("Возвращаемся в главное меню.", reply_markup=main_menu)




