# Generated by Django 3.2.16 on 2023-01-03 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='winepal',
            old_name='img',
            new_name='profile_image',
        ),
    ]