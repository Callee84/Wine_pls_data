# Generated by Django 3.2.16 on 2023-01-02 09:24

import django.core.validators
from django.db import migrations, models
import wines.models


class Migration(migrations.Migration):

    dependencies = [
        ('wines', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wine',
            name='vintage',
            field=models.PositiveIntegerField(default=2023, validators=[django.core.validators.MinValueValidator(1900), wines.models.max_value_current_year]),
        ),
    ]
