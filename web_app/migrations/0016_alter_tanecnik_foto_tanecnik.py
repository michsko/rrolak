# Generated by Django 4.2.2 on 2023-06-27 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0015_alter_tanecnik_zdravotni_prohlidka_potvr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tanecnik',
            name='foto_tanecnik',
            field=models.ImageField(default='foto_tanecnik/pic.jpg', upload_to='foto_tanecnik', verbose_name='Fotografie'),
        ),
    ]
