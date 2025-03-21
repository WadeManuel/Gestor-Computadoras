from django.db import models

# Create your models here.

    
class Departameto(models.Model):
    nombre = models.CharField(max_length=255,blank=False,unique=True)
    cantidad_pc = models.IntegerField(null=False,blank=False)
    
    def __str__(self):
        return self.nombre
class Meta:
        ordering = [ " name " ]

class Computadora(models.Model):
    componente_pc = models.CharField(max_length=155,blank=False) 
    num_inventario = models.IntegerField(null=False,blank=False)
    marca = models.CharField(max_length=155,blank=False)
    estado = models.CharField(max_length=10,blank=False)
    numero_pc = models.IntegerField(null=False,blank=False)
    departamento = models.ForeignKey(Departameto,on_delete=models.CASCADE)
    
class Meta:
        ordering = [ " numero_pc " ]

class MemoriaRam(models.Model):
    clasificacion=models.CharField(max_length=4,blank=False)
    capacidad=models.IntegerField(null=False,blank=False)
    marca = models.CharField(max_length=155,blank=False)
    velocidad=models.IntegerField(null=False,blank=False)

class Discos(models.Model):
    clasificacion=models.CharField(max_length=255,blank=False)
    capacidad=models.IntegerField(null=False,blank=False)
    marca = models.CharField(max_length=155,blank=False)
    serie=models.CharField(max_length=255,blank=False,unique=True)

class LectorCD_DVD(models.Model):
    clasificacion=models.CharField(max_length=255,blank=False)
    marca = models.CharField(max_length=155,blank=False)

class Propiedad(models.Model):
    procesador=models.CharField(max_length=255,blank=False)
    lista_memorias_ram=models.ManyToManyField(MemoriaRam)
    lista_discos_duros=models.ManyToManyField(Discos)
    gpu=models.CharField(max_length=255,blank=True)
    lector=models.ForeignKey(LectorCD_DVD,on_delete=models.CASCADE)
    computadora=models.ForeignKey(Computadora,on_delete=models.CASCADE)
        
class Mensajes(models.Model):
    nombre=models.CharField(max_length=255,blank=False)
    email=models.EmailField(max_length=255,blank=False,unique=True)
    mensaje=models.TextField(max_length=300)
    
    
    
