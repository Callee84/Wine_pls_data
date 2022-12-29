import datetime
from django.db import models
from django.db.models.signals import post_save
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


class Wine(models.Model):
    wine_type_choices = [
        ('Red wine', 'Red wine'),
        ('White wine', 'White wine'),
        ('Sparkling wine', 'Sparkling wine'),
        ('Other', 'Other')
    ]
    rating_chioce = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]
    # model for adding wine
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default='id')
    name = models.CharField(max_length=300)
    vintage = models.PositiveIntegerField(
        default=current_year(), validators=[MinValueValidator(1900),
                                            max_value_current_year])
    producer = models.CharField(max_length=300)
    grapes = models.CharField(max_length=255, blank=True)
    tasting_day = models.DateField(null=True, blank=True)
    about = models.TextField(blank=True)
    wine_type_choice = models.CharField(
        max_length=45, choices=wine_type_choices, default='Red wine'
    )
    img = models.ImageField(
        upload_to='images/', default='../default_wine_b693ou'
    )
    rating = models.CharField(
        max_length=5, choices=rating_chioce, default='Rate your wine')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name} {self.vintage}"
