from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp
from keyboards.client_kb import start_markup
from aiogram.utils.markdown import link


#@dp.message_handler(commands=['start', 'help'])
async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Салам Алейкум {message.from_user.first_name}", reply_markup=start_markup)
    #await message.answer(link('da','https://youtube.com'))

async def info(message: types.Message):
    await message.reply('Я не знаю, лол')


#@dp.message_handler(commands=['mem'])
async def send_image(message: types.Message):
    photo = open('media/lol.jpg', 'rb')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)



#@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data="button_call_1")
    markup.add(button_call_1)
    question = 'Сколько букв в алфавите?'
    answers = [
        '29',
        '32',
        '30',
        '33',
        '20',
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation='Ненадо дядя',
        reply_markup=markup,
        open_period=5,
    )


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start', 'help'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(send_image, commands=['mem'])
    dp.register_message_handler(info, commands=['info'])