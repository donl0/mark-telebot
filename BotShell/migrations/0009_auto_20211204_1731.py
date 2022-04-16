# Generated by Django 3.2.7 on 2021-12-04 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BotShell', '0008_alter_allemployment_job_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeadLines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dead_line', models.DateTimeField(verbose_name='Дедлайн для какого-либо сотрудника')),
                ('make_to_all_this_deadline', models.BooleanField(default=False, verbose_name='Установить этот дедлайн всем сотрудникам?')),
            ],
        ),
        migrations.AddField(
            model_name='manager',
            name='dead_line',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='BotShell.deadlines', verbose_name='Дедлайн сотрудника'),
        ),
        migrations.AddField(
            model_name='specialist',
            name='dead_line',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='BotShell.deadlines', verbose_name='Дедлайн сотрудника'),
        ),
        migrations.AddField(
            model_name='topmanager',
            name='dead_line',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='BotShell.deadlines', verbose_name='Дедлайн сотрудника'),
        ),
    ]
