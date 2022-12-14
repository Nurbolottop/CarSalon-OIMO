# Generated by Django 4.1.1 on 2022-10-13 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0012_tiun'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='pro_desc',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='pro_model',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='pro_nal',
            field=models.CharField(default=0, max_length=55),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='pro_type',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='pro_volume',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='pro_year',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
