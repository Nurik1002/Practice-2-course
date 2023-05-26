from aiogram.dispatcher.filters.state import StatesGroup, State

class RegisterState(StatesGroup):
    full_name = State()
    email = State()
    phone_num = State()
    manzil = State()

class AddFirmaState(StatesGroup):
    get_name = State()