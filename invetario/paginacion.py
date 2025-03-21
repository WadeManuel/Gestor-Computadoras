from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

def paga_Size(request):
    # Obtener el valor de page_size de la URL, con un valor por defecto de 10
    page_size = request.GET.get('page_size', '10')
    return page_size
    

def paginacion(request,lista):
    page_size=paga_Size(request)
    # Validar que page_size sea un número y que esté dentro del rango permitido
    try:
        page_size = int(page_size)
        if page_size > 100:
            page_size = 100  # Máximo 100 componentes por página
        elif page_size <= 0:
            page_size = 10 #Mínimo de 1 compoente pc por página
    except ValueError:
        page_size = 10  # Si no es un número, usar el valor por defecto
    paginator = Paginator(lista, page_size)  # Mostrar 10 componentes por página
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return page_obj
    
