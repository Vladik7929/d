from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, ReplyKeyboardRemove
from aiogram.utils import executor

TOKEN_API = '6362347816:AAEOm28yiGlWETmaH2OuAQNU_I0Hu_Way7M'

# инициализация бота и диспетчера
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

HELP_INFO = '''
/start - start the bot
/open_menu - open the menu
/help - help
'''
kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton(text='/start', command='start')
b2 = KeyboardButton(text='/help', command='help')
b3 = KeyboardButton(text='/open_menu')
b4 = KeyboardButton(text='You can not use the previous button because you are in menu ans you can not open it twice!')
kb.add(b1, b2, b3, b4)
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(text='Bot had started', chat_id=message.from_user.id, reply_markup=ReplyKeyboardRemove())
@dp.message_handler(commands=['open_menu'], reply_markup=ReplyKeyboardRemove())
async def open_menu(message: types.Message):
    ikb = InlineKeyboardMarkup(row_width=2)
    ib1 = InlineKeyboardButton(text='Yes, I want to open the menu', callback_data='open_menu')
    ib2 = InlineKeyboardButton(text='No, I do not want to open the menu', callback_data='notopen_menu')
    ikb.add(ib1, ib2)
    await bot.send_message(chat_id=message.from_user.id, text='Do you want to open the menu?', reply_markup=ikb)
@dp.message_handler(commands=['help'], reply_markup=ReplyKeyboardRemove())
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=HELP_INFO)
@dp.callback_query_handler()
async def callback_query(callback: types.CallbackQuery):
    if callback.data == 'open_menu':

        await callback.answer(text='Menu opened succesfully')
    await callback.answer(text='Ok, you did not open the menu')
# запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
