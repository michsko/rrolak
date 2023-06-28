# Generated by Django 4.2.2 on 2023-06-28 08:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0016_alter_tanecnik_foto_tanecnik'),
    ]

    operations = [
        migrations.AddField(
            model_name='tanecnik',
            name='datum_registrace_wrrc',
            field=models.DateField(null=True, verbose_name=datetime.date(2023, 6, 28)),
        ),
        migrations.AddField(
            model_name='tanecnik',
            name='datum_zavodni_registrace_csar',
            field=models.DateField(null=True, verbose_name=datetime.date(2023, 6, 28)),
        ),
        migrations.AddField(
            model_name='tanecnik',
            name='registrace_wrrc_do',
            field=models.DateField(null=True, verbose_name=392),
        ),
        migrations.AddField(
            model_name='tanecnik',
            name='zavodni_registrace_do',
            field=models.DateField(null=True, verbose_name=392),
        ),
        migrations.AlterField(
            model_name='tanecnik',
            name='datum_registrace',
            field=models.DateField(verbose_name=datetime.date(2023, 6, 28)),
        ),
        migrations.AlterField(
            model_name='tanecnik',
            name='registr_wrrc',
            field=models.BooleanField(default=False, null=True, verbose_name='Registrace wrrc'),
        ),
        migrations.AlterField(
            model_name='tanecnik',
            name='registr_zavodni_csar',
            field=models.BooleanField(default=False, null=True, verbose_name='Zavodni registrace'),
        ),
        migrations.AlterField(
            model_name='tanecnik',
            name='registrace_do',
            field=models.DateField(verbose_name=392),
        ),
    ]