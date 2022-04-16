from ..utils.base_messages import msg_10, msg_11, msg_25, msg_61, msg_60, msg_36, msg_35, msg_34, msg_38, msg_37, \
    msg_33, msg_32, msg_31, msg_30, msg_29, msg_28, msg_27, msg_26, msg_24, msg_23, msg_22, msg_21, msg_20, msg_19, \
    msg_18, msg_17, msg_15, msg_14, msg_13, msg_12, msg_16, msg_39, msg_40, msg_41, msg_42, msg_70, msg_71, msg_72, \
    msg_73, msg_51, msg_54, msg_52, msg_50, msg_95, msg_97
from ..utils.dbcommands import user_start_update, get_message, user_find_async, type_of_job, user_find_from_jоb_with_id, \
    mark_someone, get_collegaues_from_user, get_employers_from_user, get_teamleaders_from_user, \
    remove_from_manyomany_colleagues, remove_from_manyomany_teamLeader, remove_from_manyomany_employers, \
    increase_to_count, many_mark_me, all_user_empl
from ..utils.keyboards import phone_keyboard, hr_keyboard, teamleader_mark_keyboard, \
    specialist_mark_keyboard, manager_mark_keyboard, top_manager_mark_keyboard, mark_keyboard, mark_comment_keyboard, \
    mark_colleagues_keyboard, mark_temleader_keyboard, mark_employer_keyboard, all_empl_user_for_excel
from ..utils.states import OrderDataUser, FSMContext, State
from aiogram import Bot, Dispatcher
from aiogram import types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from ..utils.text import telegram_markup
from ..utils.tools import get_list_len, get_from_user_marked_by_someone, get_id_from_user, get_phone_num_from_user, \
    get_from_user_counter_to_mark, get_from_user_counter_marked, get_from_user_counter_marked_me
from ..utils.work_with_excel import excel_make


async def statistic_handlers(bot: Bot, dp: Dispatcher):
    @dp.message_handler(text=[telegram_markup(await get_message(7, '📄Статистика'))])
    async def stat(message: types.Message, state: FSMContext):
        id_person = message['from']['id']
        dict = {'id_tele': id_person}
        job_type = await type_of_job(dict)
        user = await user_find_from_jоb_with_id(dict)
        counter_to_mark = await get_from_user_counter_to_mark(user)
        counter_marked = await get_from_user_counter_marked(user)
        text = '-Сколько надо оценить: ' + str(counter_to_mark) + '\n-Сколько уже оценил: ' + str(counter_marked)+'\n'
        if job_type == 'TopManager':
            text += '-Сколько должно оценить меня: ' + str(await many_mark_me(dict))+'\n-Сколько меня оценило: '+str(await get_from_user_counter_marked_me(user))
            await bot.send_message(id_person, text)
        elif job_type == 'Manager':
            text += '-Сколько должно оценить меня: ' + str(await many_mark_me(dict))+'\n-Сколько меня оценило: '+str(await get_from_user_counter_marked_me(user))
            await bot.send_message(id_person, text)
        elif job_type == 'Specialist':
            await bot.send_message(id_person, text)

        #await bot.send_message(id_person, 'Выбери любой из пунктов меню 👇', reply_markup=keyboard)

