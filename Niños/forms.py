<<<<<<< HEAD
<<<<<<< HEAD
from django import forms 
from .models import Niños_tabla2  

class FormularioNiños(forms.ModelForm): 
    class Meta: 
        model= Niños_tabla2 
        fields='__all__' 
        widgets={'fechaDeNacimiento': forms.DateInput(attrs={'type':'date'})}
=======
from django import forms 
from .models import Niños_tabla2  

class FormularioNiños(forms.ModelForm): 
    class Meta: 
        model= Niños_tabla2 
        fields='__all__' 
        widgets={'fechaDeNacimiento': forms.DateInput(attrs={'type':'date'})}
>>>>>>> 22ccbe2 (se avanza en comidas)
=======
from django import forms 
from .models import Niños_tabla2  

class FormularioNiños(forms.ModelForm): 
    class Meta: 
        model= Niños_tabla2 
        fields='__all__' 
        widgets={'fechaDeNacimiento': forms.DateInput(attrs={'type':'date'})}
>>>>>>> 651dabb795813a6afaad9cb5ddf0a630dfa85e34
