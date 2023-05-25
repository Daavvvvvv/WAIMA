<<<<<<< HEAD
from django.db import models

# Create your models here.

class Niños_tabla(models.Model):
    nombre = models.TextField(max_length=100)
    fechaDeNacimiento1 = models.DateField()
    peso= models.IntegerField(max_length=100)
    edad= models.IntegerField(max_length=100)
    infoTalla = models.TextField(max_length=4000)
    
    def _str_(self):
        return self.nombre 
    

class Niños_tabla2(models.Model):
    nombre = models.TextField(max_length=100)
    fechaDeNacimiento = models.DateField()
    peso = models.IntegerField(max_length=100)
    edad = models.IntegerField(max_length=100)
    infoTalla = models.TextField(max_length=4000)
    
    def _str_(self):
=======
from django.db import models

# Create your models here.

class Niños_tabla(models.Model):
    nombre = models.TextField(max_length=100)
    fechaDeNacimiento1 = models.DateField()
    peso= models.IntegerField(max_length=100)
    edad= models.IntegerField(max_length=100)
    infoTalla = models.TextField(max_length=4000)
    
    def _str_(self):
        return self.nombre 
    

class Niños_tabla2(models.Model):
    nombre = models.TextField(max_length=100)
    fechaDeNacimiento = models.DateField()
    peso = models.IntegerField(max_length=100)
    edad = models.IntegerField(max_length=100)
    infoTalla = models.TextField(max_length=4000)
    
    def _str_(self):
>>>>>>> 22ccbe2 (se avanza en comidas)
        return self.nombre