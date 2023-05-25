<<<<<<< HEAD
from django.urls import path  
from . import views 
from django.conf import settings 
from django.conf.urls.static import static 
from .views import FormularioNiñosView  

urlpatterns = [ 

    path('registrarNiño/',FormularioNiñosView.index, name='registrarNiño'),
]
=======
from django.urls import path  
from . import views 
from django.conf import settings 
from django.conf.urls.static import static 
from .views import FormularioNiñosView  

urlpatterns = [ 

    path('registrarNiño/',FormularioNiñosView.index, name='registrarNiño'), 
    path('listarNiños/',FormularioNiñosView.index, name='listarNiño'),
    
]
>>>>>>> 22ccbe2 (se avanza en comidas)
