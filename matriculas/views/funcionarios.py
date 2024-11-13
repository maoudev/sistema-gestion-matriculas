from django.shortcuts import render


def mostrar_agregar(request):
    return render(request, 'gestion_funcionarios/agregar.html')

def mostrar_editar(request):
    return render(request, 'gestion_funcionarios/editar.html')

def mostrar_eliminar(request):
    return render(request, 'gestion_funcionarios/eliminar.html')

def mostrar_listado(request):
    return render(request, 'gestion_funcionarios/listar.html')