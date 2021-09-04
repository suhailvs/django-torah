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
    chapter_no = models.IntegerField()
    line_no = models.IntegerField()
    name = models.TextField()

    def __str__(self):
        return f'{self.title} {self.chapter_no}:{self.line_no}'


class Word(models.Model):
    name = models.CharField(max_length=200, unique=True) # paleo hebrew
    translation = models.CharField(max_length = 200, default="") # englis translation
    desc = models.TextField()
    lines = models.ManyToManyField(Line)

    def __str__(self):
        return self.name

