# Generated by Django 4.2.1 on 2023-06-24 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_blog', '0002_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='review',
            field=models.CharField(default='', max_length=1000),
        ),
    ]