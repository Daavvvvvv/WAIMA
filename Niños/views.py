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