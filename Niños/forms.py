from django import forms 
from .models import Niños_tabla2  

class FormularioNiños(forms.ModelForm): 
    class Meta: 
        model= Niños_tabla2 
        fields='__all__' 
        widgets={'fechaDeNacimiento': forms.DateInput(attrs={'type':'date'})}
