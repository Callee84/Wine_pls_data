from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from wines.models import Wine


class Comment(models.Model):
    # Model for making a comment on a post
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.comment


class CommentWine(models.Model):
    # Model for making a comment on a wine
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    wine = models.ForeignKey(Wine, on_delete=models.CASCADE)
    comment_wine = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.comment_wine
