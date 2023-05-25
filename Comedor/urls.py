<<<<<<< HEAD
<<<<<<< HEAD
from django.urls import path  
from Comedor import views 
from django.conf import settings 
from django.conf.urls.static import static
urlpatterns = [ 
    path('',views.Home,name="Home"), 
    
]

if settings.DEBUG is True:
=======
from django.urls import path  
from Comedor import views 
from django.conf import settings 
from django.conf.urls.static import static
urlpatterns = [ 
    path('',views.Home,name="Home"), 
    
]

if settings.DEBUG is True:
>>>>>>> 22ccbe2 (se avanza en comidas)
=======
from django.urls import path  
from Comedor import views 
from django.conf import settings 
from django.conf.urls.static import static
urlpatterns = [ 
    path('',views.Home,name="Home"), 
    
]

if settings.DEBUG is True:
>>>>>>> 651dabb795813a6afaad9cb5ddf0a630dfa85e34
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)