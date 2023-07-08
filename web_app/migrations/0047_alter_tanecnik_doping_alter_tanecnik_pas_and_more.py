# Generated by Django 4.2.1 on 2023-07-08 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0046_alter_tanecnik_doping_alter_tanecnik_pas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tanecnik',
            name='doping',
            field=models.FileField(null=True, upload_to='dopingove_prohlaseni', verbose_name='Dopingove prohlašení'),
        ),
        migrations.AlterField(
            model_name='tanecnik',
            name='pas',
            field=models.FileField(null=True, upload_to='kopie_pasu', verbose_name='Kopie pasu'),
        ),
        migrations.AlterField(
            model_name='tanecnik',
            name='zdravotni_prohlidka_potvr',
            field=models.FileField(null=True, upload_to='zdravotni_prohlidka/', verbose_name='Zdravotní prohlídka'),
        ),
    ]