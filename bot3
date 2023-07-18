import time
import asyncio
from aiogram import Bot, Dispatcher, executor, types
import config
import random

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

count = 0 # счетчик вызовов функции

@dp.message_handler(commands=['count'])
async def send_count(message: types.Message):
    global count # объявляем, что будем использовать глобальную переменную count
    count += 1 # увеличиваем значение счетчика на 1 при каждом вызове функции
    await message.answer(f'Количество вызовов функции: {count}')


@dp.message_handler()
async def send_random_letter_or_answer_yes_no(message: types.Message):
    global count  # объявляем, что будем использовать глобальную переменную count

    # Если сообщение пользователя содержит число 0 или 'NO', то отвечаем 'NO', иначе - случайной буквой алфавита
    if '0' in message.text or 'NO' in message.text:
        answer = 'NO'
    else:
        answer = random.choice('abcdefghijklmnopqrstuvwxyz')

    # Отправляем ответ пользователю и увеличиваем значение счетчика на 1 при каждом вызове функции
    await message.answer(answer)
    count += 1
def main():
    executor.start_polling(dp, skip_updates=True)
if __name__ == '__main__':
    asyncio.run(main())
