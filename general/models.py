from django.db import models
from django.contrib.auth.models import User


class BlogModel(models.Model):
    name = models.CharField(max_length=150)
    title = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"
    
