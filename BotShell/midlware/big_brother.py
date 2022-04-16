from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware

from BotShell.utils.dbcommands import user_find_async
from BotShell.utils.states import OrderDataUser
from BotShell.utils.tools import get_list_len


class BigBrother(BaseMiddleware):
    async def on_pre_process_update(self, update: types.Update, date: dict, state='*'):
        #print(update)
        pass

