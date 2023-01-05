from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=3
)

info_button = KeyboardButton('/info')
start_button = KeyboardButton("/start")
quiz_button = KeyboardButton('/quiz')
mem_button = KeyboardButton('/mem')

share_location = KeyboardButton("Share location", request_location=True)
share_contact = KeyboardButton("Share contact", request_contact=True)

start_markup.add(mem_button, info_button, start_button, quiz_button, share_location, share_contact)

