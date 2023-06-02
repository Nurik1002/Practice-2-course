from aiogram import types
from aiogram.types import  Message
from aiogram.dispatcher import FSMContext
from states.user_state import RegisterState, AddFirmaState
from loader import dp, db
import logging
import re


@dp.message_handler(text="Ro'yxatdan o'tish")
async def royxatdan_otish(msg:Message):
    await msg.answer("Iltimos famliya va ismingizni kiriting! Namuna (Familiya Ism) : ")
    await RegisterState.full_name.set()

@dp.message_handler(state=RegisterState.full_name)
async def get_full_name(msg : Message, state : FSMContext):

    try:
        last_name, first_name = msg.text.split()
        await state.update_data({
            "last_name" : last_name,
            "fist_name" : first_name
        })
        await msg.answer("Iltimos email manzilingizni kiriting! Namuna 'nyarashbayev97@gmail.com'")
        await RegisterState.email.set()

    except:
        await msg.answer("Iltimos familiya va ismingizni to'g'ri kiriting. Namuna 'Yarashbayev Nurgeldi'")



@dp.message_handler(state=RegisterState.email)
async def get_email(msg : Message, state : FSMContext):
    email = msg.text
    if re.match(r"[\w]*@*[a-z]*\.*[\w]{5,}(\.)*(com)*(@gmail\.com)", email):
        await state.update_data({
            "email" : email
        })
        await RegisterState.phone_num.set()
        await msg.answer("Iltimos bog'lainish uchun telefon raqamingzini kiriting! Namuna '913169659'")
    else:
        await msg.answer("Iltimos email manzilingizni to'g'ri kiriting! Namuna 'nyarashbayev97@gmail.com'")
    
@dp.message_handler(state=RegisterState.phone_num)
async def get_phone_num(msg : Message, state : FSMContext):
    phone = msg.text
    if re.match(r"^\d{9}$", phone):
        await state.update_data({
            "phone_num" : phone
        })
        await RegisterState.manzil.set()
        await msg.answer("Iltimos manzilingizni kiriting!")
    else:
        await msg.answer("Iltimos bog'lainish uchun telefon raqamingzini to'g'ri  kiriting! Namuna '913169659'")



@dp.message_handler(state=RegisterState.manzil)
async def get_manzil(msg : Message, state : FSMContext):
    manzil = msg.text
    data = await state.get_data()
    last_name = data["last_name"]
    first_name = data["fist_name"]
    email = data["email"]
    phone_num = data["phone_num"]
    telegram_id=msg.from_user.id
    telegram_username = msg.from_user.username
    await db.add_user(last_name, first_name, email, phone_num, telegram_id, telegram_username, manzil)
    chek_result = await db.check_user(telegram_id=telegram_id)
    logging.info(f"check_result in start.py {chek_result}")
    if chek_result:
        logging.info(f"Foydalanuvchi bazaga qo'shildi {last_name} {first_name} {email} {phone_num} {manzil} {telegram_id} {telegram_username}")
    else:
        logging.info("Foydalanuvchini bazagq qo'shishda xatolik!")
    await  state.finish()
    await msg.answer("/start")




@dp.message_handler(text="Firma qo'shish")
async def add_fima(msg:Message, state : FSMContext):
    await msg.answer("Firma nomini kiriting : ")
    await AddFirmaState.get_name.set()

@dp.message_handler(state=AddFirmaState.get_name)
async def add_fima(msg:Message, state : FSMContext):
    test = msg.text
    await db.add_firma(test)
    await msg.answer("Firma qo'shildi")
    await state.finish()

