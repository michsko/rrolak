# Generated by Django 4.2.2 on 2023-07-07 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0043_alter_tanecnik_foto_tanecnik'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tanecnik',
            name='zdravotni_prohlidka_potvr',
            field=models.FileField(upload_to='zdravotni_prohlidka', verbose_name='Zdravotní prohlídka'),
        ),
    ]
