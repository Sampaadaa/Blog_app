from django.db import models
from django.contrib.auth.models import User 
from tinymce.models import HTMLField

class Post(models.Model):
    title = models.CharField(max_length=100)
    description =HTMLField()
    image = models.ImageField(upload_to='post_images/', default="/post_images/blog.png")
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)
    

    def __str__(self):
        return self.title


