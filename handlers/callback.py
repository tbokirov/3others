from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp



@dp.callback_query_handler(text="button_call_1")
async def quiz_2(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data="button_call_2")
    markup.add(button_call_1)
    question = 'Сколько будет 20 + 5?'
    answers = [
        '4',
        '5',
        '6',
        'НЕЗНАЮ',
        '25',
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=4,
        explanation='Ненадо дядя',
        reply_markup=markup,
        open_period=5,
    )
@dp.callback_query_handler(text="button_call_2")
async def quiz_3(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data="button_call_2")
    markup.add(button_call_1)
    question = 'Где живут китайцы?'
    answers = [
        'Индонезия',
        'Китай',
        'Бангладеш',
        'НЕЗНАЮ',
        'Дагестан',
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=4,
        explanation='Ненадо дядя',
        reply_markup=markup,
        open_period=5,
    )
def registrer_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="button_call_1")
    dp.register_callback_query_handler(quiz_3, text="button_call_2")