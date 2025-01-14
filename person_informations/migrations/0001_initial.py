# Generated by Django 4.2.11 on 2024-03-22 11:54

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExpertiseFramework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Nom du langage')),
                ('icon', models.CharField(max_length=50, verbose_name="Classe de l'icône FontAwesome")),
                ('percentage_value', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36), (37, 37), (38, 38), (39, 39), (40, 40), (41, 41), (42, 42), (43, 43), (44, 44), (45, 45), (46, 46), (47, 47), (48, 48), (49, 49), (50, 50), (51, 51), (52, 52), (53, 53), (54, 54), (55, 55), (56, 56), (57, 57), (58, 58), (59, 59), (60, 60), (61, 61), (62, 62), (63, 63), (64, 64), (65, 65), (66, 66), (67, 67), (68, 68), (69, 69), (70, 70), (71, 71), (72, 72), (73, 73), (74, 74), (75, 75), (76, 76), (77, 77), (78, 78), (79, 79), (80, 80), (81, 81), (82, 82), (83, 83), (84, 84), (85, 85), (86, 86), (87, 87), (88, 88), (89, 89), (90, 90), (91, 91), (92, 92), (93, 93), (94, 94), (95, 95), (96, 96), (97, 97), (98, 98), (99, 99), (100, 100)], default=0, verbose_name='Niveau de connaisance')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExpertiseLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Nom du langage')),
                ('icon', models.CharField(max_length=50, verbose_name="Classe de l'icône FontAwesome")),
                ('percentage_value', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36), (37, 37), (38, 38), (39, 39), (40, 40), (41, 41), (42, 42), (43, 43), (44, 44), (45, 45), (46, 46), (47, 47), (48, 48), (49, 49), (50, 50), (51, 51), (52, 52), (53, 53), (54, 54), (55, 55), (56, 56), (57, 57), (58, 58), (59, 59), (60, 60), (61, 61), (62, 62), (63, 63), (64, 64), (65, 65), (66, 66), (67, 67), (68, 68), (69, 69), (70, 70), (71, 71), (72, 72), (73, 73), (74, 74), (75, 75), (76, 76), (77, 77), (78, 78), (79, 79), (80, 80), (81, 81), (82, 82), (83, 83), (84, 84), (85, 85), (86, 86), (87, 87), (88, 88), (89, 89), (90, 90), (91, 91), (92, 92), (93, 93), (94, 94), (95, 95), (96, 96), (97, 97), (98, 98), (99, 99), (100, 100)], default=0, verbose_name='Niveau de connaisance')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Langage Informatique',
                'verbose_name_plural': 'Langage Informatique',
            },
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nom')),
                ('last_name', models.CharField(max_length=150, verbose_name='Prénom')),
                ('image', models.ImageField(upload_to='pics_on_myself/')),
                ('birthdate', models.DateField(verbose_name="Date d'anniversaire")),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Numéro de téléphone')),
                ('address', models.CharField(max_length=100, verbose_name='Adresse')),
                ('degree', models.CharField(choices=[('BAC', 'Baccalauréat'), ('BAC+2', 'Brevet de Technicien Supérieur'), ('BAC+3', 'license'), ('BAC+5', 'master'), ('BAC+8', 'doctorat')], default='BAC', max_length=50)),
                ('year_of_graduation', models.DateField(verbose_name="Date de l'obtention du diplôme")),
                ('institution', models.CharField(max_length=100, verbose_name="Nom de l'école")),
                ('position', models.CharField(max_length=100, verbose_name='Titre du poste occupé')),
                ('company', models.CharField(max_length=100, verbose_name='Nom de la société')),
                ('hiring_date', models.DateField(verbose_name="Date d'embauche")),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Information Personnelles',
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('card_image', models.ImageField(upload_to='portfolio/', verbose_name='Image de la card')),
                ('card_title', models.CharField(max_length=50, verbose_name='Titre')),
                ('description', models.TextField(max_length=300, verbose_name='Description')),
                ('href', models.CharField(help_text='Le lien que vous mettrez ici devra être le même que le id', max_length=50, verbose_name='Le lien')),
                ('id', models.CharField(help_text='Le id que vous mettrez ici devra être unique', max_length=50, primary_key=True, serialize=False, unique=True, verbose_name='id')),
                ('aria_labelledby', models.CharField(blank=True, editable=False, max_length=100, verbose_name='aria-labelledby')),
                ('carousel_image', models.ImageField(upload_to='carousel_portfolio_images/', verbose_name='images de la carousselle')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CarouselPortfolioImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='galery/', verbose_name='Image')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('portfolio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='person_informations.portfolio')),
            ],
        ),
    ]
