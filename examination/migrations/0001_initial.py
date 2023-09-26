# Generated by Django 4.2.1 on 2023-06-13 06:35

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_profiles', '0001_initial'),
        ('Faculties', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theory',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=1000000000000, primary_key=True, serialize=False)),
                ('question', tinymce.models.HTMLField()),
                ('ans', tinymce.models.HTMLField()),
                ('explanation', tinymce.models.HTMLField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Faculties.courses')),
            ],
        ),
        migrations.CreateModel(
            name='Objectives',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=1000000000000, primary_key=True, serialize=False)),
                ('question', tinymce.models.HTMLField()),
                ('op1', tinymce.models.HTMLField()),
                ('op2', tinymce.models.HTMLField()),
                ('op3', tinymce.models.HTMLField()),
                ('op4', tinymce.models.HTMLField()),
                ('c', models.CharField(default='', max_length=100)),
                ('correct_option', models.CharField(choices=[('a', 'a'), ('b', 'b'), ('c', 'c'), ('d', 'd')], max_length=1000000)),
                ('explanation', tinymce.models.HTMLField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Faculties.courses')),
            ],
        ),
        migrations.CreateModel(
            name='CommentTheory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now, max_length=100)),
                ('content', tinymce.models.HTMLField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Theory_Questions', to='examination.theory')),
                ('user_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_profiles.userprofile')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='CommentObjective',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now, max_length=100)),
                ('content', tinymce.models.HTMLField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Objectives_Questions', to='examination.objectives')),
                ('user_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_profiles.userprofile')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]
