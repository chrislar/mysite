from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post (models.model) :
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                        )
