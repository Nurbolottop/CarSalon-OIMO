# Generated by Django 4.1.1 on 2022-10-10 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0011_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tiun',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiun_photo', models.ImageField(upload_to='', verbose_name='tiun/')),
            ],
        ),
    ]
