from ..utils.base_messages import msg_10, msg_11, msg_25, msg_61, msg_60, msg_36, msg_35, msg_34, msg_38, msg_37, \
    msg_33, msg_32, msg_31, msg_30, msg_29, msg_28, msg_27, msg_26, msg_24, msg_23, msg_22, msg_21, msg_20, msg_19, \
    msg_18, msg_17, msg_15, msg_14, msg_13, msg_12, msg_16, msg_39, msg_40, msg_41, msg_42, msg_70, msg_71, msg_72, \
    msg_73, msg_51, msg_54, msg_52, msg_50, msg_53, msg_81, msg_80, msg_92, msg_93
from ..utils.dbcommands import user_start_update, get_message, user_find_async, type_of_job, user_find_from_jоb_with_id, \
    mark_someone, get_collegaues_from_user, get_employers_from_user, get_teamleaders_from_user, \
    remove_from_manyomany_colleagues, remove_from_manyomany_teamLeader, remove_from_manyomany_employers, \
    increase_to_count, increase_counter_marked_user, mark_yourself, end_or_not_marking_after_yourself, many_mark_me, \
    user_get_many_marked_me, user_get_mark_myself, get_hr_ids, marked_by_someone, user_report_is, \
    get_employers_list_with_rafy_report
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


async def HR_handlers(bot: Bot, dp: Dispatcher):
    @dp.message_handler(text=[telegram_markup(await get_message(81, msg_81)), telegram_markup(await get_message(80, msg_80))])
    async def chose_button_HR(message: types.Message, state: FSMContext):
        id_person = message['from']['id']
        dict={'id_tele':id_person}
        mess = message.text
        if mess==telegram_markup(await get_message(80, msg_80)):
            users_diff_models = await get_employers_list_with_rafy_report()
            plused_mass = await plus_all_from_different_models(users_diff_models[0], users_diff_models[1],
                                                               users_diff_models[2])

            last_mass = await get_only_names_from_users(plused_mass)
            if len(last_mass)==0:
                await bot.send_message(id_person, 'Нет сотрудников с готовыми отчётами')
            else:
                for user_name in last_mass:
                    str_file = "excelFiles/" + user_name + ".xlsx"
                    await bot.send_document(id_person, open(str_file, "rb"))

        elif mess==telegram_markup(await get_message(81, msg_81)):
            users_diff_models = await get_employers_list_with_rafy_report()
            plused_mass = await plus_all_from_different_models(users_diff_models[0], users_diff_models[1],
                                                               users_diff_models[2])

            last_mass = await get_only_names_from_users(plused_mass)
            if len(last_mass) == 0:
                await bot.send_message(id_person, telegram_markup(await get_message(92, msg_92)))
            else:
                await bot.send_message(id_person, telegram_markup(await get_message(93, msg_93)), reply_markup=await rady_keyboard())
                await OrderDataUser.waiting_for_name_to_excel.set()

    @dp.message_handler(state=OrderDataUser.waiting_for_name_to_excel)
    async def chose_type_of_marking(message: types.Message, state: FSMContext):
        id_person = message['from']['id']
        dict = {'id_tele': id_person}
        mess = message.text
        print(message)
        str_file = "excelFiles/" + mess + ".xlsx"
        print(str_file)
        await bot.send_document(id_person, open(str_file, "rb"))
        await bot.send_message(id_person, 'выбери', reply_markup=await top_manager_Hr_mark_keyboard())
        await state.finish()