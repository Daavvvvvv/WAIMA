<<<<<<< HEAD
<<<<<<< HEAD
from django.shortcuts import render
from django.http import HttpRequest 
from .forms import FormularioNiños
# Create your views here.
"""def app1_vista(request): 
    return render(request,'niños.html') 
""" 
class FormularioNiñosView(HttpRequest):  
    def index(request):
        Niños=FormularioNiños() 
        return render (request,"NiñosIndex.html",{"form":Niños}) 
    
    def procesar_form(request): 
        Niños=FormularioNiños(request.POST) 
        if Niños.is_valid(): 
            Niños.save() 
            Niños=FormularioNiños() 
        return render(request, "NiñosIndex.html",{"form":Niños, "mensaje":'OK'})
=======
from django.shortcuts import render
from django.http import HttpRequest 
from .forms import FormularioNiños 
from .models import Niños_tabla2
# Create your views here.
"""def app1_vista(request): 
    return render(request,'niños.html') 
""" 
class FormularioNiñosView(HttpRequest):  
    def index(request):
        Niños=FormularioNiños() 
        return render (request,"NiñosIndex.html",{"form":Niños}) 
    
    def procesar_form(request): 
        Niños=FormularioNiños(request.POST) 
        if Niños.is_valid(): 
            Niños.save() 
            Niños=FormularioNiños() 
        return render(request, "NiñosIndex.html",{"form":Niños, "mensaje":'OK'}) 
    
    def listar_Niños(request): 
        Niños=Niños_tabla2.objects.all() 
        return render(request, "NiñosLista.html",{"Niños":Niños}) 
    
    """def editar(request, nombre): 
        Niños=Niños.objects.filter(nombre=nombre).first() 
        FormularioNiños(instance=Niños) 
        return render (request,"NiñoEdit.html",{"form":form, 'Niños':Niños}) 
        """
>>>>>>> 22ccbe2 (se avanza en comidas)
=======
from django.shortcuts import render
from django.http import HttpRequest 
from .forms import FormularioNiños
# Create your views here.
"""def app1_vista(request): 
    return render(request,'niños.html') 
""" 
class FormularioNiñosView(HttpRequest):  
    def index(request):
        Niños=FormularioNiños() 
        return render (request,"NiñosIndex.html",{"form":Niños}) 
    
    def procesar_form(request): 
        Niños=FormularioNiños(request.POST) 
        if Niños.is_valid(): 
            Niños.save() 
            Niños=FormularioNiños() 
        return render(request, "NiñosIndex.html",{"form":Niños, "mensaje":'OK'})
>>>>>>> 651dabb795813a6afaad9cb5ddf0a630dfa85e34
