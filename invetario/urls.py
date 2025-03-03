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
    path('departamentos/',views.listar_departamentos,name='listar_departamentos'),
    path('departamentos/crear/',views.crear_departamento,name='crear_departamento'),
    path('departamentos/editar/<int:pk>/',views.editar_departamento,name='editar_departamento'),
     path('departamentos/eliminar/<int:pk>/',views.eliminar_departamento,name='eliminar_departamento'),
]
