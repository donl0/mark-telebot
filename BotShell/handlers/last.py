from ..utils.base_messages import msg_10, msg_11, msg_25, msg_61, msg_60, msg_36, msg_35, msg_34, msg_38, msg_37, \
    msg_33, msg_32, msg_31, msg_30, msg_29, msg_28, msg_27, msg_26, msg_24, msg_23, msg_22, msg_21, msg_20, msg_19, \
    msg_18, msg_17, msg_15, msg_14, msg_13, msg_12, msg_16, msg_39, msg_40, msg_41, msg_42, msg_70, msg_71, msg_72, \
    msg_73, msg_51, msg_54, msg_52, msg_50, msg_53, msg_81, msg_80, msg_8
from ..utils.dbcommands import user_start_update, get_message, user_find_async, type_of_job, user_find_from_jоb_with_id, \
    mark_someone, get_collegaues_from_user, get_employers_from_user, get_teamleaders_from_user, \
    remove_from_manyomany_colleagues, remove_from_manyomany_teamLeader, remove_from_manyomany_employers, \
    increase_to_count, increase_counter_marked_user, mark_yourself, end_or_not_marking_after_yourself, many_mark_me, \
    user_get_many_marked_me, user_get_mark_myself, get_hr_ids, marked_by_someone, user_report_is, \
    get_employers_list_with_rafy_report, get_job_type2, get_job_type3
from ..utils.keyboards import phone_keyboard, hr_keyboard, teamleader_mark_keyboard, \
    specialist_mark_keyboard, manager_mark_keyboard, top_manager_mark_keyboard, mark_keyboard, mark_comment_keyboard, \
    mark_colleagues_keyboard, mark_temleader_keyboard, mark_employer_keyboard, rady_keyboard, HR_start_keyboard, \
    top_manager_Hr_mark_keyboard
from ..utils.states import OrderDataUser, FSMContext, State
from aiogram import Bot, Dispatcher
from aiogram import types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from ..utils.text import telegram_markup
from ..utils.tools import plus_all_from_different_models, get_only_names_from_users


async def Last_handlers(bot: Bot, dp: Dispatcher):
    @dp.message_handler(state='*')
    async def all_mess(message: types.Message, state: FSMContext):
        await state.finish()
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