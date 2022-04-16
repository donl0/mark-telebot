import types

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from .base_messages import msg_50, msg_51, msg_52, msg_53, msg_60, msg_54, msg_80, msg_81, msg_90, msg_94, msg_95
from .tools import get_only_names2, plus_all_from_different_models, get_only_names_from_users
from ..utils.text import telegram_markup
from ..utils.dbcommands import get_message, get_collegaues_from_user, get_teamleaders_from_user, \
    get_employers_from_user, get_employers_list_with_rafy_report, all_user_empl

comm_keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
item_add_c = InlineKeyboardButton(text='💬 Leave a comment')
item_back_c = InlineKeyboardButton(text='⬅  Back')
comm_keyboard.add(item_back_c, item_add_c)

#async def statistic_top_manager_keyboard():


async def HR_start_keyboard():
    keyboard = ReplyKeyboardMarkup(row_width=1)
    mark_for_one_button = KeyboardButton(text=telegram_markup(await get_message(81, msg_81)))
    mark_for_all_button = KeyboardButton(text=telegram_markup(await get_message(80, msg_80)))
    keyboard.add(mark_for_one_button, mark_for_all_button)
    return keyboard



async def rady_keyboard():
    keyboard = ReplyKeyboardMarkup(row_width=2)

    users_diff_models = await get_employers_list_with_rafy_report()
    plused_mass = await plus_all_from_different_models(users_diff_models[0], users_diff_models[1], users_diff_models[2])

    last_mass = await get_only_names_from_users(plused_mass)

    for rady in last_mass:

        teamleder_button = KeyboardButton(text=rady)
        keyboard.add(teamleder_button)
    return keyboard


async def mark_temleader_keyboard(dict):
    keyboard = ReplyKeyboardMarkup(row_width=1)
    teamleaders_fio = await get_teamleaders_from_user(dict)
    print(teamleaders_fio)
    back_button = KeyboardButton(text=telegram_markup(await get_message(90, msg_90)))
    keyboard.add(back_button)
    for teamleder in teamleaders_fio:

        teamleder_button = KeyboardButton(text=teamleder)
        keyboard.add(teamleder_button)
    return keyboard


async def mark_employer_keyboard(dict):
    keyboard = ReplyKeyboardMarkup(row_width=1)
    employer_fio = await get_employers_from_user(dict)
    back_button = KeyboardButton(text=telegram_markup(await get_message(90, msg_90)))
    keyboard.add(back_button)
    for employer in employer_fio:

        employer_button = KeyboardButton(text=employer)
        keyboard.add(employer_button)
    return keyboard


async def mark_colleagues_keyboard(dict):
    keyboard = ReplyKeyboardMarkup(row_width=1)
    colleagues_fio = await get_collegaues_from_user(dict)
    back_button = KeyboardButton(text=telegram_markup(await get_message(90, msg_90)))
    keyboard.add(back_button)
    for colleague in colleagues_fio:

        colleague_button = KeyboardButton(text=colleague)
        keyboard.add(colleague_button)
    return keyboard


async def mark_comment_keyboard():
    keyboard = ReplyKeyboardMarkup(row_width=1)
    mark_1_button = KeyboardButton(text=telegram_markup(await get_message(60, msg_60)))
    keyboard.add(mark_1_button)
    return keyboard

async def all_empl_user_for_excel(dict):
    keyboard = ReplyKeyboardMarkup(row_width=1)
    all_empl = await all_user_empl(dict)
    all_empl = all_empl.split(';')
   # print(teamleaders_fio)
   # back_button = KeyboardButton(text=telegram_markup(await get_message(90, msg_90)))
    #keyboard.add(back_button)
    for empl in all_empl:
        empl_button = KeyboardButton(text=empl)
        keyboard.add(empl_button)
    return keyboard


async def mark_keyboard():
    keyboard = ReplyKeyboardMarkup(row_width=1)
    mark_1_button = KeyboardButton(text='1 - '+telegram_markup(await get_message(50, msg_50)))
    mark_2_button = KeyboardButton(text='2 - '+telegram_markup(await get_message(51, msg_51)))
    mark_3_button = KeyboardButton(text='3 - '+telegram_markup(await get_message(52, msg_52)))
    mark_4_button1 = KeyboardButton(text='4 - '+telegram_markup(await get_message(53, msg_53)))
    mark_5_button = KeyboardButton(text=telegram_markup(await get_message(55, msg_54)))
    keyboard.add(mark_1_button, mark_2_button, mark_3_button, mark_4_button1, mark_5_button)
    return keyboard


async def manager_mark_keyboard():
    employer_keyboard = ReplyKeyboardMarkup(row_width=1)
    mark_yourself_button = KeyboardButton(text=telegram_markup(await get_message(3, 'Оценка себя (360)')))
    mark_collegue_button = KeyboardButton(text=telegram_markup(await get_message(4, 'Оценка коллег')))
    mark_teamlead_button = KeyboardButton(text=telegram_markup(await get_message(5, 'Оцени руководителя')))
    mark_teamlead_button1 = KeyboardButton(text=telegram_markup(await get_message(6, 'оценка подчинённых')))
    mark_statistic_button = KeyboardButton(text=telegram_markup(await get_message(7, '📄Статистика')))
    check_file_button = KeyboardButton(text=telegram_markup(await get_message(94, msg_94)))
    all_empl_excel = KeyboardButton(text=telegram_markup(await get_message(95, msg_95)))


    employer_keyboard.add(mark_yourself_button, mark_collegue_button, mark_teamlead_button, mark_teamlead_button1,mark_statistic_button, all_empl_excel)
    return employer_keyboard


async def top_manager_mark_keyboard():
    employer_keyboard = ReplyKeyboardMarkup(row_width=1)
    mark_yourself_button = KeyboardButton(text=telegram_markup(await get_message(3, 'Оценка себя (360)')))
    mark_collegue_button = KeyboardButton(text=telegram_markup(await get_message(4, 'Оценка коллег')))
    mark_teamlead_button = KeyboardButton(text=telegram_markup(await get_message(5, 'Оцени руководителя')))
    mark_teamlead_button1 = KeyboardButton(text=telegram_markup(await get_message(6, 'оценка подчинённых')))
    mark_statistic_button = KeyboardButton(text=telegram_markup(await get_message(7, '📄Статистика')))
    check_file_button = KeyboardButton(text=telegram_markup(await get_message(94, msg_94)))
    all_empl_excel = KeyboardButton(text=telegram_markup(await get_message(95, msg_95)))

    employer_keyboard.add(mark_yourself_button, mark_collegue_button, mark_teamlead_button, mark_teamlead_button1, mark_statistic_button, all_empl_excel)
    return employer_keyboard


async def top_manager_Hr_mark_keyboard():
    employer_keyboard = ReplyKeyboardMarkup(row_width=1)
    mark_yourself_button = KeyboardButton(text=telegram_markup(await get_message(3, 'Оценка себя (360)')))
    mark_collegue_button = KeyboardButton(text=telegram_markup(await get_message(4, 'Оценка коллег')))
    mark_teamlead_button = KeyboardButton(text=telegram_markup(await get_message(5, 'Оцени руководителя')))
    mark_teamlead_button1 = KeyboardButton(text=telegram_markup(await get_message(6, 'оценка подчинённых')))
    mark_statistic_button = KeyboardButton(text=telegram_markup(await get_message(7, '📄Статистика')))
    mark_for_one_button = KeyboardButton(text=telegram_markup(await get_message(81, msg_81)))
    mark_for_all_button = KeyboardButton(text=telegram_markup(await get_message(80, msg_80)))
    check_file_button = KeyboardButton(text=telegram_markup(await get_message(94, msg_94)))
    all_empl_excel = KeyboardButton(text=telegram_markup(await get_message(95, msg_95)))

    employer_keyboard.add(mark_yourself_button, mark_collegue_button, mark_teamlead_button, mark_teamlead_button1, mark_statistic_button, all_empl_excel, mark_for_one_button, mark_for_all_button)
    return employer_keyboard


async def teamleader_mark_keyboard():
    teamleader_keyboard = ReplyKeyboardMarkup(row_width=1)
    mark_yourself_button = KeyboardButton(text=telegram_markup(await get_message(3, 'Оценка себя (360)')))
    mark_collegue_button = KeyboardButton(text=telegram_markup(await get_message(4, 'Оценка коллег')))
    mark_teamlead_button = KeyboardButton(text=telegram_markup(await get_message(6, 'оценка подчинённых')))
    check_file_button = KeyboardButton(text=telegram_markup(await get_message(94, msg_94)))

    teamleader_keyboard.add(mark_yourself_button, mark_collegue_button, mark_teamlead_button)
    return teamleader_keyboard


async def specialist_mark_keyboard():
    specialist_keyboard = ReplyKeyboardMarkup(row_width=1)
    mark_yourself_button = KeyboardButton(text=telegram_markup(await get_message(3, 'Оценка себя (360)')))
    mark_collegue_button = KeyboardButton(text=telegram_markup(await get_message(4, 'Оценка коллег')))
    mark_teamlead_button = KeyboardButton(text=telegram_markup(await get_message(5, 'Оцени руководителя')))
    mark_statistic_button = KeyboardButton(text=telegram_markup(await get_message(7, '📄Статистика')))
    check_file_button = KeyboardButton(text=telegram_markup(await get_message(94, msg_94)))

    specialist_keyboard.add(mark_yourself_button, mark_collegue_button, mark_teamlead_button, mark_statistic_button)
    return specialist_keyboard

async def hr_keyboard():
    hr_keyboard = ReplyKeyboardMarkup(row_width=1)
    mark_yourself_button = KeyboardButton(text=telegram_markup(await get_message(3, 'Оценка себя (360)')))
    mark_collegue_button = KeyboardButton(text=telegram_markup(await get_message(6, 'оценка подчинённых')))
    mark_teamlead_button = KeyboardButton(text=telegram_markup(await get_message(7 ,'📄Статистика')))
    check_file_button = KeyboardButton(text=telegram_markup(await get_message(94, msg_94)))

    hr_keyboard.add(mark_yourself_button, mark_collegue_button, mark_teamlead_button)
    return hr_keyboard


async def phone_keyboard():
    phone_keyboard1 = ReplyKeyboardMarkup(row_width=1)
    phone_button = KeyboardButton(text=telegram_markup(await get_message(1, 'Отправить номер телефона')), request_contact=True)
    phone_keyboard1.add(phone_button)
    return phone_keyboard1


async def main_m_keyboard():
    main_m_keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    item_back1 = InlineKeyboardButton(text=telegram_markup(await get_message(44)))
    item_main_m1 = InlineKeyboardButton(text=telegram_markup(await get_message(40)))
    item_watch_n1 = InlineKeyboardButton(text=telegram_markup(await get_message(41)))
    item_u_Comments = InlineKeyboardButton(text=telegram_markup(await get_message(42)))
    item_u_fav = InlineKeyboardButton(text=telegram_markup(await get_message(43)))
    main_m_keyboard.add(item_back1, item_main_m1).add(item_watch_n1).add(item_u_Comments, item_u_fav)
    return main_m_keyboard
