from django.shortcuts import render

# Create your views here.
def mostrar_agregar(request):
    tipo = request.session.get('tipo')
    estadoSesion = request.session.get('estadoSesion')
    if tipo and estadoSesion:
        if tipo == 'admin' or tipo == 'funcionario':
            return render(request, 'gestion_matriculas/agregar.html', {
                'tipo': tipo,
            })
        else:
            return render(request, 'menu_docente.html', {
                'r2': 'No tiene permisos para acceder a esta página'
            })
    else:
        return render(request, 'login.html', {
            'r2': 'Debe iniciar sesión'
        })


def mostrar_editar(request):
    tipo = request.session.get('tipo')
    estadoSesion = request.session.get('estadoSesion')
    if tipo and estadoSesion:
        if tipo == 'admin' or tipo == 'funcionario':
            return render(request, 'gestion_matriculas/editar.html', {
                'tipo': tipo,
            })
        else:
            return render(request, 'menu_docente.html', {
                'r2': 'No tiene permisos para acceder a esta página'
            })
    else:
        return render(request, 'login.html', {
            'r2': 'Debe iniciar sesión'
        })

def mostrar_eliminar(request):
    tipo = request.session.get('tipo')
    estadoSesion = request.session.get('estadoSesion')
    if tipo and estadoSesion:
        if tipo == 'admin' or tipo == 'funcionario':
            return render(request, 'gestion_matriculas/eliminar.html', {
                'tipo': tipo,
            })
        else:
            return render(request, 'menu_docente.html', {
                'r2': 'No tiene permisos para acceder a esta página'
            })
    else:
        return render(request, 'login.html', {
            'r2': 'Debe iniciar sesión'
        })

def mostrar_listado(request):
    tipo = request.session.get('tipo')
    estadoSesion = request.session.get('estadoSesion')
    if tipo and estadoSesion:
        if tipo == 'admin' or tipo == 'funcionario':
            return render(request, 'gestion_matriculas/listado.html', {
                'tipo': tipo,
            })
        else:
            return render(request, 'menu_docente.html', {
                'r2': 'No tiene permisos para acceder a esta página'
            })
    else:
        return render(request, 'login.html', {
            'r2': 'Debe iniciar sesión'
        })