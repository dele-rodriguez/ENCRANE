# Generated by Django 4.2.1 on 2023-06-25 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Faculties', '0002_remove_faculties_courses_remove_faculties_dept_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courses',
            options={'ordering': ['course']},
        ),
        migrations.AlterModelOptions(
            name='dept',
            options={'ordering': ['dept']},
        ),
        migrations.AlterModelOptions(
            name='faculties',
            options={'ordering': ['faculty']},
        ),
        migrations.RemoveField(
            model_name='courses',
            name='faculty',
        ),
    ]
