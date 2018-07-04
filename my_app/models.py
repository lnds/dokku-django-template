from django.contrib.auth.models import User
from django.db import models


class Demo(models.Model):
    text = models.TextField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
