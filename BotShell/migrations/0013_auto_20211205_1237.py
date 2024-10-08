# Generated by Django 3.2.7 on 2021-12-05 09:37

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BotShell', '0012_auto_20211204_2134'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailingrate',
            options={'verbose_name': 'Напоминания', 'verbose_name_plural': 'Напоминания'},
        ),
        migrations.AddField(
            model_name='mailingrate',
            name='text',
            field=ckeditor.fields.RichTextField(default=1, max_length=1024, verbose_name='Текст напоминания (С этим сообщением каждому сотруднику будет также отправлен свой дедлайн)'),
            preserve_default=False,
        ),
    ]
