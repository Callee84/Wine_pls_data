from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from wines.models import Wine


class Likes(models.Model):
    # model for liking posts and wine
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='likes', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f'{self.owner} | {self.post}'


class LikesWine(models.Model):
    # model for liking posts and wine
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    wine = models.ForeignKey(
        Wine, related_name='likes', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']
        unique_together = ['owner', 'wine']

    def __str__(self):
        return f'{self.wine} | {self.owner}'
