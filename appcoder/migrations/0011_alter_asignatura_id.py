# Generated by Django 4.0.3 on 2022-03-30 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcoder', '0010_rename_entregado_extasis_aprobado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignatura',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]