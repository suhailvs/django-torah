from django import template
register = template.Library()

PATTERN = 'abgdefzhjiklmnxopsqrct'

@register.filter(name='get_letternumber')
def get_letternumber(letter):
    """
    Return Number curresponding to PaleoHebrew letter
    """
    return PATTERN.index(letter)+1

@register.filter(name='get_words')
def get_words(line):
    """
    Return list of words of given line
    """
    return line.split(' ')