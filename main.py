from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ContentType
from aiogram import F
import logging

BOT_TOKEN = '7983523138:AAGyb3InyJzFKasxzTqTtv72X5kpwYpsSNo' #токен бота

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

async def process_start_message(message: types.Message):
    await message.answer('Привет!\nМеня зовут эхо-бот!\nНапиши мне что-то и я отправлю это тебе!')


async def process_help_message(message: types.Message):
    await message.answer('Я эхо-бот, отправь мне сообщение и я отправлю тебе его')


async def echo_photo(message: types.Message):
    await message.reply_photo(message.photo[0].file_id)


async def echo_sticker(message: types.Message):
    await message.reply_sticker(message.sticker.file_id)
    info = (
        f"ℹ️ Информация о стикере:\n"
        f"ID: {message.sticker.file_id}\n"
        f"Набор: {message.sticker.set_name or 'нет'}\n"
        f"Эмодзи: {message.sticker.emoji or 'нет'}\n"
        f"Анимированный: {'да' if message.sticker.is_animated else 'нет'}"
    )
    await message.answer(info)

async def echo_video(message: types.Message):
    await message.reply_video(message.video.file_id)


async def echo_video_message(message: types.Message):
    await message.reply_video_note(message.video_note.file_id)


async def echo_document(message: types.Message):
    await message.reply_document(message.document.file_id)


async def echo_voice(message: types.Message):
    await message.reply_voice(message.voice.file_id)


async def echo_geo(message: types.Message):
    await message.reply_location( latitude=message.location.latitude, longitude=message.location.longitude)


async def echo_send(message: types.Message):
    await message.reply(text=message.text)

dp.message.register(process_start_message, Command(commands='start'))
dp.message.register(process_help_message, Command(commands='help'))
dp.message.register(echo_voice, F.voice)
dp.message.register(echo_photo, F.photo)
dp.message.register(echo_video, F.video)
dp.message.register(echo_sticker, F.sticker)
dp.message.register(echo_document, F.document)
dp.message.register(echo_video_message, F.video_note)
dp.message.register(echo_geo, F.location)
dp.message.register(echo_send)

if __name__ == '__main__':
    dp.run_polling(bot)