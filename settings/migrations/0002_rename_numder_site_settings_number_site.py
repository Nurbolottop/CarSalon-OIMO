# Generated by Django 4.1.1 on 2022-10-08 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='settings',
            old_name='numder_site',
            new_name='number_site',
        ),
    ]
