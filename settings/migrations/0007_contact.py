# Generated by Django 4.1.1 on 2022-10-09 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0006_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_site', models.CharField(max_length=255)),
                ('phone_number_1', models.CharField(max_length=255)),
                ('phone_number_2', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Контакты',
                'verbose_name_plural': 'Контакты',
            },
        ),
    ]