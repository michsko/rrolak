# Generated by Django 4.2.2 on 2023-06-28 13:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0017_tanecnik_datum_registrace_wrrc_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tanecnik',
            name='reg_try',
            field=models.DateField(null=True, verbose_name=datetime.datetime(2023, 6, 28, 13, 7, 59, 608799)),
        ),
        migrations.AlterField(
            model_name='tanecnik',
            name='datum_registrace',
            field=models.DateField(null=True, verbose_name=datetime.date(2023, 6, 28)),
        ),
        migrations.AlterField(
            model_name='tanecnik',
            name='registr_csar',
            field=models.BooleanField(default=False, null=True, verbose_name='Registrace csar'),
        ),
        migrations.AlterField(
            model_name='tanecnik',
            name='registrace_do',
            field=models.DateField(null=True, verbose_name=392),
        ),
    ]
