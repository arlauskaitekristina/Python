from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from aiogram import Bot, types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import ParseMode
import aiogram.utils.markdown as md
from keyboards import kb_client
from classes import *
import database as db
import config
import csv
import os

bot = Bot(config.TOKEN)
storage=MemoryStorage()
dp = Dispatcher(bot, storage=storage)

new = Database()
add = AddInfo()
del_line = DelInfo()

@dp.message_handler(commands=['start', 'help'])
async def commands_start(massage: types.Message):
    await bot.send_message(massage.from_user.id, 'Здравствуй, пользователь\nДля того чтобы начать пользоваться справочником, выбери команду:', reply_markup=kb_client)

@dp.message_handler(state="*", commands='exit')
@dp.message_handler(Text(equals='exit', ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Окей')

@dp.message_handler(commands=['new'])
async def new_db(message: types.Message):
    database1 = db.create_new()
    await bot.send_message(message.from_user.id, f'Создание нового справочника: {database1}')
    await bot.send_message(message.from_user.id, f'Введите название первого столбца:')
    await new.state1.set()

@dp.message_handler(state=new.state1)
async def col1_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['state1'] = message.text
    await new.next()
    await message.reply('Название второго:')
    await new.state2.set()

@dp.message_handler(state=new.state2)
async def col2_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['state2'] = message.text
    await new.next()
    await message.reply('Название третьего:')
    await new.state3.set()

@dp.message_handler(state=new.state3)
async def col3_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['state3'] = message.text
        await bot.send_message(
            message.from_user.id,
            md.text(
                md.text(f'One:', data['state1']),
                md.text(f'Two:', data['state2']),
                md.text(f'Three:', data['state3']),
                sep='\n',
            ),
            parse_mode=ParseMode.MARKDOWN)
    cols = [data['state1'], data['state2'], data['state3']]
    db.set_cols(cols)
    await state.finish()
    

@dp.message_handler(commands=['add'])
async def add_info(message: types.Message):
    await bot.send_message(message.from_user.id, f'Введите фамилию:')
    await add.state1.set()

@dp.message_handler(state=add.state1)
async def col1_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['state1'] = message.text
    await add.next()
    await message.reply("Введите имя: ")
    await add.state2.set()

@dp.message_handler(state=add.state2)
async def col2_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['state2'] = message.text
    await add.next()
    await message.reply("Введите номер телефона: ")
    await add. state3.set()

@dp.message_handler(state=add.state3)
async def col3_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['state3'] = message.text
        await bot.send_message(
            message.from_user.id,
            md.text(
                md.text(f'one:', data['state1']),
                md.text(f'Two:', data['state2']),
                md.text(f'Three:', data['state3']),
                sep='\n',
            ),
            parse_mode=ParseMode.MARKDOWN)
    cols = [data['state1'], data['state2'], data['state3']]
    db.save_data(cols)
    print(cols)
    await state.finish()

@dp.message_handler(commands=['show_base'])
async def show_base(message: types.Message):
    rows = db.get_cols()
    with open(db.show_current(), encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        for row in reader:
            await bot.send_message(message.from_user.id, f'{row[rows[0]]}, {row[rows[1]]}, {row[rows[2]]}')

@dp.message_handler(commands=['del'])
async def delete(message: types.Message):
    await bot.send_message(message.from_user.id, f'Введите номер телефона, который хотите удалить:')
    await del_line.state1.set()


@dp.message_handler(state=del_line.state1)
async def del_request(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        numbers = message.text.replace(' ', ',').replace(';', ',').replace('.', ',').split(',')
        list1 = list(map(int, numbers))
        data['state1'] = list1
        await bot.send_message(message.from_user.id, f'Номер телефона: {list1} был удален')
    indexes = data['state1']
    print(indexes)
    db.delete(indexes)
    await state.finish()
    
    

# @dp.message_handler()
# async def commands_start(massage: types.Message):
#     if message.text == 'Привет':
#         await message.answer('И тебе привет')
# await message.answer(message.text)  # просто ответ
# await message.reply(message.text)  # ответ с цитированием собщения пользователя
# await bot.send_message(message.from_user.id, message.text) #ответ в личку 