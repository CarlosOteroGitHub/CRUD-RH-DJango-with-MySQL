# Generated by Django 3.2.8 on 2021-11-21 02:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RH', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empleado',
            old_name='id',
            new_name='id_empleado',
        ),
    ]