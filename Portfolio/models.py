# making database fields

import email
from typing import Any
from typing_extensions import Required
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from numpy import require
from sqlalchemy import true

# Create your models here.


class Contact(models.Model):
    your_name = models.CharField(max_length=50)
    your_email = models.EmailField()
    subject = models.CharField(max_length=50)  # title length
    content = models.TextField()									# content field
    # update date on creating the post
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
