# Generated by Django 3.2.7 on 2021-12-16 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BotShell', '0022_alter_topmanager_all_employers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topmanager',
            name='all_employers',
            field=models.CharField(blank=True, default='', max_length=10000, verbose_name='Все подчиненные'),
        ),
    ]
