from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message

BOT_TOKEN = '7983523138:AAGyb3InyJzFKasxzTqTtv72X5kpwYpsSNo'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command(commands=["start"]))
async def process_start_message(msg: Message):
    await msg.answer('Привет!\nМеня зовут эхо-бот!\nНапиши мне что-то и я отправлю это тебе!')

@dp.message(Command(commands=["help"]))
async def process_help_message(msg: Message):
    await msg.answer('Я эхо-бот, отправь мне сообщение и я отправлю тебе его')

@dp.message()
async def echo_send(msg: Message):
    await msg.reply(text=msg.text)

if __name__ == '__main__':
    dp.run_polling(bot)