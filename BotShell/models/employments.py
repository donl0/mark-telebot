from django.db import models

from BotShell.models import MY_CHOICES, AllEmployment


class Employment(AllEmployment):

    def __str__(self):
        return self.fio + ' ' + self.phone_num

    class Meta:
        verbose_name = 'Подчинённый'
        verbose_name_plural = 'Подчинённые'
