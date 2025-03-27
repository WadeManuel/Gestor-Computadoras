from django.urls import path
from .import views 
from .views import ComputadorasPDFView,ComputadorasListWordView

urlpatterns = [
    path('',views.base,name='base'),
    path('computadoras/',views.listar_computadoras,name='listar_computadoras'),
    path('computadoras/pdf/',ComputadorasPDFView.as_view(),name='lista_pdf_computadoras'),
    path('computadoras/work/',ComputadorasListWordView.as_view(),name='lista_computadoras_work'),
    path('computadoras/crear/',views.crear_computadora,name='crear_computadora'),
    path('computadoras/editar/<int:pk>/',views.editar_computadora,name='editar_computadora'),
    path('computadoras/eliminar/<int:pk>/',views.eliminar_computadora,name='eliminar_computadora'),
    #Url para departamentos
    path('departamentos/',views.listar_departamentos,name='listar_departamentos'),
    path('departamentos/crear/',views.crear_departamento,name='crear_departamento'),
    path('departamentos/editar/<int:pk>/',views.editar_departamento,name='editar_departamento'),
    path('departamentos/eliminar/<int:pk>/',views.eliminar_departamento,name='eliminar_departamento'),
    #Url para Listas memorias Ram
    path('memorias/',views.listar_memorias_ram,name='listar_memorias_ram'),
    path('memorias/crear/',views.crear_memoria_ram,name='crear_memoria_ram'),
    path('memorias/editar/<int:pk>/',views.editar_memoria_ram,name='editar_memoria_ram'),
    path('memorias/eliminar/<int:pk>/',views.eliminar_memoria_ram,name='eliminar_memoria_ram'),
    #Url para Listas Discos
    path('discos/',views.listar_discos_duros,name='listar_discos_duros'),
    path('discos/crear/',views.crear_disco_duro,name='crear_disco_duro'),
    path('discos/editar/<int:pk>/',views.editar_disco_duro,name='editar_disco_duro'),
    path('discos/eliminar/<int:pk>/',views.eliminar_disco_duro,name='eliminar_disco_duro'),
     #Url para Listas Lectores 
    path('lectores/',views.listar_lectores,name='listar_lectores'),
    path('lectores/crear/',views.crear_lector,name='crear_lector'),
    path('lectores/editar/<int:pk>/',views.editar_lector,name='editar_lector'),
    path('lectores/eliminar/<int:pk>/',views.eliminar_lector,name='eliminar_lector'),
    #Url para propiedades
    path('propiedades/',views.listar_propiedades,name='listar_propiedades'),
    path('propiedades/crear/',views.crear_propiedad,name='crear_propiedad'),
    path('propiedades/editar/<int:pk>/',views.editar_propiedad,name='editar_propiedad'),
    path('propiedades/eliminar/<int:pk>/',views.eliminar_propiedad,name='eliminar_propiedad'),
    path('propiedades/ver/<int:pk>/',views.ver_propiedades,name='ver_propiedades'),
    
    
    
    
]
