from django.db import models

# Create your models here.

class Play(models.Model):
    # What the user provides in a post:
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField()

    # Database will automatically add date and timestamp
    date = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.title