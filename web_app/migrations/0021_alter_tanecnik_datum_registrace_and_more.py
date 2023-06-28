# Generated by Django 4.2.2 on 2023-06-28 13:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0020_remove_tanecnik_reg_try_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tanecnik',
            name='datum_registrace',
            field=models.DateField(blank=True, null=True, verbose_name=datetime.datetime(2023, 6, 28, 13, 33, 3, 670016)),
        ),
        migrations.AlterField(
            model_name='tanecnik',
            name='datum_registrace_wrrc',
            field=models.DateField(blank=True, null=True, verbose_name=datetime.datetime(2023, 6, 28, 13, 33, 3, 670047)),
        ),
        migrations.AlterField(
            model_name='tanecnik',
            name='datum_zavodni_registrace_csar',
            field=models.DateField(blank=True, null=True, verbose_name=datetime.datetime(2023, 6, 28, 13, 33, 3, 670034)),
        ),
    ]