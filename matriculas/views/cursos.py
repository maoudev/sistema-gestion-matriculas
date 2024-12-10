from django.shortcuts import render, get_object_or_404, redirect
from matriculas.models import Curso, Periodo, Funcionario, RegistroAccion

from datetime import datetime

def mostrar_gestion_cursos(request):
    tipo = request.session.get('tipo')
    estadoSesion = request.session.get('estadoSesion')
    if tipo and estadoSesion:
        if tipo == 'admin':
            if request.method == "POST":
                periodo = request.POST.get('cboper')
                nombre = request.POST.get('nombre')
                periodo_seleccionado = Periodo.objects.get(id=periodo)
                if periodo_seleccionado.activo == False:
                    if nombre:
                        Curso.objects.create(nombre=nombre, periodo=periodo_seleccionado)
                        return redirect('gestion_cursos')  
                else:
                    cursos = Curso.objects.all().values()
                    periodos = Periodo.objects.all().values()
                    return render(request, 'gestion_cursos/gestion_cursos.html', {
                        'tipo': tipo,
                        'r2': 'El periodo seleccionado está activo y no se pueden agregar cursos',
                        'cursos': cursos,
                        'periodos': periodos,
                    })

            usuario = Funcionario.objects.get(id=request.session.get('idUsuario'))
            historial = RegistroAccion(usuario=usuario, accion='Registrar Curso', detalles='Curso registrado correctamente!', fecha=datetime.now())
            historial.save()

            cursos = Curso.objects.all().values()
            periodos = Periodo.objects.all().values()
            return render(request, 'gestion_cursos/gestion_cursos.html', {
                'tipo': tipo,
                'cursos': cursos,
                'periodos': periodos,
            })
        else:
            return render(request, 'menu_docente.html', {
                'r2': 'No tiene permisos para acceder a esta página'
            })
    else:
        return render(request, 'login.html', {
            'r2': 'Debe iniciar sesión'
        })

def editar_curso(request, curso_id):
    curso = Curso.objects.filter(id=curso_id).first()
    if curso is None:
        return redirect('gestion_cursos')

    if request.method == "POST":
        curso.nombre = request.POST.get("nombre")
        curso.save()
        usuario = Funcionario.objects.get(id=request.session.get('idUsuario'))
        historial = RegistroAccion(usuario=usuario, accion='Editar Curso', detalles='Curso editado correctamente!', fecha=datetime.now())
        historial.save()
        return redirect("gestion_cursos")
    return render(request, "gestion_cursos/editar_curso.html", {"curso": curso})

def eliminar_curso(request, pk):
    curso = Curso.objects.filter(id=pk).first()
    if curso is None:
        return redirect('gestion_cursos')

    curso.delete()

    usuario = Funcionario.objects.get(id=request.session.get('idUsuario'))
    historial = RegistroAccion(usuario=usuario, accion='Eliminar Curso', detalles='Curso eliminado correctamente!', fecha=datetime.now())
    historial.save()    
    return redirect('gestion_cursos')



def mostrar_gestion_periodos(request):
    tipo = request.session.get('tipo')
    estadoSesion = request.session.get('estadoSesion')
    if tipo and estadoSesion:
        if tipo == 'admin':
            if request.method == "POST":
                anio = request.POST.get('txtani')
                estado = request.POST.get('cboest')
                if anio and estado:
                    if estado == "activo":
                        activo = True
                    else:
                        activo = False
                    
                    usuario = Funcionario.objects.get(id=request.session.get('idUsuario'))
                    historial = RegistroAccion(usuario=usuario, accion='Registrar Periodo', detalles='Periodo registrado correctamente!', fecha=datetime.now())
                    historial.save()

                    Periodo.objects.create(anio=anio, activo=activo)
                    return redirect('gestion_periodos')  

            periodos = Periodo.objects.all()
            return render(request, 'gestion_cursos/gestion_periodos.html', {
                'tipo': tipo,
                'periodos': periodos,
            })
        else:
            return render(request, 'menu_docente.html', {
                'r2': 'No tiene permisos para acceder a esta página'
            })
    else:
        return render(request, 'login.html', {
            'r2': 'Debe iniciar sesión'
        }) 
    

def editar_periodo(request, id):
    periodo = Periodo.objects.filter(id=id).first()

    if periodo is None:
        return redirect('gestion_periodos')

    if request.method == "POST":
        periodo.anio = request.POST.get("txtani")
        estado = request.POST.get("cboest")
        if estado == "activo":
            periodo.activo = True
        else:
            periodo.activo = False

        periodo.save()

        usuario = Funcionario.objects.get(id=request.session.get('idUsuario'))
        historial = RegistroAccion(usuario=usuario, accion='Editar Periodo', detalles='Periodo editado correctamente!', fecha=datetime.now())
        historial.save()
        return redirect("gestion_periodos")
    return render(request, "gestion_cursos/editar_periodo.html", {"periodo": periodo})

def eliminar_periodo(request, id):
    periodo = Periodo.objects.filter(id=id).first()
    if periodo is None:
        return redirect('gestion_periodos')
    
    periodo.delete()

    usuario = Funcionario.objects.get(id=request.session.get('idUsuario'))
    historial = RegistroAccion(usuario=usuario, accion='Registrar Periodo', detalles='Periodo registrado correctamente!', fecha=datetime.now())
    historial.save()
    return redirect('gestion_periodos')


def filtrar_por_periodo(request):
    id = request.POST.get('cboper2')
    periodo = Periodo.objects.get(id=id)
    cursos = Curso.objects.filter(periodo=periodo).values()
    periodos = Periodo.objects.all().values()
    return render(request, 'gestion_cursos/gestion_cursos.html', {
        'cursos': cursos,
        'periodos': periodos,
    })