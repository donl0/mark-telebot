# Generated by Django 3.2.7 on 2021-12-16 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BotShell', '0019_alter_allemployment_phone_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='all_employers',
            field=models.ManyToManyField(blank=True, related_name='all_employee_manager', to='BotShell.AllEmployment', verbose_name='Все подчинённые\n(Заполняется автоматически)'),
        ),
        migrations.AddField(
            model_name='topmanager',
            name='all_employers',
            field=models.ManyToManyField(blank=True, related_name='all_employee_top_manager', to='BotShell.AllEmployment', verbose_name='Все подчинённые\n(Заполняется автоматически)'),
        ),
    ]
