import asyncio

from markBot import settings
from .deadLines import DeadLines
from .allEmployees import MY_CHOICES, AllEmployment
from .colleague import Сolleague
from .employments import Employment
from .topManager import TopManager
from .hr import Hr
from .mailing import Mailing
from .mailing_rate import MailingRate
from .manager import Manager
from .specialist import Specialist
from .teamLeader import TeamLeader
from .messageEditor import Message
from aiogram import Bot
from django.db.models.signals import post_save, pre_save, m2m_changed

from BotShell.models import AllEmployment, TeamLeader, Employment, Сolleague
from django.dispatch import receiver

#@receiver(m2m_changed, sender=AllEmployment)
from ..utils.dbcommands import many_mark_me_no_asyns, many_mark_me_no_asyns_with_user
from ..utils.text import telegram_markup
from ..utils.tools import get_only_id_from_users, get_only_id_from_users_bo_async


def make_global_deadline(sender, instance, created, **kwargs):
    print('-----------')
    print(instance.dead_line)
    print(instance)
  #  print(instance.make_to_all_this_deadline)
    if instance.make_to_all_this_deadline:
        Specialist.objects.filter().update(dead_line=instance.dead_line)
        Manager.objects.filter().update(dead_line=instance.dead_line)
        TopManager.objects.filter().update(dead_line=instance.dead_line)




post_save.connect(make_global_deadline, sender = TopManager)
post_save.connect(make_global_deadline, sender = Specialist)
post_save.connect(make_global_deadline, sender = Manager)



def start_sending(sender, instance, created, **kwargs):
    print('------------------------------')
    print(instance)
  #  print(instance.make_to_all_this_deadline)
    if instance.send_or_not:
        users_mass = AllEmployment.objects.filter()
        print('--------------------------------')
        print(users_mass)
        id_users_mass = get_only_id_from_users_bo_async(users_mass)
        print(id_users_mass)
        Mailing.objects.filter(text=instance.text).update(send_or_not=False)
        #bot = Bot(token=settings.TG_TOKEN, parse_mode='HTML', loop=None)
        print(id_users_mass)
        asyncio.run(send_to_user(id_users_mass, telegram_markup(instance.text)))

async def send_to_user(id_users_mass, text):
    bot = Bot(token=settings.TG_TOKEN, parse_mode='HTML', loop=None)
    for id_tele in id_users_mass:
        print(id_tele)

        if id_tele == None:
            continue
        # asyncio.run(send_to_user(bot, id_tele, telegram_markup(instance.text)))
        await bot.send_message(id_tele, text)

      #  try:
      #      await bot.send_message(id_tele, text)
      #  except:
       #     pass
    #await bot.send_message(id_tele, text)


post_save.connect(start_sending, sender = Mailing)
#post_save.connect(asyncio.run(start_sending()), sender = Mailing)