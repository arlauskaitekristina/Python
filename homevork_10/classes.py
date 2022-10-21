from aiogram.dispatcher.filters.state import State, StatesGroup


class Database(StatesGroup):
    state1 = State()
    state2 = State()
    state3 = State()


class AddInfo(StatesGroup):
    state1 = State()
    state2 = State()
    state3 = State()


class DelInfo(StatesGroup):
    state1 = State()

