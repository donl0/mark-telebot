import asyncio
import aioschedule
from aiogram import Bot, Dispatcher
#from ..utils.dbcommands import clear24h_watches, clear7d_watches, clear1m_watches

#bot = Bot(token=settings.TG_TOKEN, parse_mode='HTML', loop=loop)

#dp = Dispatcher(bot, storage=MemoryStorage())
from BotShell.models import AllEmployment
from BotShell.utils.dbcommands import notification_rate, match_last_time_with_mail_rate, \
    get_employers_list_with_no_rady_report, match_last_time_with_mail_rate_sync, get_mess_from_mail_rate_sync, \
    get_hr_ids, get_employers_list_with_start_record, get_employers_list_with_no_start_record, \
    get_employers_list_with_end_record
from BotShell.utils.text import telegram_markup
from BotShell.utils.tools import plus_all_from_different_models, get_only_names_from_users, get_only_id_from_users, \
    get_only_dead_line_from_users


async def clear24h():
    pass


async def clear7d():
    pass


async def clear1m():
    pass

async def print1():
    print('+')

async def simple_querry():
    AllEmployment.objects.filter()


async def report_for_HR(bot):
    users_diff_models = await get_employers_list_with_start_record()
    plused_mass = await plus_all_from_different_models(users_diff_models[0], users_diff_models[1],
                                                       users_diff_models[2])
    fio_started_mass = await get_only_names_from_users(plused_mass)

    users_diff_models_no_saretd = await get_employers_list_with_no_start_record()
    plused_mass_no_saretd = await plus_all_from_different_models(users_diff_models_no_saretd[0], users_diff_models_no_saretd[1],
                                                       users_diff_models_no_saretd[2])
    fio_no_started_mass = await get_only_names_from_users(plused_mass_no_saretd)


    users_diff_models_end_rec = await get_employers_list_with_end_record()
    plused_mass_end_rec = await plus_all_from_different_models(users_diff_models_end_rec[0], users_diff_models_end_rec[1],
                                                       users_diff_models_end_rec[2])
    fio_end_rec_started_mass = await get_only_names_from_users(plused_mass_end_rec)
    counter_all=len(fio_started_mass)+len(fio_no_started_mass)+len(fio_end_rec_started_mass)
    persent_end = (len(fio_end_rec_started_mass)/counter_all)*100
    mess = f'Прошло оценку около {int(persent_end)}% сотрудников\n\n📌Начали проверку:\n'
    for user_name in fio_started_mass:
        mess+=str(user_name)+'\n'
    mess+='\n\n📌Не начали проверку:\n'
    for user_name in fio_no_started_mass:
        mess+=str(user_name)+'\n'
    mess += '\n\n📌Закончили оценку:\n'
    for user_name in fio_end_rec_started_mass:
        mess += str(user_name) + '\n'

    hr_id_mass = await get_hr_ids()
    for hr_id in hr_id_mass:
        await bot.send_message(hr_id, mess)


async def check_to_start_mailing(bot):
    print('POPL V START EMAILING')
    if await match_last_time_with_mail_rate_sync():
        users_diff_models = await get_employers_list_with_no_rady_report()
        plused_mass = await plus_all_from_different_models(users_diff_models[0], users_diff_models[1],
                                                           users_diff_models[2])

        last_mass = await get_only_id_from_users(plused_mass)
        all_dead_lines= await get_only_dead_line_from_users(plused_mass)
        message = telegram_markup(await get_mess_from_mail_rate_sync())
        i=0
        print(last_mass)
        for id_tele in last_mass:
            print(id_tele)

            try:
                await bot.send_message(id_tele, message+'\n\nДедлайн: '+str(all_dead_lines[i]))
            except:
                pass
            i+=1


async def scheduler(bot, dp):
  #  aioschedule.every(7).days.at("10:00").do(clear7d)
   # aioschedule.every(30).days.at("10:00").do(clear1m)
   # dp = Dispatcher(bot, storage=MemoryStorage())

    aioschedule.every().minute.do(simple_querry)
    aioschedule.every(1).hour.do(check_to_start_mailing, bot=bot)
    aioschedule.every().days.at("15:00").do(report_for_HR, bot=bot)


    #aioschedule.every(await notification_rate()).seconds.do(print1)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)

