# Generated by Django 4.2.2 on 2023-06-27 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0012_alter_tanecnik_foto_tanecnik'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tanecnik',
            name='foto_tanecnik',
            field=models.ImageField(default='profile_pic.jpg', upload_to='foto_tanecnik', verbose_name='Fotografie'),
        ),
    ]