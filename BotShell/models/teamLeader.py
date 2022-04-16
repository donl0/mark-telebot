from django.db import models

from . import AllEmployment


class TeamLeader(AllEmployment):


    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'Руководитель'
        verbose_name_plural = 'Руководители'
