# Generated by Django 4.2.2 on 2023-07-05 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0034_remove_prihlaska_zavod_soutez_prihlaska_zavod_zavod_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prihlaska_zavod',
            name='zavod',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='prihlaseni', to='web_app.zavod'),
        ),
    ]