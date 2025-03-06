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

class Propiedad(models.Model):
    procesador=models.CharField(max_length=255,blank=False)
    memoria_ram=models.CharField(max_length=255,blank=False)
    disco=models.CharField(max_length=255,blank=False)
    gpu=models.CharField(max_length=255,blank=True)
    computadora=models.ForeignKey(Computadora,on_delete=models.CASCADE)
    
    
     

class Invetario(models.Model):
    departamento = models.ForeignKey(Departameto,on_delete=models.CASCADE)
    pc = models.ForeignKey(Computadora,on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    
    
    
