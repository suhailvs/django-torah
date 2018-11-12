from django.db import models


class Word(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()