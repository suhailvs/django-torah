from django.db import models

class Line(models.Model):
    TITLES = (
        ('genesis', 'genesis'),
        ('exodus', 'exodus'),
        ('leviticus', 'leviticus'),
        ('numbers', 'numbers'),
        ('deuteronomy', 'deuteronomy')
    )
    title = models.CharField(max_length = 15,choices = TITLES)
    chapter = models.IntegerField()
    line = models.IntegerField()


class Word(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    lines = models.ManyToManyField(Line)


