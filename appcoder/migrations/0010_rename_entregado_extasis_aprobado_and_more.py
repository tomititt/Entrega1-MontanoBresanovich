# Generated by Django 4.0.3 on 2022-03-24 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appcoder', '0009_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='extasis',
            old_name='entregado',
            new_name='aprobado',
        ),
        migrations.RemoveField(
            model_name='extasis',
            name='fecha_entregado',
        ),
    ]
