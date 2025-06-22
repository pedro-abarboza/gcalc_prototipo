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

@register.filter("translate_permission")
def translate_name(name):
    dict_translate = {
        'add': 'Adicionar',
        'change': 'Alterar',
        'delete': 'Excluir',
        'view': 'Visualizar',
        'list': 'Listar',
        'group' : 'Grupo',
        'permission': 'Permissão',
        'user': 'Usuário',
        'Can': '',
    }
    retorno=''
    for palavra in name.split(' '):
        if palavra in dict_translate:
            retorno += dict_translate[palavra]+" "
        else:
            retorno += palavra+" "
    return retorno.strip()