# Generated by Django 4.2.2 on 2023-06-26 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0006_remove_profil_telefon'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='telefon',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
