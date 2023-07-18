import time
import asyncio
from aiogram import Bot, Dispatcher, executor, types
import random
import config

API_TOKEN = '6322175401:AAEFXOVrIy63gVgwK2HkBUC_4iOLkmq-SoQ'

bot = Bot(config.TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message= types.Message):
    await message.answer('Данный бот общается с вами и chatgpt')
    await message.delete()

@dp.message_handler(commands=['help'])
async def echo(message: types.Message):
    await message.answer(config.HELP_INFO)

@dp.message_handler(commands=['description'])
async def echo(message: types.Message):
    await message.answer(config.DESCRIPTION_INFO)


@dp.message_handler(commands=['greet'])
async def echo(message: types.Message):
    await message.reply('Hello, what is your name?')

@dp.message_handler()
async def send_random_letter(message: types.Message):
    # Генерируем случайную букву алфавита и отправляем ее пользователю
    letter = random.choice('abcdefghijklmnopqrstuvwxyz')
    await message.answer(letter)
def main():
    executor.start_polling(dp, skip_updates=True)
if __name__ == '__main__':
    asyncio.run(main())
