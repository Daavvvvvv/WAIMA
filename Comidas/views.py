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