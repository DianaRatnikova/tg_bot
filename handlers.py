# Основной файл, в котором будет почти весь код бота. 
# Будет состоять из функций-обработчиков с декораторами (фильтрами)

from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

import kb
import text


router = Router()


def print_text():
    print("Hello world!")

# @router.message => функция является обработчиком входящих сообщений
@router.message(Command("start"))
async def start_handler(msg: Message):
#    await msg.answer("Привет! Я помогу тебе узнать твой ID, просто отправь мне любое сообщение")
    await msg.answer(text.GREET_ACTS.format(name=msg.from_user.full_name), reply_markup=kb.menu)


# @router.message()
# async def message_handler(msg: Message):
#     await msg.answer(f"Твой ID: {msg.from_user.id}")


#@router.message(Command("start"))
#async def start_handler(msg: Message):
    
    
@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
@router.message(F.text == "◀️ Выйти в меню")
async def menu(msg: Message):
    print_text()
    await msg.answer(text.menu, reply_markup=kb.menu)