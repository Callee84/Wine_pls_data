# Generated by Django 3.2.16 on 2022-12-29 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wines', '0006_alter_wine_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='wine',
            name='grapes',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
