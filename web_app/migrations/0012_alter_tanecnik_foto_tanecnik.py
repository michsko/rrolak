# Generated by Django 4.2.2 on 2023-06-27 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0011_alter_tanecnik_doping_alter_tanecnik_foto_tanecnik_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tanecnik',
            name='foto_tanecnik',
            field=models.ImageField(default='foto_tanecnik/profile_pic.jpg', upload_to='foto_tanecnik', verbose_name='Fotografie'),
        ),
    ]