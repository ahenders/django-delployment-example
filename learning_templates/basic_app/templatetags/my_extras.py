from django import template

register = template.Library()

@register.filter(name='our_cut')
def our_cut(value, arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg, '')

# register.filter('our_cut',our_cut)
