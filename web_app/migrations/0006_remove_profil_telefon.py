# Generated by Django 4.2.2 on 2023-06-26 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0005_profil_email_alter_profil_telefon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profil',
            name='telefon',
        ),
    ]
