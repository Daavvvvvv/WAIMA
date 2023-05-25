<<<<<<< HEAD
from django.db import models
from django import forms
# Create your models here.
class comida(models.Model):
    producto = models.TextField(max_length=50)
    descripcion = models.TextField(max_length=5000)
    peso= models.IntegerField(max_length=100)
    informacion = models.TextField(max_length=4000)
    
    def _str_(self):
        return self.producto 

=======
from django.db import models
from django import forms
# Create your models here.
class comida(models.Model):
    producto = models.TextField(max_length=50)
    descripcion = models.TextField(max_length=5000)
    peso= models.IntegerField(max_length=100)
    informacion = models.TextField(max_length=4000)
    
    def _str_(self):
        return self.producto 

>>>>>>> 22ccbe2 (se avanza en comidas)
