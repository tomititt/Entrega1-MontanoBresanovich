# Generated by Django 4.0.3 on 2022-03-24 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appcoder', '0006_rename_estudiante_mago'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profesor',
            old_name='profesion',
            new_name='materia',
        ),
    ]
