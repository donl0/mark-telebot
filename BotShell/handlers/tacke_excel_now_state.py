from ..utils.base_messages import msg_10, msg_11, msg_25, msg_61, msg_60, msg_36, msg_35, msg_34, msg_38, msg_37, \
    msg_33, msg_32, msg_31, msg_30, msg_29, msg_28, msg_27, msg_26, msg_24, msg_23, msg_22, msg_21, msg_20, msg_19, \
    msg_18, msg_17, msg_15, msg_14, msg_13, msg_12, msg_16, msg_39, msg_40, msg_41, msg_42, msg_70, msg_71, msg_72, \
    msg_73, msg_51, msg_54, msg_52, msg_50, msg_94, msg_96, msg_97, msg_95, msg_8
from ..utils.dbcommands import user_start_update, get_message, user_find_async, type_of_job, user_find_from_jоb_with_id, \
    mark_someone, get_collegaues_from_user, get_employers_from_user, get_teamleaders_from_user, \
    remove_from_manyomany_colleagues, remove_from_manyomany_teamLeader, remove_from_manyomany_employers, \
    increase_to_count, many_mark_me, all_user_empl, get_job_type2, get_job_type3
from ..utils.keyboards import phone_keyboard, hr_keyboard, teamleader_mark_keyboard, \
    specialist_mark_keyboard, manager_mark_keyboard, top_manager_mark_keyboard, mark_keyboard, mark_comment_keyboard, \
    mark_colleagues_keyboard, mark_temleader_keyboard, mark_employer_keyboard, all_empl_user_for_excel, \
    HR_start_keyboard, top_manager_Hr_mark_keyboard
from ..utils.states import OrderDataUser, FSMContext, State
from aiogram import Bot, Dispatcher
from aiogram import types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from ..utils.text import telegram_markup
from ..utils.tools import get_list_len, get_from_user_marked_by_someone, get_id_from_user, get_phone_num_from_user, \
    get_from_user_counter_to_mark, get_from_user_counter_marked, get_from_user_counter_marked_me, \
    get_only_fio_from_user, get_fio_num_from_user1
from ..utils.work_with_excel import excel_make


async def grab_excel_handlers(bot: Bot, dp: Dispatcher):
    @dp.message_handler(text=[telegram_markup(await get_message(94, msg_94))])
    async def grab_user_excel(message: types.Message, state: FSMContext):
        id_person = message['from']['id']
        dict = {'id_tele': id_person}
        user = await user_find_async(dict)
        user_fio = await get_fio_num_from_user1(user)
        str_file = "excelFiles/" + user_fio + ".xlsx"
        await bot.send_document(id_person, open(str_file, "rb"))

    @dp.message_handler(text=[telegram_markup(await get_message(95, msg_95))])
    async def stat(message: types.Message, state: FSMContext, msg_95=None):
        id_person = message['from']['id']
        dict = {'id_tele': id_person}
        if len(await all_user_empl(dict)) == 0:
            await bot.send_message(id_person, telegram_markup(await get_message(96, msg_96)))
        else:
            await bot.send_message(id_person, telegram_markup(await get_message(97, msg_97)),
                                   reply_markup=await all_empl_user_for_excel(dict))
            # make keybord
            await OrderDataUser.wait_for_empl_name_to_take_excel.set()

    @dp.message_handler(state=OrderDataUser.wait_for_empl_name_to_take_excel)
    async def stat(message: types.Message, state: FSMContext):
        await state.finish()
        user_id = message['from']['id']
        str_file = "excelFiles/" + message.text + ".xlsx"
        await bot.send_document(user_id, open(str_file, "rb"))
        user_id = message['from']['id']
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


