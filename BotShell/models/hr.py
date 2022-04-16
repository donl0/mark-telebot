from django.db import models

from .teamLeader import TeamLeader
from .employments import Employment


class Hr(models.Model):
    fio = models.CharField(max_length=100, default="NULL", verbose_name="Ф.И.О.")
    phone_num = models.CharField(max_length=100, default="+398989889", verbose_name="Номер телефона", unique=True)
    colleagues = models.ManyToManyField("self", blank=True, verbose_name="Сотрудники для оценивания из HR")
    employments = models.ManyToManyField(Employment, blank=True, verbose_name="Сотрудники для оценивания из списка подчинённых",)
    team_leaders = models.ManyToManyField(TeamLeader, blank=True,
                                         verbose_name="Сотрудники для оценивания из списка руководителей")

   # speciality_choice = [
   #     ('Top_manager', 'Топ-менеджер'),
   #     ('Manager', 'Менеджер'),
   #     ('specialist', 'Специалист'),
  #  ]
    #speciality = models.CharField(default='Специальность', choices=speciality_choice, max_length=2)


    mail = models.CharField(max_length=100, default="NULL", verbose_name="@mail")
    id_tele = models.IntegerField(default=None, verbose_name="Телеграм id", null=True, blank=True)
    name_tele = models.CharField(max_length=50, default="NULL", verbose_name="телеграм имя")

    def __str__(self):
        return self.fio+' '+self.phone_num

    class Meta:
        verbose_name = 'HR1'
        verbose_name_plural = "HR1"
