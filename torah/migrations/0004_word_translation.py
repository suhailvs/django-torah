# Generated by Django 2.1.3 on 2018-11-22 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torah', '0003_word_lines'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='translation',
            field=models.CharField(default='', max_length=200),
        ),
    ]
