# Generated by Django 3.2.7 on 2021-12-05 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BotShell', '0013_auto_20211205_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='make_to_all_this_deadline',
            field=models.BooleanField(default=False, verbose_name='Установить этот дедлайн всем сотрудникам?'),
        ),
        migrations.AddField(
            model_name='specialist',
            name='make_to_all_this_deadline',
            field=models.BooleanField(default=False, verbose_name='Установить этот дедлайн всем сотрудникам?'),
        ),
        migrations.AddField(
            model_name='topmanager',
            name='make_to_all_this_deadline',
            field=models.BooleanField(default=False, verbose_name='Установить этот дедлайн всем сотрудникам?'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='dead_line',
            field=models.DateTimeField(verbose_name='Дедлайн для сотрудника'),
        ),
        migrations.AlterField(
            model_name='specialist',
            name='dead_line',
            field=models.DateTimeField(verbose_name='Дедлайн для сотрудника'),
        ),
        migrations.AlterField(
            model_name='topmanager',
            name='dead_line',
            field=models.DateTimeField(verbose_name='Дедлайн для сотрудника'),
        ),
    ]
