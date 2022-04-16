from django.db import models
from django.db.models.signals import post_save, m2m_changed

from .allEmployees import AllEmployment
from .deadLines import DeadLines
from .employments import Employment


class Manager(models.Model):
    fio = models.OneToOneField(AllEmployment, on_delete=models.CASCADE)
    markStart = models.BooleanField(verbose_name='Начал оченку', default=False)
    markEnd = models.BooleanField(verbose_name='Закончил оченку', default=False)
    markByHimSelf = models.BooleanField(verbose_name='Оценил сам себя', default=False)
    #markBySomeone = models.BooleanField(verbose_name='Был ли уже оценен кем-либо', default=False)
    manyToMark = models.IntegerField(verbose_name='осталось оценить', default=0)
    markCounter = models.IntegerField(verbose_name='сколько оценено', default=0)
    counterMarkedMe = models.IntegerField(verbose_name='Сколько меня оценило', default=0)
    reportIsReady = models.BooleanField(verbose_name='Готов ли отчёт по этому человеку', default=False)
    dead_line = models.DateTimeField(verbose_name='Дедлайн для сотрудника', blank=True, null=True)
    make_to_all_this_deadline = models.BooleanField(default=False,
                                                    verbose_name='Установить этот дедлайн всем сотрудникам?')
    teamLeader = models.ManyToManyField(AllEmployment, blank=True, verbose_name="Руководители, которых осталось оценить", related_name='lead_m')
    colleagues = models.ManyToManyField(AllEmployment, blank=True, verbose_name="Коллеги, которых осталось оценить", related_name='colleg')
    employers = models.ManyToManyField(AllEmployment, blank=True, verbose_name="Подчинённые, которых осталось оценить", related_name='employee')

    all_employers = models.TextField(max_length=10000, blank=True, default="", verbose_name="Все подчиненные", unique=False)
    #all_employers = models.ManyToManyField(AllEmployment, blank=True, verbose_name="Все подчинённые\n(Заполняется автоматически)", related_name='all_employee_manager')
    def __str__(self):
        return str(self.fio)+' статус начала оценки:'+str(self.markStart)+' статус окончания всех оценок:'+str(self.markEnd)

    class Meta:
        verbose_name = 'Менеджер'
        verbose_name_plural = 'Менеджеры'


def a1(sender, instance, **kwargs):
    ###сдлетаь трай жэкс если нету роли
   # print('---------------------')
    #print(instance.teamLeader.all())
   # print(instance.colleagues.all())
   # print(instance.employers.all())
    counter = len(instance.teamLeader.all())+len(instance.colleagues.all())+len(instance.employers.all())
    Manager.objects.filter(fio=instance.fio).update(manyToMark=counter)

    if (counter==0) and (instance.markCounter>0) and (instance.markByHimSelf==True):
        Manager.objects.filter(fio=instance.fio).update(markEnd=True)
    else:
        Manager.objects.filter(fio=instance.fio).update(markEnd=False)

    all_emp = str(instance.all_employers)
    all_emp = all_emp.split(';')
    if not len(instance.employers.all())==0:
        for emp in instance.employers.all():
            print('emp: '+str(emp))
            if not emp.fio in all_emp:
                print(emp.fio)
                #TopManager.objects.filter(fio=instance.fio).update(all_employers=F('all_employers')+str(emp.fio)+';')
                prev_inf = Manager.objects.get(fio=instance.fio).all_employers
                prev_inf +=str(emp.fio)+';'
                Manager.objects.filter(fio=instance.fio).update(all_employers=prev_inf)

   # TopManager.objects.filter(fio=instance.fio).update(markCounter=F('markCounter')+1)
    #instance.update(manyToMark=counter)
    #print(counter)
    #print(instance)
  #  manyToMark
    #instance.update
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


m2m_changed.connect(a1, sender = Manager.teamLeader.through)
m2m_changed.connect(a1, sender = Manager.colleagues.through)
m2m_changed.connect(a1, sender = Manager.employers.through)


def create_something3(sender, instance, created, **kwargs):
    print('ПРОШЁЁЁЁЁЁЁЁЁЁЁЛ------------')
    print(instance.job_type)
    # TopManager.objects.get_or_create(fio=instance)
    if created:  # new object will be created
        if instance.job_type == 'manager':
            Manager.objects.get_or_create(fio=instance)
    else:
        if instance.job_type == 'manager':
            Manager.objects.get_or_create(fio=instance)
'''
 else:
            try:
                dict = {'fio': instance}
                instance = Manager.objects.get(**dict)
                instance.delete()
            except:
                pass
                '''


post_save.connect(create_something3, sender = AllEmployment)