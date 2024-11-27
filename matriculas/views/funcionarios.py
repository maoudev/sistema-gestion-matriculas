from django.shortcuts import render, get_object_or_404, redirect
from matriculas.models import Funcionario, Curso, RegistroAccion

from datetime import datetime

from matriculas.utils import hash_password


def mostrar_agregar(request):
    if request.method == "POST":
        clave = request.POST.get("txtpas")
        nombres = request.POST.get("txtnom")
        paterno = request.POST.get("txtpat")
        materno = request.POST.get("txtmat")
        rut = request.POST.get("txtrut")
        correo = request.POST.get("txtema")
        cargo = request.POST.get("cbocar")
        cursos = request.POST.getlist("cbocur")
        cursos_jefatura = request.POST.getlist("cbocurjef")
        jefatura = request.POST.get("rdojef")
        asignatura = request.POST.get("txtasi")
        estado = request.POST.get("cboest")

        funcionario = Funcionario(
            nombres=nombres,
            paterno=paterno,
            materno=materno,
            rut=rut,
            correo=correo,
            cargo=cargo,
            asignatura=asignatura,
            password=hash_password(clave)
        )
        if estado == "activo":
            funcionario.estado = True
        else:
            funcionario.estado = False
        funcionario.save()

        if jefatura == "1":
            cursos = Curso.objects.filter(id__in=cursos_jefatura)
            for curso in cursos:
                curso.profesor_jefe = funcionario
                curso.save()

        cursos = Curso.objects.filter(id__in=cursos)
        for curso in cursos:
            curso.profesores.add(funcionario)
            curso.save()
        

        usuario = Funcionario.objects.get(id=request.session.get('idUsuario'))
        historial = RegistroAccion(usuario=usuario, accion='Registrar funcionario', detalles='Funcionario registrado correctamente!', fecha=datetime.now())
        historial.save()


        return render(request, "gestion_funcionarios/agregar.html", {
                "r": "Funcionario agregado correctamente",
        })
        
    cursos = Curso.objects.all().values()
    return render(request, 'gestion_funcionarios/agregar.html', {
        "cursos": cursos
    })


def mostrar_editar(request, id):
    funcionario = Funcionario.objects.get(id=id)
    if request.method == "POST":
        clave = request.POST.get("txtpas")
        nombres = request.POST.get("txtnom")
        paterno = request.POST.get("txtpat")
        materno = request.POST.get("txtmat")
        rut = request.POST.get("txtrut")
        correo = request.POST.get("txtema")
        cargo = request.POST.get("cbocar")
        cursos = request.POST.getlist("cbocur")
        cursos_jefatura = request.POST.getlist("cbocurjef")
        jefatura = bool(request.POST.get("rdojef"))
        asignatura = request.POST.get("txtasi")
        estado = request.POST.get("cboest")

        funcionario.nombres = nombres
        funcionario.paterno = paterno
        funcionario.materno = materno
        funcionario.rut = rut
        funcionario.correo = correo
        funcionario.cargo = cargo
        funcionario.asignatura = asignatura
        if clave:
            funcionario.password = hash_password(clave)

        if estado == "activo":
            funcionario.estado = True
        else:
            funcionario.estado = False
        funcionario.save()

        if jefatura:
            cursos = Curso.objects.filter(id__in=cursos_jefatura)
            for curso in cursos:
                curso.profesor_jefe = funcionario
                curso.save()

        cursos = Curso.objects.filter(id__in=cursos)
        for curso in cursos:
            curso.profesores.add(funcionario)
            curso.save()



        usuario = Funcionario.objects.get(id=request.session.get('idUsuario'))
        historial = RegistroAccion(usuario=usuario, accion='Editar funcionario', detalles='Funcionario editado correctamente!', fecha=datetime.now())
        historial.save()

        cursos = Curso.objects.values().all()
        funcionarios = Funcionario.objects.prefetch_related('cursos')


        return render(request, "gestion_funcionarios/listar.html", {
            'r': 'Funcionario editado correctamente',
            "funcionarios": funcionarios,
            "cursos": cursos
        })

    cursos = Curso.objects.all().values()
    return render(request, 'gestion_funcionarios/editar.html', {
        "funcionario": funcionario,
        "cursos": cursos
        })


def mostrar_eliminar(request, id):
    funcionario = get_object_or_404(Funcionario, id=id)
    funcionario.delete()

    usuario = Funcionario.objects.get(id=request.session.get('idUsuario'))
    historial = RegistroAccion(usuario=usuario, accion='Eliminar funcionario', detalles='Funcionario eliminado correctamente!', fecha=datetime.now())
    historial.save()

    cursos = Curso.objects.values().all()
    funcionarios = Funcionario.objects.prefetch_related('cursos')
    return render(request, 'gestion_funcionarios/listar.html', {
        'r': 'Funcionario eliminado correctamente',
        "funcionarios": funcionarios,
        "cursos": cursos
    })

def mostrar_listado(request):
    cursos = Curso.objects.values().all()
    funcionarios = Funcionario.objects.prefetch_related('cursos')
    return render(request, 'gestion_funcionarios/listar.html', {
        "funcionarios": funcionarios,
        "cursos": cursos
        })
