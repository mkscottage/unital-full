# Generated by Django 2.1.7 on 2019-05-06 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='organisor',
        ),
        migrations.DeleteModel(
            name='Exam',
        ),
    ]
