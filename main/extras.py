from django import template
register = template.Library()

@register.filter(name='cut')
def cut(value):
    return value - 100

@register.filter(name='cei')
def compute_exact_id(value, rb_page_no):    
    new_id = value+(5*(rb_page_no-1))    ## here's the mathematical operation
    return new_id