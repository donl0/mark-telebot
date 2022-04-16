from openpyxl import Workbook
from openpyxl import load_workbook

from BotShell.utils.dbcommands import get_message, get_message_no_async
from BotShell.utils.text import telegram_markup
def open_excel():
    wb = load_workbook('excelFiles/original.xlsx')