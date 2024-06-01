import re
from django import forms
from apps.servicos.models import TipoServico

class FormTipoServicos(forms.ModelForm):
    
    class Meta:
        model = TipoServico
        fields = '__all__'

    def clean_valor(self):
        valor = self.cleaned_data['valor']
        # Aqui, 'valor' já deve ser um decimal, mas você pode adicionar validações adicionais
        return valor
    
    def validar_numero(valor):
        pattern = r'^[0-9]+(\.[0-9]{1,})?$'
        if not re.match(pattern, valor):
            raise forms.ValidationError('O número está no formato incorreto.')