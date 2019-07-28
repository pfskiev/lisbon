from django import template

register = template.Library()


def smart_truncate(content, length=100, suffix='...'):
    if len(content) <= length:
        return content
    else:
        return ' '.join(content[:length + 1].split(' ')[0:-1]) + suffix


@register.simple_tag()
def get_translated_description(news, lang):
    if 'en' in lang:
        return smart_truncate(news.description_EN, 300)

    if 'pt' in lang:
        return smart_truncate(news.description_PT, 300)

    if 'de' in lang:
        return smart_truncate(news.description_DE, 300)
