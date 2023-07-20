from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, \
    CallbackQuery, ReplyKeyboardRemove
from aiogram.utils import executor
import gpt4free

TOKEN_API = '6362347816:AAEOm28yiGlWETmaH2OuAQNU_I0Hu_Way7M'

# инициализация бота и диспетчера
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

stateGPT = False
statepictures = False

HELP_INFO = '''
/start - start the bot
/open_menu - open the menu
/help - help
'''
menu = ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(KeyboardButton(text='/start', command='/start'))
menu.add(KeyboardButton(text='/help', command='/help'))
menu.add(KeyboardButton(text='/enableGPT', command='/enableGPT'))
menu.add(KeyboardButton(text='/disableGPT', command='/disableGPT'))
menu.add(KeyboardButton(text='/open_menu', callback_data='onemoremenuopeningwhilemenuisopened'))
menu.add(KeyboardButton(text='ATTENTION, you can not open the menu while menu is opened'))

ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='Yes, I want to open the menu', callback_data='open_menu')
ib2 = InlineKeyboardButton(text='No, I do not want to open the menu', callback_data='notopen_menu')
ikb.add(ib1, ib2)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(text='Bot had started', chat_id=message.from_user.id, reply_markup=menu)


@dp.message_handler(commands=['open_menu'])
async def open_menu(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text='Do you want to open the menu?', reply_markup=ikb)


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP_INFO,
                           reply_markup=ReplyKeyboardRemove())
@dp.message_handler(commands=['enableGPT'])
async def enableGPT(message: types.Message):
    global stateGPT
    stateGPT = True
    await bot.send_message(chat_id=message.from_user.id, text='GPT has been enabled')
@dp.message_handler(commands=['disableGPT'])
async def disableGPT(message: types.Message):
    global stateGPT
    stateGPT = False
    await bot.send_message(chat_id=message.from_user.id, text='GPT has been disabled')

@dp.message_handler(commands=['photogener'])
async def photogener(message: types.Message):
    global statepictures
    statepictures = True
    await bot.send_message(chat_id=message.from_user.id, text='GPT has been enabled')


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

@dp.callback_query_handler()
async def callback_query(callback: types.CallbackQuery):
    if callback.data == 'open_menu':
        # message = await bot.send_message(chat_id=callback.from_user.id,
        #                                  reply_markup=menu,
        #                                  text='The menu had been opened')
        await bot.send_message(text='The menu had been opened', reply_markup=menu, chat_id=callback.from_user.id)
        # await bot.send_message(callback.from_user.id, reply_markup=menu, text='This message will be deleted in 1 second')
        # await bot.delete_message(chat_id=callback.from_user.id, message_id=message.message_id)
    #     await bot.edit_message_reply_markup(chat_id=callback.message.chat.id,
    #                                         message_id=callback.message.message_id,
    #                                         reply_markup=menu)
    else:
        await bot.send_message(text='The menu had not been opened', reply_markup= ReplyKeyboardRemove(), chat_id=callback.from_user.id)


# запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
