# Generated by Django 3.2.7 on 2021-12-05 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BotShell', '0015_alter_manager_dead_line'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialist',
            name='dead_line',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дедлайн для сотрудника'),
        ),
        migrations.AlterField(
            model_name='topmanager',
            name='dead_line',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дедлайн для сотрудника'),
        ),
    ]
