from django import template

register = template.Library()


@register.simple_tag
def get_widget(wro, **kwargs):
    return wro.get_widget(**kwargs)
