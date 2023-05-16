from django.db import models
from baselayer.basemodel import LogsMixin
from django.contrib.auth.models import User
# Create your models here.

class Post(LogsMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    description = models.TextField()
