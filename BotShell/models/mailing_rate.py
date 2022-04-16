from django.db import models

from .teamLeader import TeamLeader
from .employments import Employment
from ..utils.text import clean_html_markup
from ckeditor.fields import RichTextField


class MailingRate(models.Model):
    text = RichTextField(max_length=1024, verbose_name='Текст напоминания (С этим сообщением каждому сотруднику будет также отправлен свой дедлайн)')

    mail_rate = models.IntegerField(default=120, verbose_name='Напоминание сотрудником, не закончившим оценку, поисходит раз в часов: ')
    time_from_last_mail = models.IntegerField(default=0, verbose_name='Прошло часов с педыдущего уведомления: ')

    def __str__(self):

        text = str(clean_html_markup(self.text))
        if len(text) > 30:
            return f'{text[:45]}...'
        else:
            return text

    class Meta:
        verbose_name = 'Напоминания'
        verbose_name_plural = 'Напоминания'