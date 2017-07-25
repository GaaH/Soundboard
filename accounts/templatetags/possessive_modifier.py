from django import template

register = template.Library()

@register.assignment_tag(takes_context=True)
def possessive_modifier(context):
    request = context['request']
    user = context['user']
    return 'Mes' if request.user == user else 'Ses'
