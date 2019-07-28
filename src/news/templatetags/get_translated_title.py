from django import template

register = template.Library()


@register.simple_tag()
def get_translated_title(entity, lang):
    if 'en' in lang:
        return entity.title_EN

    if 'pt' in lang:
        return entity.title_PT

    if 'de' in lang:
        return entity.title_DE

