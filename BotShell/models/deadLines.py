from django.db import models




class DeadLines(models.Model):
    dead_line = models.DateTimeField(verbose_name='Дедлайн для какого-либо сотрудника')
    make_to_all_this_deadline = models.BooleanField(default=False, verbose_name='Установить этот дедлайн всем сотрудникам?')

    def __str__(self):
        return str(self.dead_line)

    class Meta:
        verbose_name = 'Дедлайн'
        verbose_name_plural = 'Дедлайны'

