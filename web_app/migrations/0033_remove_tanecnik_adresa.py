# Generated by Django 4.2.1 on 2023-07-04 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0032_prihlaska_zavod_delete_prihlaska_soutez'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tanecnik',
            name='adresa',
        ),
    ]