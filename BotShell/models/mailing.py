from django.db import models

from ..utils.text import clean_html_markup
from ckeditor.fields import RichTextField



class Mailing(models.Model):
    text = RichTextField(max_length=1024, verbose_name='Текст для рассылки')

    send_or_not = models.BooleanField(default=False, verbose_name='Произвести рассылку этого сообщения прямо сейчас')
    def __str__(self):

        text = str(clean_html_markup(self.text))
        if len(text) > 30:
            return f'{text[:45]}...'
        else:
            return text

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылка'


