from django.shortcuts import render
from django.db.models import Q
from matriculas.models import Nacionalidad, Periodo, Curso, Alumno, Apoderado, Matricula, RegistroAccion, Funcionario
from datetime import datetime

# Create your views here.
def mostrar_agregar(request):
    tipo = request.session.get('tipo')
    estadoSesion = request.session.get('estadoSesion')
    if tipo and estadoSesion:
        if tipo == 'admin' or tipo == 'funcionario':
            nacionalidades = Nacionalidad.objects.all().values()
            periodos = Periodo.objects.all().values()
            return render(request, 'gestion_matriculas/agregar.html', {
                'tipo': tipo,
                'nacionalidades': nacionalidades,
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

def cargar_cursos(request):
    periodo_id = request.POST.get('cboper')
    periodo_seleccionado = Periodo.objects.get(id=periodo_id)
    cursos = Curso.objects.filter(periodo=periodo_seleccionado).values()
    nacionalidades = Nacionalidad.objects.all().values()
    return render(request, 'gestion_matriculas/agregar.html', {
        'cursos': cursos,
        'nacionalidades': nacionalidades,
        'periodo': periodo_seleccionado,
    })

def mostrar_editar(request, id):
    tipo = request.session.get('tipo')
    estadoSesion = request.session.get('estadoSesion')
    if tipo and estadoSesion:
        if tipo == 'admin':
            matricula = Matricula.objects.get(id=id)
            periodo = matricula.periodo
            nacionalidades = Nacionalidad.objects.all().values()
            cursos = Curso.objects.filter(periodo=periodo).values()
            return render(request, 'gestion_matriculas/editar.html', {
                'tipo': tipo,
                'matricula': matricula,
                'nacionalidades': nacionalidades,
                'periodo': periodo,
                'cursos': cursos,
                'id': id,
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
        if tipo == 'admin':
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
        if tipo == 'admin':
            matriculas = Matricula.objects.select_related('periodo', 'alumno', 'curso', 'curso__sala').prefetch_related('alumno__nacionalidades')
            return render(request, 'gestion_matriculas/listado.html', {
                'tipo': tipo,
                'matriculas': matriculas,
            })
        else:
            return render(request, 'menu_docente.html', {
                'r2': 'No tiene permisos para acceder a esta página'
            })
    else:
        return render(request, 'login.html', {
            'r2': 'Debe iniciar sesión'
        })
    


# matriculas

def registrar_matricula(request):
    try: 
        periodo = request.POST["cboper"]
        periodo_seleccionado = Periodo.objects.get(id=periodo)

        # Apoderado
        nombre_apoderado = request.POST["txtnom"]
        apellido_paterno_apoderado = request.POST["txtapepat"]
        apellido_materno_apoderado = request.POST["txtapemat"]
        perentesco = request.POST["txtpar"]
        rut_apoderado = request.POST["txtrut"]
        edad_apoderado = request.POST["txteda"]
        nacionalidades_apoderado = request.POST.getlist("cbonac")
        
        comprobar_apoderado = Apoderado.objects.filter(rut=rut_apoderado).first()
        if comprobar_apoderado:
            comprobar_apoderado.nombres = nombre_apoderado
            comprobar_apoderado.paterno = apellido_paterno_apoderado
            comprobar_apoderado.materno = apellido_materno_apoderado
            comprobar_apoderado.edad = edad_apoderado
            comprobar_apoderado.parentesco = perentesco
            comprobar_apoderado.save()
            comprobar_apoderado.nacionalidades.set(nacionalidades_apoderado)
        else:
            apoderado = Apoderado(rut = rut_apoderado, nombres = nombre_apoderado, paterno = apellido_paterno_apoderado, materno = apellido_materno_apoderado, edad = edad_apoderado, parentesco = perentesco)
            apoderado.save()
            apoderado.nacionalidades.set(nacionalidades_apoderado)




        # Alumno
        nombre_alumno = request.POST["txtnomalu"]
        apellido_paterno_alumno = request.POST["txtapepatalu"]
        apellido_materno_alumno = request.POST["txtapematalu"]
        rut_alumno = request.POST["txtrutalu"]
        edad_alumno = request.POST["txtedaalu"]
        nacionalidades_alumno = request.POST.getlist("cbonacalu")
        curso = request.POST["cbocur"]
        promedio_anterior = request.POST["txtproalu"]

        curso_seleccionado = Curso.objects.get(id=curso)
        if curso_seleccionado.cantidad_alumnos >= 30:
            tipo = request.session.get('tipo')
            nacionalidades = Nacionalidad.objects.all().values()
            periodos = Periodo.objects.all().values()
            cursos = Curso.objects.all().values()
            return render(request, 'gestion_matriculas/agregar.html', {
                'r2': 'El curso seleccionado ya tiene 30 alumnos',
                'tipo': tipo,
                'nacionalidades': nacionalidades,
                'periodos': periodos,
                'cursos': cursos,
            })
        

        comprobar_alumno = Alumno.objects.filter(rut = rut_alumno).first()

        if comprobar_alumno:
            comprobar_alumno.nombres = nombre_alumno
            comprobar_alumno.paterno = apellido_paterno_alumno
            comprobar_alumno.materno = apellido_materno_alumno
            comprobar_alumno.edad = edad_alumno
            comprobar_alumno.promedio_anterior = promedio_anterior
            comprobar_alumno.curso = curso_seleccionado
            comprobar_alumno.save()
            comprobar_alumno.nacionalidades.set(nacionalidades_alumno)

        else:
            alumno = Alumno(rut = rut_alumno, nombres = nombre_alumno, paterno = apellido_paterno_alumno, materno = apellido_materno_alumno, edad = edad_alumno, promedio_anterior = int(promedio_anterior))
            alumno.curso = curso_seleccionado
            alumno.save()
            alumno.nacionalidades.set(nacionalidades_alumno)
            



        # Matricula
        alumno_final = Alumno.objects.get(rut = rut_alumno)
        apoderado_apoderado = Apoderado.objects.get(rut = rut_apoderado)
        comprobar_matricula = Matricula.objects.filter(
            Q(alumno = alumno_final) & Q(periodo = periodo_seleccionado)
        ).first()

        if comprobar_matricula:
            tipo = request.session.get('tipo')
            nacionalidades = Nacionalidad.objects.all().values()
            periodos = Periodo.objects.all().values()
            cursos = Curso.objects.all().values()
            return render(request, 'gestion_matriculas/agregar.html', {
                'r2': 'El alumno ya está matriculado en el periodo seleccionado',
                'tipo': tipo,
                'nacionalidades': nacionalidades,
                'periodos': periodos,
                'cursos': cursos,
            })
        

        matricula = Matricula(alumno = alumno, periodo = periodo_seleccionado, apoderado = apoderado_apoderado, curso = curso_seleccionado)
        matricula.save()

        curso_seleccionado.cantidad_alumnos += 1
        curso_seleccionado.save()

        id_usuario = request.session.get('idUsuario')
        usuario = Funcionario.objects.get(id=id_usuario)

        historial = RegistroAccion(usuario=usuario, accion='Registrar de matricula', detalles='Matricula registrada correctamente!', fecha=datetime.now())
        historial.save()


        tipo = request.session.get('tipo')
        nacionalidades = Nacionalidad.objects.all().values()
        periodos = Periodo.objects.all().values()
        cursos = Curso.objects.all().values()
        return render(request, 'gestion_matriculas/agregar.html', {
            
            'tipo': tipo,
            'nacionalidades': nacionalidades,
            'periodos': periodos,
            'cursos': cursos,
            'r': 'Matricula registrada correctamente',
        })
    except Exception as e:
        print(e)
        tipo = request.session.get('tipo')
        nacionalidades = Nacionalidad.objects.all().values()
        periodos = Periodo.objects.all().values()
        cursos = Curso.objects.all().values()
        return render(request, 'gestion_matriculas/agregar.html', {
            'tipo': tipo,
            'nacionalidades': nacionalidades,
            'periodos': periodos,
            'r2': 'Error al registrar matricula',
            'cursos': cursos,
        })


def editar_matricula(request, id):
    try:
        matricula = Matricula.objects.get(id=id)

        periodo = request.POST["cboper"]
        periodo_seleccionado = Periodo.objects.get(id=periodo)

        if periodo_seleccionado.activo == False:
            return render(request, 'gestion_matriculas/agregar.html', {
                'r2': 'El periodo seleccionado no está activo',
            })
        
        # Apoderado
        nombre_apoderado = request.POST["txtnom"]
        apellido_paterno_apoderado = request.POST["txtapepat"]
        apellido_materno_apoderado = request.POST["txtapemat"]
        perentesco = request.POST["txtpar"]
        rut_apoderado = request.POST["txtrut"]
        edad_apoderado = request.POST["txteda"]
        nacionalidades_apoderado = request.POST.getlist("cbonac")

        matricula.apoderado.nombres = nombre_apoderado
        matricula.apoderado.paterno = apellido_paterno_apoderado
        matricula.apoderado.materno = apellido_materno_apoderado
        matricula.apoderado.rut = rut_apoderado
        matricula.apoderado.edad = edad_apoderado
        matricula.apoderado.parentesco = perentesco
        matricula.apoderado.save()
        matricula.apoderado.nacionalidades.set(nacionalidades_apoderado)

                # Alumno
        nombre_alumno = request.POST["txtnomalu"]
        apellido_paterno_alumno = request.POST["txtapepatalu"]
        apellido_materno_alumno = request.POST["txtapematalu"]
        rut_alumno = request.POST["txtrutalu"]
        edad_alumno = request.POST["txtedaalu"]
        nacionalidades_alumno = request.POST.getlist("cbonacalu")
        curso = request.POST["cbocur"]
        promedio_anterior = request.POST["txtproalu"]

        curso_seleccionado = Curso.objects.get(id=curso)

        matricula.alumno.nombres = nombre_alumno
        matricula.alumno.paterno = apellido_paterno_alumno
        matricula.alumno.materno = apellido_materno_alumno
        matricula.alumno.rut = rut_alumno
        matricula.alumno.edad = edad_alumno
        matricula.alumno.promedio_anterior = float(promedio_anterior)
        matricula.alumno.curso = curso_seleccionado
        matricula.alumno.save()
        matricula.alumno.nacionalidades.set(nacionalidades_alumno)

        matricula.periodo = periodo_seleccionado
        matricula.curso = curso_seleccionado
        matricula.save()

        id_usuario = request.session.get('idUsuario')
        usuario = Funcionario.objects.get(id=id_usuario)

        historial = RegistroAccion(usuario=usuario, accion='Editar Matricula', detalles='Matricula modificada correctamente!', fecha=datetime.now())
        historial.save()

        tipo = request.session.get('tipo')
        matriculas = Matricula.objects.select_related('periodo', 'alumno', 'curso', 'curso__sala').prefetch_related('alumno__nacionalidades')
        return render(request, 'gestion_matriculas/listado.html', {
            'tipo': tipo,
            'matriculas': matriculas,
            'r': 'Matricula editada correctamente',
        })



        
    except Exception as e:
        print(e)
        tipo = request.session.get('tipo')
        matriculas = Matricula.objects.select_related('periodo', 'alumno', 'curso', 'curso__sala').prefetch_related('alumno__nacionalidades')

        return render(request, 'gestion_matriculas/listado.html', {
            'tipo': tipo,
            'r2': 'Error al editar matricula',
            'matriculas': matriculas
        })
    
def eliminar_matricula(request, id):
    try:
        matricula = Matricula.objects.get(id=id)
        matricula.delete()

        id_usuario = request.session.get('idUsuario')
        usuario = Funcionario.objects.get(id=id_usuario)

        historial = RegistroAccion(usuario=usuario, accion='Eliminar matricula', detalles='Matricula eliminada correctamente!', fecha=datetime.now())
        historial.save()

        tipo = request.session.get('tipo')
        matriculas = Matricula.objects.select_related('periodo', 'alumno', 'curso', 'curso__sala').prefetch_related('alumno__nacionalidades')
        return render(request, 'gestion_matriculas/listado.html', {
            'tipo': tipo,
            'matriculas': matriculas,
            'r': 'Matricula eliminada correctamente',
        })
    except Exception as e:
        print(e)
        tipo = request.session.get('tipo')
        matriculas = Matricula.objects.select_related('periodo', 'alumno', 'curso', 'curso__sala').prefetch_related('alumno__nacionalidades')

        return render(request, 'gestion_matriculas/listado.html', {
            'tipo': tipo,
            'r2': 'Error al editar matricula',
            'matriculas': matriculas
        })  