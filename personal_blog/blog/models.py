from django.db import models
from django.contrib.auth.models import User  # We'll link posts to users

class Post(models.Model):
    title = models.CharField(max_length=200)  # Title of the post
    content = models.TextField()  # Content of the post
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when post is created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when post is last updated
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Link post to a user (author)

    def __str__(self):
        return self.title  # Shows title in admin panel

