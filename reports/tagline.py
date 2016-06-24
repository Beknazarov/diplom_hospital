from hospital import settings
@register.simple_tag
def media_root():
    return getattr(settings, 'MEDIA_ROOT', '/')
