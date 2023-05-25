from django import forms 
from .models import comida

class FormularioComidas(forms.ModelForm): 
    class Meta: 
        model= comida 
        fields='__all__' 
