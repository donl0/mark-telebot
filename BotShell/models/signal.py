
from django.db.models.signals import post_save, pre_save, m2m_changed

from BotShell.models import AllEmployment, TeamLeader, Employment, Сolleague
from django.dispatch import receiver

#@receiver(m2m_changed, sender=AllEmployment)
def a1(sender, instance, **kwargs):
    ###сдлетаь трай жэкс если нету роли

    user = AllEmployment.objects.get(phone_num=instance.phone_num)

    role = user.role.all()
    print(role)
    print('SDELALA')
    if 'Руководитель' in role:
        TeamLeader.objects.get_or_create(user)
       # add_to_teamleader(user)
    elif 'Подчиненный' in role:
        Employment.objects.get_or_create(user)
       # add_to_employment(user)
    elif 'Коллега' in role:
        Сolleague.objects.get_or_create(user)
      #  add_to_colleague(user)
    print(role[0])
    #list(user.role.all())
   # print(instance.all())
   # print(user.role.all())
    #print(user)



m2m_changed.connect(a1, sender = AllEmployment.role.through)