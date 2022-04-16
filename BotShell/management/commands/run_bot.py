import asyncio

from ...handlers.Document import document_handlers
from ...handlers.HR import HR_handlers
from ...handlers.back import Back_handlers
from ...handlers.last import Last_handlers
from ...handlers.marker import marking_handlers
from ...handlers.statistic import statistic_handlers
from ...handlers.tacke_excel_now_state import grab_excel_handlers
from ...midlware.big_brother import BigBrother

from django.core.management.base import BaseCommand

from aiogram import Bot, Dispatcher

from django.conf import settings


from ...handlers.start import start_handlers

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from ...utils.loop_call import scheduler


async def bot_settings(loop=None):

    bot = Bot(token=settings.TG_TOKEN, parse_mode='HTML', loop=loop)

    dp = Dispatcher(bot, storage=MemoryStorage())

    await document_handlers(bot,dp)
    await grab_excel_handlers(bot, dp)
    await start_handlers(bot, dp)
    await Back_handlers(bot, dp)
    await HR_handlers(bot, dp)
    await statistic_handlers(bot, dp)
    await marking_handlers(bot, dp)
    await Last_handlers(bot, dp)
    return bot, dp


async def polling():
    bot, dp = await bot_settings()
    asyncio.create_task(scheduler(bot, dp))
    dp.middleware.setup(BigBrother())
    try:
        await dp.start_polling()
    finally:
        await bot.close()


class Command(BaseCommand):
    def handle(self, *args, **options):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        while True:
            asyncio.run(polling())
