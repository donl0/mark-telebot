# Generated by Django 3.2.7 on 2021-12-05 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BotShell', '0017_mailing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allemployment',
            name='role',
        ),
    ]
