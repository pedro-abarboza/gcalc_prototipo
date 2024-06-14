from django import template
from django.utils.translation import gettext as _

register = template.Library()

@register.filter("get_coluna")
def get_coluna(obj, descricao):
    verba = obj.verbascalc_set.filter(descricao=descricao)
    return verba[0].total if verba else ""

@register.filter("translate_name")
def translate_name(name):
    retorno=''
    for palavra in name.split(' '):
        retorno += _(palavra.lower())+" "
    return retorno.capitalize().strip()

@register.filter("translate_name_tm")
def translate_name(name):
    retorno=''
    for palavra in name.split(' '):
        retorno += _(palavra.lower()).capitalize()+" "
    return retorno.strip()