from django.contrib import admin

# Register your models here.
from .models import Departameto,Computadora,Invetario

class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre','cantidad_pc')
    search_fields = ('nombre',)
    
class ComputadoraAdmin(admin.ModelAdmin):
    list_display = ('componente_pc','num_inventario','marca','estado','numero_pc')
    search_fields = ('num_invetario',)


class InventarioAdmin(admin.ModelAdmin):
    list_display = ('departamento','pc','fecha')
    search_fields = ('departamento',)

admin.site.register(Departameto,DepartamentoAdmin)
admin.site.register(Computadora,ComputadoraAdmin)
admin.site.register(Invetario,InventarioAdmin)
