<<<<<<< HEAD
<<<<<<< HEAD
from django.shortcuts import render


# Create your views here.
def app3_vista(request): 
    return render(request,'comidas.html') 

def agregarComida(request, idComida, idDieta):
    dietaID = None
    for i in dietas:
        nombreDieta = str(i.nombre)
        if nombreDieta == idDieta:
            dietaID = i.id
            break
    objDieta = dieta.objects.get(id=dietaID)
    objComida = comida.objects.get(id=idComida)
    CDInstance = comidaDieta.objects.create(comida=objComida,dieta=objDieta)
    CDInstance.save()
    return render(request, 'comidaAgregada.html', {})
=======
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpRequest 
from .forms import FormularioComidas 
from .models import comida

# Create your views here.
class FormularioComidasView(HttpRequest):  
    def index(request):
        Comidas=FormularioComidas() 
        return render (request,"ComidasIndex.html",{"form":Comidas}) 
    
    def procesar_form(request): 
        Comidas=FormularioComidas(request.POST) 
        if Comidas.is_valid(): 
            Comidas.save() 
            Comidas=FormularioComidas() 
        return render(request, "ComidasIndex.html",{"form":Comidas, "mensaje":'OK'}) 
    
    def listar_Comidas(request): 
        Comidas=comida.objects.all() 
        return render(request, "ComLista.html",{"Comidas":Comidas}) 
    
>>>>>>> 22ccbe2 (se avanza en comidas)
=======
from django.shortcuts import render


# Create your views here.
def app3_vista(request): 
    return render(request,'comidas.html') 

def agregarComida(request, idComida, idDieta):
    dietaID = None
    for i in dietas:
        nombreDieta = str(i.nombre)
        if nombreDieta == idDieta:
            dietaID = i.id
            break
    objDieta = dieta.objects.get(id=dietaID)
    objComida = comida.objects.get(id=idComida)
    CDInstance = comidaDieta.objects.create(comida=objComida,dieta=objDieta)
    CDInstance.save()
    return render(request, 'comidaAgregada.html', {})
>>>>>>> 651dabb795813a6afaad9cb5ddf0a630dfa85e34
