from aiogram import types
from aiogram.types import  Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from states.menu_state import MenuState
from loader import dp, db
from typing import Union
from aiogram import types
from keyboards.inline.menu_inline import categoryMenu, computerkeyboard, smartwatchkeyboard, smartphonekeyboard, accessorykeyboard, otherproductskeyboard


@dp.message_handler(text="Bosh menyu")
async def show_menu(message: types.Message):
    await message.answer("Mahsulotni tanlang : ", reply_markup=categoryMenu)
    await MenuState.category.set()
    
@dp.callback_query_handler(state=MenuState.category)
async def show_products(call : CallbackQuery, state : FSMContext):
    if call.data == "computer":
        await call.message.edit_text("Mahsulot tanlang", reply_markup=computerkeyboard)
    elif call.data == "smartphone":
        await call.message.edit_text("Mahsulot tanlang", reply_markup=smartphonekeyboard)
    elif call.data == "smartwatch":
        await call.message.edit_text("Mahsulot tanlang", reply_markup=smartwatchkeyboard)
    elif call.data == "accessory":
        await call.message.edit_text("Mahsulot tanlang", reply_markup=accessorykeyboard)
    elif call.data == "otherproducts":
        await call.message.edit_text("Mahsulot tanlang", reply_markup=otherproductskeyboard)
        