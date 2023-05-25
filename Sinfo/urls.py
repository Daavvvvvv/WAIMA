<<<<<<< HEAD
<<<<<<< HEAD
from django.contrib import admin
from django.urls import path ,include
from Niños.views import FormularioNiñosView
#estas urs son de todo el proyecto en general, asi que vamos a haver un archivo urls.py para cada aplicacion y asi que cada una tenga sus urls
urlpatterns = [
    path('admin/', admin.site.urls),  
    #asi se enlazan las urls del pryecto con las de la app
    path('',include('Comedor.urls')), 
    #ya a la url se le debe agregar ProyectoWebApp/  
    path('Niños/',include('Niños.urls')), 
    ##path('',include('app2.urls')), 
    ##path('',include('app3.urls')), 
    path('Comidas/',include('Comidas.urls')), 
    path('registrarNiño/',FormularioNiñosView.index, name='registrarNiño'), 
    path('guardarNiño/', FormularioNiñosView.procesar_form, name= 'guardarNiño')

=======
from django.contrib import admin
from django.urls import path ,include
from Niños.views import FormularioNiñosView 
from Comidas.views import FormularioComidasView
#estas urs son de todo el proyecto en general, asi que vamos a haver un archivo urls.py para cada aplicacion y asi que cada una tenga sus urls
urlpatterns = [
    path('admin/', admin.site.urls),  
    #asi se enlazan las urls del pryecto con las de la app
    path('',include('Comedor.urls')), 
    #ya a la url se le debe agregar ProyectoWebApp/  
    path('Niños/',include('Niños.urls')), 
    ##path('',include('app2.urls')), 
    ##path('',include('app3.urls')), 
    path('Comidas/',include('Comidas.urls')), 
    path('registrarNiño/',FormularioNiñosView.index, name='registrarNiño'), 
    path('guardarNiño/', FormularioNiñosView.procesar_form, name= 'guardarNiño'), 
    path('listarNiño/', FormularioNiñosView.listar_Niños, name= 'listarNiño '), 
    path('registrarComidas/',FormularioComidasView.index, name='registrarComida'),  
    path('guardarComidas/', FormularioComidasView.procesar_form, name= 'guardarComidas'), 
    path('listarComidas/',FormularioComidasView.listar_Comidas, name='listarComida'), 
   


>>>>>>> 22ccbe2 (se avanza en comidas)
=======
from django.contrib import admin
from django.urls import path ,include
from Niños.views import FormularioNiñosView
#estas urs son de todo el proyecto en general, asi que vamos a haver un archivo urls.py para cada aplicacion y asi que cada una tenga sus urls
urlpatterns = [
    path('admin/', admin.site.urls),  
    #asi se enlazan las urls del pryecto con las de la app
    path('',include('Comedor.urls')), 
    #ya a la url se le debe agregar ProyectoWebApp/  
    path('Niños/',include('Niños.urls')), 
    ##path('',include('app2.urls')), 
    ##path('',include('app3.urls')), 
    path('Comidas/',include('Comidas.urls')), 
    path('registrarNiño/',FormularioNiñosView.index, name='registrarNiño'), 
    path('guardarNiño/', FormularioNiñosView.procesar_form, name= 'guardarNiño')

>>>>>>> 651dabb795813a6afaad9cb5ddf0a630dfa85e34
]