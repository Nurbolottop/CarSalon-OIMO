# Generated by Django 4.1.1 on 2022-10-08 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='photo_1',
        ),
        migrations.RemoveField(
            model_name='info',
            name='photo_2',
        ),
        migrations.RemoveField(
            model_name='info',
            name='photo_3',
        ),
    ]
