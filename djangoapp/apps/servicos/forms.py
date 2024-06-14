import re
from django import forms
from apps.servicos.models import TipoServicos

class FormTipoServicos(forms.ModelForm):
    
    class Meta:
        model = TipoServicos
        fields = '__all__'


    def clean(self):
        cleaned_data = super().clean()
        valor = re.sub(r"[^\d\-,]","",self.data['valor']).replace(",",".")
        cleaned_data.update({'valor': float(valor)})
        return cleaned_data
    
    def validar_numero(valor):
        pattern = r'^[0-9]+(\.[0-9]{1,})?$'
        if not re.match(pattern, valor):
            raise forms.ValidationError('O número está no formato incorreto.')