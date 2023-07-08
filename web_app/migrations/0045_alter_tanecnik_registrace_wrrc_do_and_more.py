# Generated by Django 4.2.1 on 2023-07-08 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0044_alter_tanecnik_zdravotni_prohlidka_potvr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tanecnik',
            name='registrace_wrrc_do',
            field=models.DateField(blank=True, null=True, verbose_name=372),
        ),
        migrations.AlterField(
            model_name='tanecnik',
            name='zdravotni_prohlidka_potvr',
            field=models.FileField(upload_to='zdravotni_prohlidka/', verbose_name='Zdravotní prohlídka'),
        ),
    ]