import logging
from loader import db
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from loader import db

categoryMenu = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="💻 Computer", callback_data="computer"),
    ],
    [
        InlineKeyboardButton(text="📱 Smartphone", callback_data="smartphone"),
    ],
    [
        InlineKeyboardButton(text="⌚️ Smartwatch", callback_data="smartwatch"),
    ],
    [
        InlineKeyboardButton(text="🎙 Accessory", callback_data="accessory"),
    ],
    [
        InlineKeyboardButton(text="🖨 Other products", callback_data="otherproducts"),
    ]
        
])

data = await db.get_all_computer()
computerkeyboard = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text=f"{data[i,1]}", callback_data=data[i,0])] for i in range(len(data)) ]
)


# for i in range(len(data)):
#     computerkeyboard.add([InlineKeyboardButton(text = data[i,1], callback_data=data[i,0])])
# computerkeyboard.add([InlineKeyboardButton[text = "⬅️Ortga" , callback_data='back']])
    

smartphonekeyboard = InlineKeyboardMarkup(
    inline_keyboard=[]
)

data = await db.get_all_smartphone()
for i in range(len(data)):
    smartphonekeyboard.add([InlineKeyboardButton(text = data[i,1] , callback_data=data[i,0])])
smartphonekeyboard.add([InlineKeyboardButton(text = "⬅️Ortga" , callback_data='back ')])


smartwatchkeyboard = InlineKeyboardMarkup(
    inline_keyboard=[]
)    
data = await db.get_all_smartwatch()
for i in range(len(data)):
    smartwatchkeyboard.add([InlineKeyboardButton(text = data[i,1] , callback_data=data[i,0])])
smartwatchkeyboard.add([InlineKeyboardButton(text = "⬅️Ortga" , callback_data='back')])
 
 
accessorykeyboard = InlineKeyboardMarkup(
    inline_keyboard=[]
)      
data = await db.get_all_accessory()
for i in range(len(data)):
    accessorykeyboard.add([InlineKeyboardButton(text = data[i,1] , callback_data=data[i,0])])
accessorykeyboard.add([InlineKeyboardButton(text = "⬅️Ortga" , callback_data='back')])
    

otherproductskeyboard = InlineKeyboardMarkup(
    inline_keyboard=[]
)      
data = await db.get_all_otherproducts()
for i in range(len(data)):
    otherproductskeyboard.add([InlineKeyboardButton(text = data[i,1] , callback_data=data[i,0])])
otherproductskeyboard.add([InlineKeyboardButton(text = "⬅️Ortga" , callback_data='back')])