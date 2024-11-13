from django.shortcuts import render

from matriculas.models import Usuario
from matriculas.utils import check_password

def index(request):
    return render(request, 'index.html')

def login(request):
    try:
        if request.method == 'POST':
            nombre = request.POST["txtnom"]
            password = request.POST["txtpas"]

            usuario = Usuario.objects.filter(nombre=nombre).first()
            if usuario:
                if usuario.estado == False:
                    return render(request, 'login.html', {
                        'r2': 'Usuario bloqueado'
                    })
                
                if usuario.cantidad_intentos == 3:
                    usuario.estado = False
                    usuario.cantidad_intentos = 0
                    usuario.save()
                    return render(request, 'login.html', {
                        'r2': 'Usuario bloqueado'
                    })
                
                if check_password(password=password, hashed_password=usuario.password) == False:
                    usuario.cantidad_intentos += 1
                    usuario.save()
                    print('paso aqui')
                    return render(request, 'login.html', {
                        'r2': 'Nombre y/o contraseña incorrectos'
                    })
                
                usuario.cantidad_intentos = 0
                request.session['idUsuario'] = usuario.id
                request.session['nombre'] = usuario.nombre.upper()
                request.session['tipo'] = usuario.tipo
                request.session['estadoSesion'] = True

                if usuario.tipo == 'admin':
                    return render(request, 'menu_admin.html', {
                        "nombre": usuario.nombre.upper()
                    })
                
                if usuario.tipo == 'funcionario':
                    return render(request, 'menu_funcionarios.html', {
                        "nombre": usuario.nombre.upper()
                    })
                
                if usuario.tipo == 'docente':
                    return render(request, 'menu_docente.html', {
                        "nombre": usuario.nombre.upper()
                    })


            else:
                return render(request, 'login.html', {
                    'r2': 'Nombre y/o contraseña incorrectos'
                })

        elif request.method == 'GET':
            return render(request, 'login.html')

        else:
            return render(request, 'login.html', {
                'r2': 'No se pudo procesar la solicitud'
            })
        
    except Exception as e:
        print(e)
        return render(request, 'login.html', {
            'r2': 'Error al procesar la solicitud'
        })
    

def logout(request):
    try:
        del request.session['idUsuario']
        del request.session['nombre']
        del request.session['tipo']
        del request.session['estadoSesion']
        return render(request, 'login.html', {
            'r': 'Sesión cerrada exitosamente'
        })
    except:
        return render(request, 'login.html', {
            'r2': 'Error al procesar la solicitud'
        })
    

def menu_admin(request):
    tipo = request.session.get('tipo')
    nombre = request.session.get('nombre')
    estadoSesion = request.session.get('estadoSesion')
    if tipo and estadoSesion:
        if tipo == 'admin':
            return render(request, 'menu_admin.html', {
                'nombre': nombre,
            })
        elif tipo == 'funcionario':
            return render(request, 'menu_funcionarios.html', {
                'r2': 'No tiene permisos para acceder a esta página',
                'nombre': nombre,
            })
        elif tipo == 'docente':
            return render(request, 'menu_docente.html', {
                'r2': 'No tiene permisos para acceder a esta página',
                'nombre': nombre,
            })
    else:
        return render(request, 'login.html', {
            'r2': 'Debe iniciar sesión'
        })


def menu_funcionario(request):
    tipo = request.session.get('tipo')
    nombre = request.session.get('nombre')
    estadoSesion = request.session.get('estadoSesion')
    if tipo and estadoSesion:
        if tipo == 'admin':
            return render(request, 'menu_admin.html', {
                'r2': 'No tiene permisos para acceder a esta página',
                'nombre': nombre,
            })       
        elif tipo == 'funcionario':
            return render(request, 'menu_funcionarios.html', {
                'nombre': nombre,
            })
        elif tipo == 'docente':
            return render(request, 'menu_docente.html', {
                'r2': 'No tiene permisos para acceder a esta página',
                'nombre': nombre,
            })
    else:
        return render(request, 'login.html', {
            'r2': 'Debe iniciar sesión'
        })