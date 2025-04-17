from aiogram import types
from aiogram.types import (
    InlineKeyboardMarkup, 
    ReplyKeyboardMarkup,
    KeyboardButton,
)


master_panel_inline_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='')]
        ],
    resize_keyboard=True
)
