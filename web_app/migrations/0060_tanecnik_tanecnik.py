# Generated by Django 4.2.2 on 2023-07-15 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0059_tanecnik_odborny_dozor_tanecnik_porotce_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tanecnik',
            name='tanecnik',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Tanečník'),
        ),
    ]
