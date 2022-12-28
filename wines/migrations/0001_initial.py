# Generated by Django 3.2.16 on 2022-12-28 19:35

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('producer', models.CharField(max_length=300)),
                ('year', models.DateField(blank=True, null=True)),
                ('about', models.TextField(blank=True)),
                ('wine_type_choice', models.CharField(choices=[('Red wine', 'Red wine'), ('White wine', 'White wine'), ('Sparkling wine', 'Sparkling wine'), ('Other', 'Other')], default='Red wine', max_length=45)),
                ('img', models.ImageField(default='../default_wine_b693ou', upload_to='images/')),
                ('rating', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('owner', models.ForeignKey(default='id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
