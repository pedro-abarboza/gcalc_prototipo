from django import template

register = template.Library()

@register.filter("get_coluna")
def get_coluna(obj, descricao):
    verba = obj.verbascalc_set.filter(descricao=descricao)
    return verba[0].total if verba else ""