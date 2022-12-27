from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Post(models.Model):
    # model for creating posts
    wine_type_choices = [
        ('Red wine', 'Red wine'),
        ('White wine', 'White wine'),
        ('Sparkling wine', 'Sparkling wine'),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_ysqaze.jpg',
        blank=True
    )
    wine_type_choice = models.CharField(
        max_length=45, choices=wine_type_choices, default='Red wine'
    )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.id} | {self.title}'
