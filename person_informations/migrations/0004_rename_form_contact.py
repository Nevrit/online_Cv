# Generated by Django 4.2.11 on 2024-03-25 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person_informations', '0003_alter_form_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Form',
            new_name='Contact',
        ),
    ]