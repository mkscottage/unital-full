# Generated by Django 2.1.7 on 2019-04-22 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='for_college',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.College', verbose_name='Question For College'),
        ),
        migrations.AlterField(
            model_name='question',
            name='for_department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.Department', verbose_name='Question For Department'),
        ),
    ]
