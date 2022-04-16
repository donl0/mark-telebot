from django.db import models
from django.db.models.signals import m2m_changed, post_save

from .allEmployees import AllEmployment
from django.db.models import F, Q

from .deadLines import DeadLines


class TopManager(models.Model):
    fio = models.OneToOneField(AllEmployment, on_delete=models.CASCADE, related_name='obj_from_all_empl')
    markStart = models.BooleanField(verbose_name='Начал оченку', default=False)
    markEnd = models.BooleanField(verbose_name='Закончил оченку', default=False)
    markByHimSelf = models.BooleanField(verbose_name='Оценил сам себя', default=False)
    manyToMark = models.IntegerField(verbose_name='осталось оценить', default=0)
    markCounter = models.IntegerField(verbose_name='сколько оценено', default=0)
    counterMarkedMe = models.IntegerField(verbose_name='Сколько меня оценило', default=0)
    reportIsReady = models.BooleanField(verbose_name='Готов ли отчёт', default=False)
    dead_line = models.DateTimeField(verbose_name='Дедлайн для сотрудника', blank=True, null=True)
    make_to_all_this_deadline = models.BooleanField(default=False,
                                                    verbose_name='Установить этот дедлайн всем сотрудникам?')
    teamLeader = models.ManyToManyField(AllEmployment, blank=True, verbose_name="Руководители, которых осталось оценить", related_name='lead_spec')
    colleagues = models.ManyToManyField(AllEmployment, blank=True, verbose_name="Коллеги, которых осталось оценить", related_name='coll_topm')
    employers = models.ManyToManyField(AllEmployment, blank=True, verbose_name="Подчинённые, которых осталось оценить", related_name='employee_topm')

    all_employers = models.CharField(max_length=10000, blank=True, default="", verbose_name="Все подчиненные", unique=False)
    #all_employers = models.ManyToManyField(AllEmployment, blank=True, verbose_name="Все подчинённые\n(Заполняется автоматически)", related_name='all_employee_top_manager')
    def __str__(self):
        return str(self.fio)+' статус начала оценки:'+str(self.markStart)+' статус окончания всех оценок:'+str(self.markEnd)

    class Meta:
        verbose_name = 'Топ менеджер'
        verbose_name_plural = 'Топ менеджеры'


def a1(sender, instance, **kwargs):
    counter = len(instance.teamLeader.all())+len(instance.colleagues.all())+len(instance.employers.all())
    TopManager.objects.filter(fio=instance.fio).update(manyToMark=counter)
    if (counter==0) and (instance.markCounter>0) and (instance.markByHimSelf==True):#и ещё себя оценил
        TopManager.objects.filter(fio=instance.fio).update(markEnd=True)
    else:
        TopManager.objects.filter(fio=instance.fio).update(markEnd=False)

    all_emp = str(instance.all_employers)
    all_emp = all_emp.split(';')
    if not len(instance.employers.all())==0:
        for emp in instance.employers.all():
            print('emp: '+str(emp))
            if not emp.fio in all_emp:
                print(emp.fio)
                #TopManager.objects.filter(fio=instance.fio).update(all_employers=F('all_employers')+str(emp.fio)+';')
                prev_inf = TopManager.objects.get(fio=instance.fio).all_employers
                prev_inf +=str(emp.fio)+';'
                TopManager.objects.filter(fio=instance.fio).update(all_employers=prev_inf)

''' 
   for emp in instance.employers.all():
     #   print(emp)
      #  user_to_add = {'phone_num': user_id_to_remove}
        user = TopManager.objects.get(fio=instance.fio)
     #   print(user)
        emp_to_add = AllEmployment.objects.get(fio=emp.fio)
      #  print('emp_to_add:' +str(emp_to_add))
        res = user.all_employers.add(emp_to_add)
       # print('user: '+str(user))
      #  print('emp_to_add:' + str(emp_to_add))
      #  print('res: '+str(res))
      #  print(user.all_employers.all())
        user2_all_emp = TopManager.objects.get(fio=instance.fio).all_employers.all()
        print('user2_all_emp: '+str(user2_all_emp))
        #user2_save = TopManager.objects.get(fio=instance.fio)
      #  print('VSE USERS: '+str(user2))
      #  user.save()
        #user2_save.save()
     #   super().save()
'''
'''
    user = TopManager.objects.get(phone_num=instance.fio)

    role = user.role.all()
    print(role)
    print('SDELALA')
    if 'Руководитель' in role:
        print('1')
        #TeamLeader.objects.get_or_create(user)
       # add_to_teamleader(user)
    elif 'Подчиненный' in role:
        print('2')
     #   Employment.objects.get_or_create(user)
       # add_to_employment(user)
    elif 'Коллега' in role:
        print('3')
       # Сolleague.objects.get_or_create(user)
      #  add_to_colleague(user)
    print(role[0])
    #list(user.role.all())
   # print(instance.all())
   # print(user.role.all())
    #print(user)
'''


m2m_changed.connect(a1, sender = TopManager.teamLeader.through)
m2m_changed.connect(a1, sender = TopManager.colleagues.through)
m2m_changed.connect(a1, sender = TopManager.employers.through)


def create_something1(sender, instance, created, **kwargs):
    print('ПРОШЁЁЁЁЁЁЁЁЁЁЁЛ------------')
    print(instance.job_type)
   # TopManager.objects.get_or_create(fio=instance)
    if created:  # new object will be created
        if instance.job_type == 'TopManager':
            TopManager.objects.get_or_create(fio=instance)
    else:
        if instance.job_type=='TopManager':
            TopManager.objects.get_or_create(fio=instance)
        '''else:
            try:
                dict={'fio':instance}
                instance = TopManager.objects.get(**dict)
                instance.delete()
            except:
                pass'''




post_save.connect(create_something1, sender = AllEmployment)


