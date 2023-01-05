from aiogram import types, Dispatcher
from config import bot, dp
from config import ADMINS


async def echo(message: types.Message):
    if message.chat.type != "private":
        bad_words = ['java', 'html', 'дурак', 'чокун']
        username = f"@{message.from_user.username}" \
            if message.from_user.username is not None else message.from_user.full_name

        for i in bad_words:
            if i in message.text.lower().replace(' ', ''):
                await bot.delete_message(message.chat.id, message.message_id)
                await message.answer(f"Не матерись {username}, "
                                     f"сам ты {i}!")

    if message.chat.type != 'private':
        if message.from_user.id in ADMINS:
            if message.text.startswith('game'):
                await bot.send_dice(message.chat.id, emoji='🎰')

            elif message.reply_to_message and message.text.startswith('!pin'):
                await bot.pin_chat_message(message.chat.id, message.message_id)


def register_handler_extra(dp: Dispatcher):
    dp.register_message_handler(echo)