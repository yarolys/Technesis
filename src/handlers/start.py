from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command

from src.config import BOT_ADMIN_ID

router = Router()


@router.message(Command('start'), F.chat.type == 'private')
async def start(message: Message):
    user_name = message.from_user.full_name
    await message.answer(
        f'Добро пожаловать, {user_name}. Этот бот - тестовое задание для компании Technesis.\n'
        'Просто отправь мне файл в формате .xlsx и чтобы в её содержании было:\n\n'
        'title url xpath, и я выведу его содержимое.\n\n'
        'Создал: @KandyBobby'
    )
    if message.from_user.id == BOT_ADMIN_ID:
        await message.answer('Для запуска админки нажми /admin')
