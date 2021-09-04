from django.contrib import admin

# Register your models here.
from .models import Line, Word

admin.site.register(Line)
admin.site.register(Word)