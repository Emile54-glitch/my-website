from django.db import models

# Create your models here.
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()
    signature = models.CharField(max_length=140, default="Your Signature")

    def __str__(self):
        return self.title