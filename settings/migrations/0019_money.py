# Generated by Django 4.1.1 on 2022-10-21 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0018_rename_email_con2_settings_email_site_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Money',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Kyrgyzstan', models.ImageField(upload_to='money/')),
                ('Kazahstan', models.ImageField(upload_to='money/')),
                ('Russia', models.ImageField(upload_to='money/')),
                ('USA', models.ImageField(upload_to='money/')),
                ('name', models.CharField(max_length=255)),
                ('Uzbekiston', models.ImageField(upload_to='money/')),
            ],
            options={
                'verbose_name': 'Валюты',
                'verbose_name_plural': 'Валюта',
            },
        ),
    ]