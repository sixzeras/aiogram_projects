from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram import F
from dotenv import load_dotenv
import logging
import os


load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


logging.basicConfig(level=logging.INFO)


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command(commands='start'))
async def process_start_message(message: types.Message):
    await message.answer('Привет!\nМеня зовут эхо-бот!\nНапиши мне что-то и я отправлю это тебе!')


@dp.message(Command(commands='help'))
async def process_help_message(message: types.Message):
    await message.answer('Я эхо-бот, отправь мне сообщение и я отправлю тебе его')


@dp.message(F.sticker)
async def echo_sticker(message: types.Message):
    print(message.model_dump(exclude_none=True))
    await message.reply_sticker(message.sticker.file_id)
    info = (
        f"ℹ️ Информация о стикере:\n"
        f"ID: {message.sticker.file_id}\n"
        f"Набор: {message.sticker.set_name or 'нет'}\n"
        f"Эмодзи: {message.sticker.emoji or 'нет'}\n"
    )
    await message.answer(info)


@dp.message()
async def send_echo(message: types.message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(
            text='Этот тип апдейтов не поддерживается'
            'методом send.copy' 
        )


if __name__ == '__main__':
    dp.run_polling(bot)