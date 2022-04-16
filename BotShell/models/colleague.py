from django.db import models

from . import MY_CHOICES, AllEmployment
from .employments import Employment


class Сolleague(AllEmployment):

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'Коллега'
        verbose_name_plural = 'Коллеги'
