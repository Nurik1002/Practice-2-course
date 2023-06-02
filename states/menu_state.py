from aiogram.dispatcher.filters.state import StatesGroup, State

class MenuState(StatesGroup):
    category  = State()
    product = State()
    