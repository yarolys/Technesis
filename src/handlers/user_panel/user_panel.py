from io import BytesIO
import pandas as pd

from asyncio.log import logger
from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from src.database.models.website import Website

router = Router()


@router.message(F.document, F.document.file_name.endswith(('.xlsx', '.xls')))
async def upload_file_handler(message: Message, state: FSMContext):
    try:
        file = await message.bot.get_file(message.document.file_id)
        file_bytes = await message.bot.download_file(file.file_path)

        df = pd.read_excel(BytesIO(file_bytes.read()))

        required_columns = ['title', 'url', 'xpath']
        if not all(col in df.columns for col in required_columns):
            missing = set(required_columns) - set(df.columns)
            await message.answer(f"В файле отсутствуют обязательные колонки: {', '.join(missing)}")
            return

        await Website.dataframe(df)

        await message.answer("Файл успешно обработан. Содержимое:\n" + df.to_string(index=False))

    except Exception as e:
        logger.exception("Ошибка при обработке Excel-файла:")
        await message.answer(f"Произошла ошибка при обработке файла: {str(e)}")

