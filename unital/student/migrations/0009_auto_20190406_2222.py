# Generated by Django 2.1.7 on 2019-04-06 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_languagesknown'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='academicqualification',
            options={'verbose_name_plural': '02. Academic Qualifications'},
        ),
        migrations.AlterModelOptions(
            name='hobbies',
            options={'verbose_name_plural': '06. Hobbies'},
        ),
        migrations.AlterModelOptions(
            name='internship',
            options={'verbose_name_plural': '08. Internships'},
        ),
        migrations.AlterModelOptions(
            name='languagesknown',
            options={'verbose_name_plural': '07. Languages Known'},
        ),
        migrations.AlterModelOptions(
            name='portfolio',
            options={'verbose_name_plural': '01. Portfolios'},
        ),
        migrations.AlterModelOptions(
            name='profilesummary',
            options={'verbose_name_plural': '05. Profile Summary'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name_plural': '09. Projects'},
        ),
        migrations.AlterModelOptions(
            name='skillset',
            options={'verbose_name_plural': '03. Skill Set'},
        ),
        migrations.AlterModelOptions(
            name='technicalskill',
            options={'verbose_name_plural': '04. Technical Skills'},
        ),
        migrations.AlterModelOptions(
            name='technologyused',
            options={'verbose_name_plural': '10. Technology Used (in project)'},
        ),
        migrations.AlterField(
            model_name='hobbies',
            name='portfolio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hobbies', to='student.Portfolio', verbose_name='Portfolio'),
        ),
        migrations.AlterField(
            model_name='languagesknown',
            name='portfolio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='languages_known', to='student.Portfolio', verbose_name='Portfolio'),
        ),
    ]
