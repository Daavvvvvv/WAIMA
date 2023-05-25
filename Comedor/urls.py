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
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)