from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

show_base = KeyboardButton('/show_base')
exit = KeyboardButton('/exit')
new = KeyboardButton('/new')
add = KeyboardButton('/add')
delete = KeyboardButton('/del')


kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
# kb_client.add(b1).insert(b2) # add - с новой строки, insert - добавляет к строке

kb_client.row(new, add, show_base)  # всё в строку
kb_client.row(delete, exit)

