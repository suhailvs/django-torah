from django import template
register = template.Library()

@register.filter(name='get_index')
def get_index(l, arg):
    """
    Get the index of an array
    eg: 
    input : 'suhaile','e'
    output: 7
    """
    # if arg==' ':
    #     v = '_'
    # else:
    #     v = l.index(arg)+1
    return l.index(arg)+1 #v

@register.filter(name='get_icomoon')
def get_icomoon(l,arg):
    """
    Get Unicode of a string
    eg: 
    input : 's'
    output: "\U00000394"
    """
    
    return '<span class="icon-%d"></span>'%(l.index(arg)+1,)
