# Generated by Django 4.2.7 on 2023-11-01 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicle',
            old_name='Identifier',
            new_name='vehicle_identifier',
        ),
    ]