from django import template
register = template.Library()


@register.filter()
def get_conducteurs(conducteurs):
    print(conducteurs)
    return conducteurs