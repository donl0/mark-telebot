from ..utils.base_messages import msg_10, msg_11, msg_25, msg_61, msg_60, msg_36, msg_35, msg_34, msg_38, msg_37, \
    msg_33, msg_32, msg_31, msg_30, msg_29, msg_28, msg_27, msg_26, msg_24, msg_23, msg_22, msg_21, msg_20, msg_19, \
    msg_18, msg_17, msg_15, msg_14, msg_13, msg_12, msg_16, msg_39, msg_40, msg_41, msg_42, msg_70, msg_71, msg_72, \
    msg_73, msg_51, msg_54, msg_52, msg_50, msg_53, msg_8, msg_65, msg_62, msg_63, msg_64, msg_91
from ..utils.dbcommands import user_start_update, get_message, user_find_async, type_of_job, user_find_from_jоb_with_id, \
    mark_someone, get_collegaues_from_user, get_employers_from_user, get_teamleaders_from_user, \
    remove_from_manyomany_colleagues, remove_from_manyomany_teamLeader, remove_from_manyomany_employers, \
    increase_to_count, increase_counter_marked_user, mark_yourself, end_or_not_marking_after_yourself, many_mark_me, \
    user_get_many_marked_me, user_get_mark_myself, get_hr_ids, marked_by_someone, user_report_is, get_job_type2, \
    update_start_mark, user_find, user_find_fio, get_massage_for_question, get_job_type3
from ..utils.keyboards import phone_keyboard, hr_keyboard, teamleader_mark_keyboard, \
    specialist_mark_keyboard, manager_mark_keyboard, top_manager_mark_keyboard, mark_keyboard, mark_comment_keyboard, \
    mark_colleagues_keyboard, mark_temleader_keyboard, mark_employer_keyboard, HR_start_keyboard, \
    top_manager_Hr_mark_keyboard
from ..utils.states import OrderDataUser, FSMContext, State
from aiogram import Bot, Dispatcher
from aiogram import types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from ..utils.text import telegram_markup
from ..utils.tools import get_list_len, get_from_user_marked_by_someone, get_id_from_user, get_phone_num_from_user, \
    get_only_fio_from_user
from ..utils.work_with_excel import excel_make


async def marking_handlers(bot: Bot, dp: Dispatcher):
    @dp.message_handler(text=[telegram_markup(await get_message(3, 'Оценка себя (360)')), telegram_markup(await get_message(4, 'Оценка коллег')),telegram_markup(await get_message(5, 'Оцени руководителя')), telegram_markup(await get_message(6, 'оценка подчинённых'))])
    async def chose_type_of_marking(message: types.Message, state: FSMContext):
        id_person = message['from']['id']
        dict={'id_tele':id_person}

        if message.text == telegram_markup(await get_message(3, 'Оценка себя (360)')):
            await state.update_data(mark_type=message.text)
            await state.update_data(job_type=await type_of_job(dict))
            user_data = await state.get_data()

            id_to_send = await get_massage_for_question(user_data['job_type'], 10)
            await bot.send_message(id_person, telegram_markup(await get_message(id_to_send, msg_10)))
            id_to_send = await get_massage_for_question(user_data['job_type'], 11)
            await bot.send_message(id_person, telegram_markup(await get_message(id_to_send, msg_11)), reply_markup=await mark_keyboard())
            await OrderDataUser.start_marking_a.set()
        elif message.text == telegram_markup(await get_message(4, 'Оценка коллег')):
            await state.update_data(mark_type=message.text)
            colleagues = await get_collegaues_from_user(dict)
            len_you_collegues = await get_list_len(colleagues)
            if len_you_collegues==0:
                await bot.send_message(id_person, telegram_markup(await get_message(71, msg_71)))
            else:
                await bot.send_message(message['from']['id'], telegram_markup(await get_message(70, msg_70)), reply_markup=await mark_colleagues_keyboard(dict))

                await OrderDataUser.get_name.set()
        elif message.text == telegram_markup(await get_message(5, 'Оцени руководителя')):
            await state.update_data(mark_type=message.text)
            teamleaders = await get_teamleaders_from_user(dict)
            len_you_teamleaders = await get_list_len(teamleaders)
            if len_you_teamleaders==0:
                await bot.send_message(id_person, telegram_markup(await get_message(72, msg_72)))
            else:
                await bot.send_message(message['from']['id'], telegram_markup(await get_message(70, msg_70)), reply_markup=await mark_temleader_keyboard(dict))

                await OrderDataUser.get_name.set()
        elif message.text == telegram_markup(await get_message(6, 'оценка подчинённых')):
            await state.update_data(mark_type=message.text)
            employers = await get_employers_from_user(dict)
            len_you_employers = await get_list_len(employers)
            if len_you_employers==0:
                await bot.send_message(id_person, telegram_markup(await get_message(73, msg_73)))
            else:
                await bot.send_message(message['from']['id'], telegram_markup(await get_message(73, msg_73)), reply_markup=await mark_employer_keyboard(dict))

                await OrderDataUser.get_name.set()

    @dp.message_handler(state=OrderDataUser.get_name)
    async def start_mark(message: types.Message, state: FSMContext):
        mess = message.text
        id_person = message['from']['id']
        dict = {'fio':mess}
        await state.update_data(job_type=await type_of_job(dict))
        user_data = await state.get_data()
        id_to_send = await get_massage_for_question(user_data['job_type'], 10)
        base_mess = 'msg_'+str(id_to_send)
        await bot.send_message(id_person, telegram_markup(await get_message(id_to_send, msg_10)))
        id_to_send = await get_massage_for_question(user_data['job_type'], 11)
        base_mess = 'msg_' + str(id_to_send)
        await bot.send_message(id_person, telegram_markup(await get_message(id_to_send, msg_11)),
                               reply_markup=await mark_keyboard())
        await OrderDataUser.start_marking_a.set()
        await state.update_data(your_marking_user=message.text)

    #text=['1 - '+telegram_markup(await get_message(50, msg_50)),'2 - '+telegram_markup(await get_message(51, msg_51)),'3 - '+telegram_markup(await get_message(52, msg_52)),'4 - '+telegram_markup(await get_message(53, msg_53)),telegram_markup(await get_message(54, msg_54))]
    @dp.message_handler(text=['1 - '+telegram_markup(await get_message(50, msg_50)),'2 - '+telegram_markup(await get_message(51, msg_51)),'3 - '+telegram_markup(await get_message(52, msg_52)),'4 - '+telegram_markup(await get_message(53, msg_53)),telegram_markup(await get_message(54, msg_54))], state = OrderDataUser.start_marking_a)
    async def start_mark(message: types.Message, state: FSMContext):
        user_data = await state.get_data()
        mess = message.text
        if mess == telegram_markup(await get_message(54, msg_54)):
            mess=None
            await state.update_data(answers=[mess])
        else:
            await state.update_data(answers=[mess[0]])
        await state.update_data(comments=[])
        await state.update_data(answera1=mess)
        id_to_send = await get_massage_for_question(user_data['job_type'], 12)
        base_mess = 'msg_' + str(id_to_send)
        await bot.send_message(message['from']['id'], telegram_markup(await get_message(id_to_send, msg_12)))
        await OrderDataUser.mark_a1.set()
        user_data = await state.get_data()

    @dp.message_handler(text=['1 - '+telegram_markup(await get_message(50, msg_50)),'2 - '+telegram_markup(await get_message(51, msg_51)),'3 - '+telegram_markup(await get_message(52, msg_52)),'4 - '+telegram_markup(await get_message(53, msg_53)),telegram_markup(await get_message(54, msg_54))],state=OrderDataUser.mark_a1)
    async def start_mark(message: types.Message, state: FSMContext):
        user_data = await state.get_data()
        mess = message.text

        answers = user_data['answers']
        if mess == telegram_markup(await get_message(54, msg_54)):
            mess=None
            answers.append(mess)
        else:
            answers.append(mess[0])
        print(answers)
        await state.update_data(answers=answers)
        await state.update_data(answera2=mess)
        id_to_send = await get_massage_for_question(user_data['job_type'], 13)
        base_mess = 'msg_' + str(id_to_send)

        await bot.send_message(message['from']['id'], telegram_markup(await get_message(id_to_send, msg_13)))
        await OrderDataUser.mark_a2.set()
        user_data = await state.get_data()

    @dp.message_handler(text=['1 - '+telegram_markup(await get_message(50, msg_50)),'2 - '+telegram_markup(await get_message(51, msg_51)),'3 - '+telegram_markup(await get_message(52, msg_52)),'4 - '+telegram_markup(await get_message(53, msg_53)),telegram_markup(await get_message(54, msg_54))],state=OrderDataUser.mark_a2)
    async def start_mark(message: types.Message, state: FSMContext):
        user_data = await state.get_data()
        mess = message.text

        answers = user_data['answers']
        if mess == telegram_markup(await get_message(54, msg_54)):
            mess = None
            answers.append(mess)
        else:
            answers.append(mess[0])
        await state.update_data(answers=answers)
        await state.update_data(answera3=mess)
        id_to_send = await get_massage_for_question(user_data['job_type'], 14)
        base_mess = 'msg_' + str(id_to_send)
        await bot.send_message(message['from']['id'], telegram_markup(await get_message(id_to_send, msg_14)))
        await OrderDataUser.mark_a3.set()
        user_data = await state.get_data()
        print(user_data['answers'])

    @dp.message_handler(text=['1 - '+telegram_markup(await get_message(50, msg_50)),'2 - '+telegram_markup(await get_message(51, msg_51)),'3 - '+telegram_markup(await get_message(52, msg_52)),'4 - '+telegram_markup(await get_message(53, msg_53)),telegram_markup(await get_message(54, msg_54))],state=OrderDataUser.mark_a3)
    async def start_mark(message: types.Message, state: FSMContext):
        user_data = await state.get_data()
        mess = message.text

        answers = user_data['answers']
        if mess == telegram_markup(await get_message(54, msg_54)):
            mess = None
            answers.append(mess)
        else:
            answers.append(mess[0])
        await state.update_data(answers=answers)
        await state.update_data(answera4=mess)
        id_to_send = await get_massage_for_question(user_data['job_type'], 15)

        await bot.send_message(message['from']['id'], telegram_markup(await get_message(id_to_send, msg_15)))
        await OrderDataUser.mark_a4.set()
        user_data = await state.get_data()
        print(user_data['answers'])

    @dp.message_handler(text=['1 - '+telegram_markup(await get_message(50, msg_50)),'2 - '+telegram_markup(await get_message(51, msg_51)),'3 - '+telegram_markup(await get_message(52, msg_52)),'4 - '+telegram_markup(await get_message(53, msg_53)),telegram_markup(await get_message(54, msg_54))],state=OrderDataUser.mark_a4)
    async def start_mark(message: types.Message, state: FSMContext):
        user_data = await state.get_data()
        mess = message.text

        answers = user_data['answers']
        if mess == telegram_markup(await get_message(54, msg_54)):
            mess = None
            answers.append(mess)
        else:
            answers.append(mess[0])
        await state.update_data(answers=answers)
        await state.update_data(answera5=mess)

        id_to_send = await get_massage_for_question(user_data['job_type'], 16)
        await bot.send_message(message['from']['id'], telegram_markup(await get_message(id_to_send, msg_16)))
        await OrderDataUser.mark_a5.set()

    @dp.message_handler(text=['1 - '+telegram_markup(await get_message(50, msg_50)),'2 - '+telegram_markup(await get_message(51, msg_51)),'3 - '+telegram_markup(await get_message(52, msg_52)),'4 - '+telegram_markup(await get_message(53, msg_53)),telegram_markup(await get_message(54, msg_54))],state=OrderDataUser.mark_a5)
    async def start_mark(message: types.Message, state: FSMContext):
        user_data = await state.get_data()
        mess = message.text

        answers = user_data['answers']
        if mess == telegram_markup(await get_message(54, msg_54)):
            mess = None
            answers.append(mess)
        else:
            answers.append(mess[0])
        await state.update_data(answers=answers)
        await state.update_data(answera6=mess)

        await bot.send_message(message['from']['id'], telegram_markup(await get_message(61, msg_61)), reply_markup=await mark_comment_keyboard())
        await OrderDataUser.mark_a_comment.set()

    @dp.message_handler(state=OrderDataUser.mark_a_comment)
    async def start_mark(message: types.Message, state: FSMContext):
        user_data = await state.get_data()

        mess = message.text
        if mess == telegram_markup(await get_message(60, msg_60)):
            mess = ''
        else:
            mess = '-' + mess + '\n\n'

        comments = user_data['comments']
        comments.append(mess)
        await state.update_data(comments=comments)

        await state.update_data(comm_a=mess)
        id_to_send = await get_massage_for_question(user_data['job_type'], 17)

        await bot.send_message(message['from']['id'], telegram_markup(await get_message(id_to_send, msg_17)))

        id_to_send = await get_massage_for_question(user_data['job_type'], 18)
        await bot.send_message(message['from']['id'], telegram_markup(await get_message(id_to_send, msg_18)), reply_markup=await mark_keyboard())
        await OrderDataUser.mark_b1.set()


    @dp.message_handler(text=['1 - '+telegram_markup(await get_message(50, msg_50)),'2 - '+telegram_markup(await get_message(51, msg_51)),'3 - '+telegram_markup(await get_message(52, msg_52)),'4 - '+telegram_markup(await get_message(53, msg_53)),telegram_markup(await get_message(54, msg_54))],state=OrderDataUser.mark_b1)
    async def start_mark(message: types.Message, state: FSMContext):
        user_data = await state.get_data()
        mess = message.text

        answers = user_data['answers']
        if mess == telegram_markup(await get_message(54, msg_54)):
            mess = None
            answers.append(mess)
        else:
            answers.append(mess[0])
        await state.update_data(answers=answers)
        await state.update_data(answerb1=mess)
        id_to_send = await get_massage_for_question(user_data['job_type'], 19)
        await bot.send_message(message['from']['id'], telegram_markup(await get_message(id_to_send, msg_19)))
        await OrderDataUser.mark_b2.set()


    @dp.message_handler(text=['1 - '+telegram_markup(await get_message(50, msg_50)),'2 - '+telegram_markup(await get_message(51, msg_51)),'3 - '+telegram_markup(await get_message(52, msg_52)),'4 - '+telegram_markup(await get_message(53, msg_53)),telegram_markup(await get_message(54, msg_54))],state=OrderDataUser.mark_b2)
    async def start_mark(message: types.Message, state: FSMContext):
        user_data = await state.get_data()
        mess = message.text

        answers = user_data['answers']
        if mess == telegram_markup(await get_message(54, msg_54)):
            mess = None
            answers.append(mess)
        else:
            answers.append(mess[0])
        await state.update_data(answers=answers)
        await state.update_data(answerb2=mess)
        id_to_send = await get_massage_for_question(user_data['job_type'], 20)

        await bot.send_message(message['from']['id'], telegram_markup(await get_message(id_to_send, msg_20)))
        await OrderDataUser.mark_b3.set()

    @dp.message_handler(text=['1 - '+telegram_markup(await get_message(50, msg_50)),'2 - '+telegram_markup(await get_message(51, msg_51)),'3 - '+telegram_markup(await get_message(52, msg_52)),'4 - '+telegram_markup(await get_message(53, msg_53)),telegram_markup(await get_message(54, msg_54))],state=OrderDataUser.mark_b3)
    async def start_mark(message: types.Message, state: FSMContext):
        user_data = await state.get_data()
        mess = message.text

        answers = user_data['answers']
        if mess == telegram_markup(await get_message(54, msg_54)):
            mess = None
            answers.append(mess)
        else:
            answers.append(mess[0])
        await state.update_data(answers=answers)
        await state.update_data(answerb3=mess)

        id_to_send = await get_massage_for_question(user_data['job_type'], 21)
        await bot.send_message(message['from']['id'], telegram_markup(await get_message(id_to_send, msg_21)))
        await OrderDataUser.mark_b4.set()

    @dp.message_handler(text=['1 - '+telegram_markup(await get_message(50, msg_50)),'2 - '+telegram_markup(await get_message(51, msg_51)),'3 - '+telegram_markup(await get_message(52, msg_52)),'4 - '+telegram_markup(await get_message(53, msg_53)),telegram_markup(await get_message(54, msg_54))],state=OrderDataUser.mark_b4)
    async def start_mark(message: types.Message, state: FSMContext):
        user_data = await state.get_data()
        mess = message.text

        answers = user_data['answers']
        if mess == telegram_markup(await get_message(54, msg_54)):
            mess = None
            answers.append(mess)
        else:
            answers.append(mess[0])
        await state.update_data(answers=answers)
        await state.update_data(answerb4=mess)

        id_to_send = await get_massage_for_question(user_data['job_type'], 22)
        await bot.send_message(message['from']['id'], telegram_markup(await get_message(id_to_send, msg_22)))
        await OrderDataUser.mark_b5.set()

    @dp.message_handler(text=['1 - '+telegram_markup(await get_message(50, msg_50)),'2 - '+telegram_markup(await get_message(51, msg_51)),'3 - '+telegram_markup(await get_message(52, msg_52)),'4 - '+telegram_markup(await get_message(53, msg_53)),telegram_markup(await get_message(54, msg_54))],state=OrderDataUser.mark_b5)
    async def start_mark(message: types.Message, state: FSMContext):
        user_data = await state.get_data()
        mess = message.text

        answers = user_data['answers']
        if mess == telegram_markup(await get_message(54, msg_54)):
            mess = None
            answers.append(mess)
        else:
            answers.append(mess[0])
        await state.update_data(answers=answers)
        await state.update_data(answerb5=mess)
        await bot.send_message(message['from']['id'], telegram_markup(await get_message(62, msg_62)), reply_markup=await mark_comment_keyboard())
        await OrderDataUser.mark_b_comment.set()########

    @dp.message_handler(state=OrderDataUser.mark_b_comment)
    async def start_mark(message: types.Message, state: FSMContext):
        user_data = await state.get_data()

        mess = message.text
        if mess == telegram_markup(await get_message(60, msg_60)):
            mess = ''
        else:
            mess = '-' + mess + '\n\n'

        comments = user_data['comments']
        comments.append(mess)
        await state.update_data(comments=comments)

        await state.update_data(comm_b=mess)

        id_to_send = await get_massage_for_question(user_data['job_type'], 23)
        await bot.send_message(message['from']['id'], telegram_markup(await get_message(id_to_send, msg_23)))

        id_to_send = await get_massage_for_question(user_data['job_type'], 24)
        await bot.send_message(message['from']['id'], telegram_markup(await get_message(id_to_send, msg_24)), reply_markup=await mark_keyboard())
        await OrderDataUser.mark_c1.set()#123



    @dp.message_handler(text=['1 - '+telegram_markup(await get_message(50, msg_50)),'2 - '+telegram_markup(await get_message(51, msg_51)),'3 - '+telegram_markup(await get_message(52, msg_52)),'4 - '+telegram_markup(await get_message(53, msg_53)),telegram_markup(await get_message(54, msg_54))],state=OrderDataUser.mark_c1)
    async def start_mark(message: types.Message, state: FSMContext):
        user_data = await state.get_data()
        mess = message.text

        answers = user_data['answers']
        if mess == telegram_markup(await get_message(54, msg_54)):
            mess = None
            answers.append(mess)
        else:
            answers.append(mess[0])
        await state.update_data(answers=answers)

        await state.update_data(answerc1=mess)

        id_to_send = await get_massage_for_question(user_data['job_type'], 25)
        await bot.send_message(message['from']['id'], telegram_markup(await get_message(id_to_send, msg_25)))
        await OrderDataUser.mark_c2.set()

    @dp.message_handler(text=['1 - '+telegram_markup(await get_message(50, msg_50)),'2 - '+telegram_markup(await get_message(51, msg_51)),'3 - '+telegram_markup(await get_message(52, msg_52)),'4 - '+telegram_markup(await get_message(53, msg_53)),telegram_markup(await get_message(54, msg_54))],state=OrderDataUser.mark_c2)
    async def start_mark(message: types.Message, state: FSMContext):
        user_data = await state.get_data()
        mess = message.text

        answers = user_data['answers']
        if mess == telegram_markup(await get_message(54, msg_54)):
            mess = None
            answers.append(mess)
        else:
            answers.append(mess[0])
        await state.update_data(answers=answers)

        await state.update_data(answerc2=mess)
        id_to_send = await get_massage_for_question(user_data['job_type'], 26)
        await bot.send_message(message['from']['id'], telegram_markup(await get_message(id_to_send, msg_26)))
        await OrderDataUser.mark_c3.set()

    @dp.message_handler(text=['1 - '+telegram_markup(await get_message(50, msg_50)),'2 - '+telegram_markup(await get_message(51, msg_51)),'3 - '+telegram_markup(await get_message(52, msg_52)),'4 - '+telegram_markup(await get_message(53, msg_53)),telegram_markup(await get_message(54, msg_54))],state=OrderDataUser.mark_c3)
    async def start_mark(message: types.Message, state: FSMContext):
        user_data = await state.get_data()
        mess = message.text

        answers = user_data['answers']
        if mess == telegram_markup(await get_message(54, msg_54)):
            mess = None
            answers.append(mess)
        else:
            answers.append(mess[0])
        await state.update_data(answers=answers)

        await state.update_data(answerc3=mess)

        id_to_send = await get_massage_for_question(user_data['job_type'], 27)
        await bot.send_message(message['from']['id'], telegram_markup(await get_message(id_to_send, msg_27)))

        await OrderDataUser.mark_c4.set()

    @dp.message_handler(text=['1 - '+telegram_markup(await get_message(50, msg_50)),'2 - '+telegram_markup(await get_message(51, msg_51)),'3 - '+telegram_markup(await get_message(52, msg_52)),'4 - '+telegram_markup(await get_message(53, msg_53)),telegram_markup(await get_message(54, msg_54))],state=OrderDataUser.mark_c4)
    async def start_mark(message: types.Message, state: FSMContext):
        user_data = await state.get_data()
        mess = message.text

        answers = user_data['answers']
        if mess == telegram_markup(await get_message(54, msg_54)):
            mess = None
            answers.append(mess)
        else:
            answers.append(mess[0])
        await state.update_data(answers=answers)

        await state.update_data(answerc4=mess)

        id_to_send = await get_massage_for_question(user_data['job_type'], 28)
        await bot.send_message(message['from']['id'], telegram_markup(await get_message(id_to_send, msg_28)))
        await OrderDataUser.mark_c5.set()

    @dp.message_handler(text=['1 - '+telegram_markup(await get_message(50, msg_50)),'2 - '+telegram_markup(await get_message(51, msg_51)),'3 - '+telegram_markup(await get_message(52, msg_52)),'4 - '+telegram_markup(await get_message(53, msg_53)),telegram_markup(await get_message(54, msg_54))],state=OrderDataUser.mark_c5)
    async def start_mark(message: types.Message, state: FSMContext):
        user_data = await state.get_data()
        mess = message.text

        answers = user_data['answers']
        if mess == telegram_markup(await get_message(54, msg_54)):
            mess = None
            answers.append(mess)
        else:
            answers.append(mess[0])
        await state.update_data(answers=answers)

        await state.update_data(answerc5=mess)

        id_to_send = await get_massage_for_question(user_data['job_type'], 29)
        await bot.send_message(message['from']['id'], telegram_markup(await get_message(id_to_send, msg_29)))
        await OrderDataUser.mark_c6.set()






    @dp.message_handler(text=['1 - '+telegram_markup(await get_message(50, msg_50)),'2 - '+telegram_markup(await get_message(51, msg_51)),'3 - '+telegram_markup(await get_message(52, msg_52)),'4 - '+telegram_markup(await get_message(53, msg_53)),telegram_markup(await get_message(54, msg_54))],state=OrderDataUser.mark_c6)
    async def start_mark(message: types.Message, state: FSMContext):
        user_data = await state.get_data()
        mess = message.text

        answers = user_data['answers']
        if mess == telegram_markup(await get_message(54, msg_54)):
            mess = None
            answers.append(mess)
        else:
            answers.append(mess[0])
        await state.update_data(answers=answers)

        await state.update_data(answerc6=mess)
        await bot.send_message(message['from']['id'], telegram_markup(await get_message(63, msg_63)),reply_markup=(await mark_comment_keyboard()))
        await OrderDataUser.mark_c_comment.set()#1234

    @dp.message_handler(state=OrderDataUser.mark_c_comment)
    async def start_mark(message: types.Message, state: FSMContext):
        user_data = await state.get_data()

        mess = message.text
        if mess == telegram_markup(await get_message(60, msg_60)):
            mess = ''
        else:
            mess = '-' + mess + '\n\n'

        comments = user_data['comments']
        comments.append(mess)
        await state.update_data(comments=comments)

        await state.update_data(comm_c=mess)
        id_to_send = await get_massage_for_question(user_data['job_type'], 30)
        await bot.send_message(message['from']['id'], telegram_markup(await get_message(id_to_send, msg_30)))

        id_to_send = await get_massage_for_question(user_data['job_type'], 31)
        await bot.send_message(message['from']['id'], telegram_markup(await get_message(id_to_send, msg_31)), reply_markup=await mark_keyboard())
        await OrderDataUser.mark_d1.set()  # 1234





    @dp.message_handler(text=['1 - '+telegram_markup(await get_message(50, msg_50)),'2 - '+telegram_markup(await get_message(51, msg_51)),'3 - '+telegram_markup(await get_message(52, msg_52)),'4 - '+telegram_markup(await get_message(53, msg_53)),telegram_markup(await get_message(54, msg_54))],state=OrderDataUser.mark_d1)
    async def start_mark(message: types.Message, state: FSMContext):
        user_data = await state.get_data()
        mess = message.text

        answers = user_data['answers']
        if mess == telegram_markup(await get_message(54, msg_54)):
            mess = None
            answers.append(mess)
        else:
            answers.append(mess[0])
        await state.update_data(answers=answers)


        await state.update_data(answerd1=mess)

        id_to_send = await get_massage_for_question(user_data['job_type'], 32)
        await bot.send_message(message['from']['id'], telegram_markup(await get_message(id_to_send, msg_32)))
        await OrderDataUser.mark_d2.set()

    @dp.message_handler(text=['1 - '+telegram_markup(await get_message(50, msg_50)),'2 - '+telegram_markup(await get_message(51, msg_51)),'3 - '+telegram_markup(await get_message(52, msg_52)),'4 - '+telegram_markup(await get_message(53, msg_53)),telegram_markup(await get_message(54, msg_54))],state=OrderDataUser.mark_d2)
    async def start_mark(message: types.Message, state: FSMContext):
        user_data = await state.get_data()
        mess = message.text

        answers = user_data['answers']
        if mess == telegram_markup(await get_message(54, msg_54)):
            mess = None
            answers.append(mess)
        else:
            answers.append(mess[0])
        await state.update_data(answers=answers)

        await state.update_data(answerd2=mess)

        id_to_send = await get_massage_for_question(user_data['job_type'], 33)
        await bot.send_message(message['from']['id'], telegram_markup(await get_message(id_to_send, msg_33)))
        await OrderDataUser.mark_d3.set()

    @dp.message_handler(text=['1 - '+telegram_markup(await get_message(50, msg_50)),'2 - '+telegram_markup(await get_message(51, msg_51)),'3 - '+telegram_markup(await get_message(52, msg_52)),'4 - '+telegram_markup(await get_message(53, msg_53)),telegram_markup(await get_message(54, msg_54))],state=OrderDataUser.mark_d3)
    async def start_mark(message: types.Message, state: FSMContext):
        user_data = await state.get_data()
        mess = message.text

        answers = user_data['answers']
        if mess == telegram_markup(await get_message(54, msg_54)):
            mess = None
            answers.append(mess)
        else:
            answers.append(mess[0])
        await state.update_data(answers=answers)

        await state.update_data(answerd3=mess)

        id_to_send = await get_massage_for_question(user_data['job_type'], 34)
        await bot.send_message(message['from']['id'], telegram_markup(await get_message(id_to_send, msg_34)))
        await OrderDataUser.mark_d4.set()

    @dp.message_handler(text=['1 - '+telegram_markup(await get_message(50, msg_50)),'2 - '+telegram_markup(await get_message(51, msg_51)),'3 - '+telegram_markup(await get_message(52, msg_52)),'4 - '+telegram_markup(await get_message(53, msg_53)),telegram_markup(await get_message(54, msg_54))],state=OrderDataUser.mark_d4)
    async def start_mark(message: types.Message, state: FSMContext):
        user_data = await state.get_data()
        mess = message.text

        answers = user_data['answers']
        if mess == telegram_markup(await get_message(54, msg_54)):
            mess = None
            answers.append(mess)
        else:
            answers.append(mess[0])
        await state.update_data(answers=answers)

        await state.update_data(answerd4=mess)

        id_to_send = await get_massage_for_question(user_data['job_type'], 35)
        await bot.send_message(message['from']['id'], telegram_markup(await get_message(id_to_send, msg_35)))
        await OrderDataUser.mark_d5.set()

    @dp.message_handler(text=['1 - '+telegram_markup(await get_message(50, msg_50)),'2 - '+telegram_markup(await get_message(51, msg_51)),'3 - '+telegram_markup(await get_message(52, msg_52)),'4 - '+telegram_markup(await get_message(53, msg_53)),telegram_markup(await get_message(54, msg_54))],state=OrderDataUser.mark_d5)
    async def start_mark(message: types.Message, state: FSMContext):
        user_data = await state.get_data()
        mess = message.text

        answers = user_data['answers']
        if mess == telegram_markup(await get_message(54, msg_54)):
            mess = None
            answers.append(mess)
        else:
            answers.append(mess[0])
        await state.update_data(answers=answers)

        await state.update_data(answerad5=mess)
        await bot.send_message(message['from']['id'], telegram_markup(await get_message(64, msg_64)), reply_markup=await mark_comment_keyboard())
        await OrderDataUser.mark_d_comment.set()

    @dp.message_handler(state=OrderDataUser.mark_d_comment)
    async def start_mark(message: types.Message, state: FSMContext):
        user_data = await state.get_data()

        mess = message.text
        if mess == telegram_markup(await get_message(60, msg_60)):
            mess = ''
        else:
            mess = '-' + mess + '\n\n'

        comments = user_data['comments']
        comments.append(mess)
        await state.update_data(comments=comments)

        await state.update_data(comm_d=mess)
        id_to_send = await get_massage_for_question(user_data['job_type'], 36)
        await bot.send_message(message['from']['id'], telegram_markup(await get_message(id_to_send, msg_36)))
        id_to_send = await get_massage_for_question(user_data['job_type'], 37)
        await bot.send_message(message['from']['id'], telegram_markup(await get_message(id_to_send, msg_37)), reply_markup=await mark_keyboard())
        await OrderDataUser.mark_e1.set()

    @dp.message_handler(text=['1 - '+telegram_markup(await get_message(50, msg_50)),'2 - '+telegram_markup(await get_message(51, msg_51)),'3 - '+telegram_markup(await get_message(52, msg_52)),'4 - '+telegram_markup(await get_message(53, msg_53)),telegram_markup(await get_message(54, msg_54))],state=OrderDataUser.mark_e1)
    async def start_mark(message: types.Message, state: FSMContext):
        user_data = await state.get_data()
        mess = message.text

        answers = user_data['answers']
        if mess == telegram_markup(await get_message(54, msg_54)):
            mess = None
            answers.append(mess)
        else:
            answers.append(mess[0])
        await state.update_data(answers=answers)

        await state.update_data(answere1=mess)

        id_to_send = await get_massage_for_question(user_data['job_type'], 38)
        await bot.send_message(message['from']['id'], telegram_markup(await get_message(id_to_send, msg_38)))
        await OrderDataUser.mark_e2.set()

    @dp.message_handler(text=['1 - '+telegram_markup(await get_message(50, msg_50)),'2 - '+telegram_markup(await get_message(51, msg_51)),'3 - '+telegram_markup(await get_message(52, msg_52)),'4 - '+telegram_markup(await get_message(53, msg_53)),telegram_markup(await get_message(54, msg_54))],state=OrderDataUser.mark_e2)
    async def start_mark(message: types.Message, state: FSMContext):
        user_data = await state.get_data()
        mess = message.text

        answers = user_data['answers']
        if mess == telegram_markup(await get_message(54, msg_54)):
            mess = None
            answers.append(mess)
        else:
            answers.append(mess[0])
        await state.update_data(answers=answers)


        await state.update_data(answere2=mess)

        id_to_send = await get_massage_for_question(user_data['job_type'], 39)
        await bot.send_message(message['from']['id'], telegram_markup(await get_message(id_to_send, msg_39)))
        await OrderDataUser.mark_e3.set()

    @dp.message_handler(text=['1 - '+telegram_markup(await get_message(50, msg_50)),'2 - '+telegram_markup(await get_message(51, msg_51)),'3 - '+telegram_markup(await get_message(52, msg_52)),'4 - '+telegram_markup(await get_message(53, msg_53)),telegram_markup(await get_message(54, msg_54))],state=OrderDataUser.mark_e3)
    async def start_mark(message: types.Message, state: FSMContext):
        user_data = await state.get_data()
        mess = message.text

        answers = user_data['answers']
        if mess == telegram_markup(await get_message(54, msg_54)):
            mess = None
            answers.append(mess)
        else:
            answers.append(mess[0])
        await state.update_data(answers=answers)

        await state.update_data(answere3=mess)

        id_to_send = await get_massage_for_question(user_data['job_type'], 40)
        await bot.send_message(message['from']['id'], telegram_markup(await get_message(id_to_send, msg_40)))
        await OrderDataUser.mark_e4.set()

    @dp.message_handler(text=['1 - '+telegram_markup(await get_message(50, msg_50)),'2 - '+telegram_markup(await get_message(51, msg_51)),'3 - '+telegram_markup(await get_message(52, msg_52)),'4 - '+telegram_markup(await get_message(53, msg_53)),telegram_markup(await get_message(54, msg_54))],state=OrderDataUser.mark_e4)
    async def start_mark(message: types.Message, state: FSMContext):
        user_data = await state.get_data()
        mess = message.text

        answers = user_data['answers']
        if mess == telegram_markup(await get_message(54, msg_54)):
            mess = None
            answers.append(mess)
        else:
            answers.append(mess[0])
        await state.update_data(answers=answers)

        await state.update_data(answere4=mess)

        id_to_send = await get_massage_for_question(user_data['job_type'], 41)
        await bot.send_message(message['from']['id'], telegram_markup(await get_message(id_to_send, msg_41)))
        await OrderDataUser.mark_e5.set()

    @dp.message_handler(text=['1 - '+telegram_markup(await get_message(50, msg_50)),'2 - '+telegram_markup(await get_message(51, msg_51)),'3 - '+telegram_markup(await get_message(52, msg_52)),'4 - '+telegram_markup(await get_message(53, msg_53)),telegram_markup(await get_message(54, msg_54))],state=OrderDataUser.mark_e5)
    async def start_mark(message: types.Message, state: FSMContext):
        user_data = await state.get_data()
        mess = message.text

        answers = user_data['answers']
        if mess == telegram_markup(await get_message(54, msg_54)):
            mess = None
            answers.append(mess)
        else:
            answers.append(mess[0])
        await state.update_data(answers=answers)

        await state.update_data(answere5=mess)

        id_to_send = await get_massage_for_question(user_data['job_type'], 42)
        await bot.send_message(message['from']['id'], telegram_markup(await get_message(id_to_send, msg_42)))
        await OrderDataUser.mark_e6.set()


    @dp.message_handler(text=['1 - '+telegram_markup(await get_message(50, msg_50)),'2 - '+telegram_markup(await get_message(51, msg_51)),'3 - '+telegram_markup(await get_message(52, msg_52)),'4 - '+telegram_markup(await get_message(53, msg_53)),telegram_markup(await get_message(54, msg_54))],state=OrderDataUser.mark_e6)
    async def start_mark(message: types.Message, state: FSMContext):
        user_data = await state.get_data()
        mess = message.text

        answers = user_data['answers']
        if mess == telegram_markup(await get_message(54, msg_54)):
            mess = None
            answers.append(mess)
        else:
            answers.append(mess[0])
        await state.update_data(answers=answers)

        await state.update_data(answere6=mess)
        await bot.send_message(message['from']['id'], telegram_markup(await get_message(65, msg_65)), reply_markup=await mark_comment_keyboard())
        await OrderDataUser.mark_e_comment.set()

    @dp.message_handler(state=OrderDataUser.mark_e_comment)
    async def start_mark(message: types.Message, state: FSMContext):
        await bot.send_message(message['from']['id'], telegram_markup(await get_message(91, msg_91)))

        user_data = await state.get_data()

        mess = message.text
        if mess == telegram_markup(await get_message(60, msg_60)):
            mess = ''
        else:
            mess='-' + mess + '\n\n'
        comments = user_data['comments']
        comments.append(mess)

        await state.update_data(comments=comments)
        await state.update_data(comm_e=mess)
        user_data = await state.get_data()
        await state.finish()
      #  print(user_data['mark_type'])
        #print(telegram_markup(await get_message(4, 'Оценка коллег')))
        dict_myself = {'id_tele': message['from']['id']}
        user_from_job = await user_find_from_jоb_with_id(dict_myself)
        await update_start_mark(user_from_job)
        if user_data['mark_type']==telegram_markup(await get_message(3, 'Оценка себя (360)')):
            dict = {'id_tele': message['from']['id']}


            user = await user_find_async(dict)
            phone_num = await get_phone_num_from_user(user)
            #user_mark = await mark_someone(dict)
            await excel_make(user_data, phone_num, 'me', user_data['job_type'])
            dict_user = {'id_tele': message['from']['id']}
            await mark_yourself(dict_user)
            await end_or_not_marking_after_yourself(dict_user)

            #await increase_to_count(dict_user)

            #dict = {'fio': user_data['your_marking_user']}
            try:
                if (await many_mark_me(dict) == 0) and (await user_get_many_marked_me(dict) > 0) and (
                await marked_by_someone(dict)):
                    await marked_by_someone(dict)
                    hrs_id = await get_hr_ids()
                    dict = {'id_tele': message['from']['id']}
                    user_name = await user_find_fio(dict)
                   #user_name = get_only_fio_from_user(user)
                   # user_name=user_data['your_marking_user']
                    str_file = "excelFiles/"+user_name+".xlsx"
                    print(str_file)
                    for hr_id in hrs_id:
                        await bot.send_document(hr_id, open(str_file, "rb"))
            except:
                pass
        elif user_data['mark_type']==telegram_markup(await get_message(4, 'Оценка коллег')):
            dict = {'fio':user_data['your_marking_user']}
            user = await user_find_async(dict)
            phone_num = await get_phone_num_from_user(user)
            print(dict)
            #user_mark = await mark_someone(dict)
            #print(user_mark)
            #await excel_make(user_data, phone_num, user_mark, 'O')
            await excel_make(user_data, phone_num, 'colleg', user_data['job_type'])
            await remove_from_manyomany_colleagues(message['from']['id'], phone_num)
            await increase_counter_marked_user(dict)

            dict_user = {'id_tele': message['from']['id']}
            await increase_to_count(dict_user)

            dict = {'fio': user_data['your_marking_user']}
            try:
                if (await many_mark_me(dict) == 0) and (await user_get_many_marked_me(dict) > 0) and (
                    await marked_by_someone(dict)):
                    hrs_id = await get_hr_ids()
                    await user_report_is(dict)
                    user_name=user_data['your_marking_user']
                    str_file = "excelFiles/"+user_name+".xlsx"
                    print(str_file)
                    for hr_id in hrs_id:
                        await bot.send_document(hr_id, open(str_file, "rb"))
            except:
                pass
        elif user_data['mark_type'] == telegram_markup(await get_message(5, 'Оцени руководителя')):
            dict = {'fio': user_data['your_marking_user']}
            user = await user_find_async(dict)
            phone_num = await get_phone_num_from_user(user)
            print(dict)
          #  user_mark = await mark_someone(dict)
          #  print(user_mark)
            #  await excel_make(user_data, phone_num, user_mark, 'L')
            await excel_make(user_data, phone_num, 'teamLead', user_data['job_type'])
            await remove_from_manyomany_teamLeader(message['from']['id'], phone_num)
           # await increase_counter_marked_user(dict)

            await increase_counter_marked_user(dict)
            dict_user = {'id_tele': message['from']['id']}
            await increase_to_count(dict_user)

            dict = {'fio': user_data['your_marking_user']}
            try:
                if (await many_mark_me(dict) == 0) and (await user_get_many_marked_me(dict) > 0) and (
                await marked_by_someone(dict)):
                    await user_report_is(dict)
                    hrs_id = await get_hr_ids()
                    user_name = user_data['your_marking_user']
                    str_file = "excelFiles/" + user_name + ".xlsx"
                    print(str_file)
                    for hr_id in hrs_id:
                        await bot.send_document(hr_id, open(str_file, "rb"))
            except:
                pass
        elif user_data['mark_type'] == telegram_markup(await get_message(6, 'оценка подчинённых')):
            dict = {'fio': user_data['your_marking_user']}
            user = await user_find_async(dict)
            phone_num = await get_phone_num_from_user(user)
            print(dict)
            #user_mark = await mark_someone(dict)
            #print(user_mark)
            #await excel_make(user_data, phone_num, user_mark, 'I')
            await excel_make(user_data, phone_num, 'employer', user_data['job_type'])
            await remove_from_manyomany_employers(message['from']['id'], phone_num)
            await increase_counter_marked_user(dict)

            dict_user = {'id_tele': message['from']['id']}
            await increase_to_count(dict_user)
          #  print(await many_mark_me(dict))
          #  print(await user_get_many_marked_me(dict))
            #print(await mark_someone(dict))
            #если его никто не долэжен оценить
            #если его оценил больше 1 человека
            #если он сам себя
            dict = {'fio': user_data['your_marking_user']}
            try:
                if (await many_mark_me(dict)==0) and (await user_get_many_marked_me(dict)>0) and (await marked_by_someone(dict)):
                    await user_report_is(dict)
                    hrs_id = await get_hr_ids()
                    user_name = user_data['your_marking_user']
                    str_file = "excelFiles/" + user_name + ".xlsx"
                    print(str_file)
                    for hr_id in hrs_id:

                        await bot.send_document(hr_id, open(str_file, "rb"))
            except:
                pass
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
