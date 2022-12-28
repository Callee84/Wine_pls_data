from django.db import models
from django.db.models.signals import post_save
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


class Wine(models.Model):
    wine_type_choices = [
        ('Red wine', 'Red wine'),
        ('White wine', 'White wine'),
        ('Sparkling wine', 'Sparkling wine'),
        ('Other', 'Other')
    ]
    # model for adding wine
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default='id')
    name = models.CharField(max_length=300)
    producer = models.CharField(max_length=300)
    year = models.DateField(null=True, blank=True)
    about = models.TextField(blank=True)
    wine_type_choice = models.CharField(
        max_length=45, choices=wine_type_choices, default='Red wine'
    )
    img = models.ImageField(
        upload_to='images/', default='../default_wine_b693ou'
    )
    rating = models.IntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"
