# Generated by Django 4.2.2 on 2023-07-11 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0055_tanecni_jednotka_jmeno_tanecnik15_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tanecni_jednotka',
            name='kategorie',
            field=models.CharField(choices=[('Děti', 'Kategorie Děti'), ('Žáci', 'Kategorie Žáci'), ('Junior', 'Kategorie Junior'), ('C', 'Kategorie C'), ('B', 'Kategorie B'), ('A', 'Kategorie A'), ('MDFD', 'Malá Dívčí Formace Děti'), ('MDFJ', 'Malá Dívčí Formace Junior'), ('MDFS', 'Malá Dívčí Formace Senior'), ('DFD', 'Dívčí Formace Děti'), ('DFJ', 'Dívčí Formace Junior'), ('DFS', 'Dívčí Formace Senior'), ('PFJ', 'Párová Formace Junior'), ('PFS', 'Párová Formace Senior'), ('DG', 'Duo Girls'), ('DL', 'Duo Ladies')], max_length=128, null=True, verbose_name='Kategorie'),
        ),
    ]