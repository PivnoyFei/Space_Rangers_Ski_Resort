# Generated by Django 3.2.15 on 2022-10-17 09:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ski_resort', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ski',
            name='data_today',
            field=models.DateField(default=datetime.datetime(3022, 10, 17, 12, 8, 21, 614482), verbose_name='Сегодняшний день'),
        ),
    ]
