# Generated by Django 4.2.1 on 2023-07-08 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0052_alter_tanecnik_registrace_do_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tanecni_jednotka',
            name='jmeno_tanecnik13',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tanecnik15', to='web_app.tanecnik'),
        ),
        migrations.AlterField(
            model_name='tanecni_jednotka',
            name='jmeno_tanecnik14',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tanecnik16', to='web_app.tanecnik'),
        ),
    ]
