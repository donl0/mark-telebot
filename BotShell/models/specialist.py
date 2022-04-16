from django.db import models
from django.db.models.signals import post_save, m2m_changed

from . import DeadLines
from .allEmployees import AllEmployment



class Specialist(models.Model):
    fio = models.OneToOneField(AllEmployment, on_delete=models.CASCADE)
    markStart = models.BooleanField(verbose_name='Начал оченку', default=False)
    markEnd = models.BooleanField(verbose_name='Закончил оченку', default=False)
    markByHimSelf = models.BooleanField(verbose_name='Оценил сам себя', default=False)
    #markBySomeone = models.BooleanField(verbose_name='Был ли уже оценен кем-либо', default=False)
    manyToMark = models.IntegerField(verbose_name='осталось оценить', default=0)
    markCounter = models.IntegerField(verbose_name='сколько оценено', default=0)
    counterMarkedMe = models.IntegerField(verbose_name='Сколько меня оценило', default=0)
    reportIsReady = models.BooleanField(verbose_name='Готов ли отчёт', default=False)
    dead_line = models.DateTimeField(verbose_name='Дедлайн для сотрудника', blank=True, null=True)
    make_to_all_this_deadline = models.BooleanField(default=False,
                                                    verbose_name='Установить этот дедлайн всем сотрудникам?')
    teamLeader = models.ManyToManyField(AllEmployment, blank=True, verbose_name="Руководители, которых осталось оценить", related_name='lead_topm')
    colleagues = models.ManyToManyField(AllEmployment, blank=True, verbose_name="Коллеги, которых осталось оценить", related_name='colleg_spec')

    def __str__(self):
        return str(self.fio)+' статус начала оценки:'+str(self.markStart)+' статус окончания всех оценок:'+str(self.markEnd)

    class Meta:
        verbose_name = 'Специалист'
        verbose_name_plural = 'Специалисты'


def counter_to_mark(sender, instance, **kwargs):
    ###сдлетаь трай жэкс если нету роли
    # print('---------------------')
    # print(instance.teamLeader.all())
    # print(instance.colleagues.all())
    # print(instance.employers.all())
    counter = len(instance.teamLeader.all()) + len(instance.colleagues.all())
    Specialist.objects.filter(fio=instance.fio).update(manyToMark=counter)
    if (counter==0) and (instance.markCounter>0) and (instance.markByHimSelf==True):
        Specialist.objects.filter(fio=instance.fio).update(markEnd=True)
    else:
        Specialist.objects.filter(fio=instance.fio).update(markEnd=False)
m2m_changed.connect(counter_to_mark, sender=Specialist.teamLeader.through)
m2m_changed.connect(counter_to_mark, sender=Specialist.colleagues.through)


def create_something2(sender, instance, created, **kwargs):
    print(instance.job_type)
    # TopManager.objects.get_or_create(fio=instance)
    if created:  # new object will be created
        if instance.job_type == 'specialist':
            Specialist.objects.get_or_create(fio=instance)
    else:
        if instance.job_type == 'specialist':
            Specialist.objects.get_or_create(fio=instance)
        else:
            try:
                dict = {'fio': instance.fio}
                instance = Specialist.objects.get(**dict)
                instance.delete()
            except:
                pass


post_save.connect(create_something2, sender = AllEmployment)