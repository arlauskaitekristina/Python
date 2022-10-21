import comands
import json
import requests
import datetime
from config import tg_bot_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token = tg_bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start", "help"])
async def start_commands(message: types.Message):
    button = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button.add(types.KeyboardButton("Добавить контакт"), ("Удалить контакт"), ("Поиск"))
    
    await message.answer("Вы можете выполнять следующие операции с этой телефонной книгой: \n/add - Добавить контакт;\n/delete - Удалить контакт;\n/search - Поиск контакта;\nПожалуйста, введите свой выбор: ", reply_markup=button)



if __name__ == '__main__':
    executor.start_polling(dp)