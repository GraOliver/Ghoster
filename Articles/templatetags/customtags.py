from django import template
from django.template.defaultfilters import stringfilter
from Accounts import models
register=template.Library()

@register.filter(name="get_image")
@register.simple_tag
def get_image(value):
    
    """ cette tags nous permet de trouver la photo par utilisateur
        
    Returns:
        _type_: _description_
    """
    images = models.User.objects.get(username=value)
    if images.profile_photo and hasattr(images.profile_photo,'url'):
        return images.profile_photo.url
    else :
        return "/static/Accounts/assetes/default_profile.png"

@register.filter(name="article_filtre")
@stringfilter
def article_filtre(value):
    for i in value :
        return i[0]
