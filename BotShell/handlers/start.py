from django.db.models import F

from ..utils.base_messages import msg_8
from ..utils.dbcommands import user_start_update, get_message, user_find_async, type_of_job, user_find_from_jоb_with_id, \
    increase_to_count, many_mark_me, get_employers_list, user_report_is, get_employers_list_with_rafy_report, \
    get_job_type2, get_job_type3
from ..utils.keyboards import phone_keyboard, hr_keyboard, teamleader_mark_keyboard, \
    specialist_mark_keyboard, manager_mark_keyboard, top_manager_mark_keyboard, HR_start_keyboard, \
    top_manager_Hr_mark_keyboard
from ..utils.states import OrderDataUser, FSMContext, State
from aiogram import Bot, Dispatcher
from aiogram import types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from ..utils.text import telegram_markup
from ..utils.tools import get_list_len, plus_all_from_different_models, get_only_names_from_users


async def start_handlers(bot: Bot, dp: Dispatcher):
    @dp.message_handler(commands=['start'])
    async def start(message: types.Message):

        id_person = message['from']['id']

        dict = {'id_tele': id_person}

        len_user_info = await get_list_len(await user_find_async(dict))

        if len_user_info == 0:

            await bot.send_message(chat_id=message['from']['id'], text=telegram_markup(await get_message(2, 'отправь свойномер для подтверждения доступа к боту.')), reply_markup=await phone_keyboard())
        else:
            user_id = message['from']['id']
            user_name = message['from']['username']
            await bot.send_message(user_id, 'Привет, ' + str(user_name) + '!')
            dict = {'id_tele': user_id}
            job_type = await type_of_job(dict)
            if job_type == 'TopManager':
                hr = await get_job_type3(dict)
                if hr == True:
                    keyboard = await top_manager_Hr_mark_keyboard()
                else:
                    keyboard = await top_manager_mark_keyboard()
            elif job_type == 'Manager':
                keyboard = await manager_mark_keyboard()
            elif job_type == 'Specialist':
                keyboard = await specialist_mark_keyboard()
            await bot.send_message(user_id, telegram_markup(await get_message(8, msg_8)), reply_markup=keyboard)


    @dp.message_handler(content_types=['contact'])
    async def contact(message):
        if message.contact is not None:
            hide_keyboard= types.ReplyKeyboardRemove()

            phonenumber= str(message.contact.phone_number)
            if phonenumber[0]!='+':
                phonenumber='+'+phonenumber
            user_id = str(message.contact.user_id)
            user_name = message['from']['username']
            if user_name==None:
                user_name='telegram name none'
            await user_start_update(phonenumber, user_id, user_name)
            #user_info=await user_find_async(dict)
            #print(user_info)
            await bot.send_message(user_id, 'Привет, '+str(user_name)+'!', reply_markup=hide_keyboard)
            dict = {'id_tele': user_id}
            job_type = await type_of_job(dict)
            if job_type == 'TopManager':
                hr = await get_job_type3(dict)
                if hr == True:
                    keyboard = await top_manager_Hr_mark_keyboard()
                else:
                    keyboard = await top_manager_mark_keyboard()
            elif job_type == 'Manager':
                keyboard = await manager_mark_keyboard()
            elif job_type == 'Specialist':
                keyboard = await specialist_mark_keyboard()
            await bot.send_message(user_id, telegram_markup(await get_message(8, msg_8)), reply_markup=keyboard)

