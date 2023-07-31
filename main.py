from __future__ import print_function
from create_bot import dp, shutdown
from aiogram.utils import executor
import sheet_management as sm
import data_base


data_base.truncate()
sm.empty_row = sm.first_free('Сформированные заказы')

from handlers import client, admin
client.register_handlers_client(dp)
admin.register_handlers_admin(dp)

data_base.create_db()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_shutdown=shutdown)
