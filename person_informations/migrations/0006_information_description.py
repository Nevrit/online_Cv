# Generated by Django 4.2.11 on 2024-03-25 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person_informations', '0005_rename_first_name_contact_firstname'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='description',
            field=models.CharField(blank=True, default='', max_length=1000, verbose_name='A propos de moi'),
        ),
    ]
