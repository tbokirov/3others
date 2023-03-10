from handlers import client, callback, extra, admin, fsm_mentor
from aiogram.utils import executor
from config import dp
import logging

callback.registrer_callback_handlers(dp)
client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
fsm_mentor.register_handlers_fsm_mentor(dp)

extra.register_handler_extra(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
