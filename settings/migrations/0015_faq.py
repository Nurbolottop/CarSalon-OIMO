# Generated by Django 4.1.1 on 2022-10-21 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0014_products_pro_photo2_products_pro_photo3_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vopros', models.TextField()),
                ('otvet', models.TextField()),
            ],
            options={
                'verbose_name': 'Вопросы',
                'verbose_name_plural': 'Вопрос',
            },
        ),
    ]