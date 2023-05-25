from django.urls import path  
from Comedor import views 
from django.conf import settings 
from django.conf.urls.static import static
urlpatterns = [ 
    path('',views.Home,name="Home"), 
    
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)