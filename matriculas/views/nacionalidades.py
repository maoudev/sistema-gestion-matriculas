from django.shortcuts import render, get_object_or_404, redirect
from matriculas.models import Nacionalidad, RegistroAccion, Funcionario

from datetime import datetime

def gestionar_nacionalidades(request):
    tipo = request.session.get('tipo')
    estadoSesion = request.session.get('estadoSesion')

    if tipo and estadoSesion:
        if tipo in ['admin', 'funcionario']:
            nacionalidades = Nacionalidad.objects.all()

            if request.method == "POST":
                nombre = request.POST.get("nombre")
                if nombre:
                    Nacionalidad.objects.create(nombre=nombre)

                    usuario = Funcionario.objects.get(id=request.session.get('idUsuario'))
                    historial = RegistroAccion(usuario=usuario, accion='Registrar Nacionalidad', detalles='Nacionalidad registrada correctamente!', fecha=datetime.now())
                    historial.save()
                    return redirect("gestion_nacionalidades")

            return render(request, "gestion_nacionalidades/gestion_nacionalidades.html", {
                "tipo": tipo,
                "nacionalidades": nacionalidades,
            })
        else:
            return render(request, "menu_docente.html", {
                "r2": "No tiene permisos para acceder a esta página"
            })
    else:
        return render(request, "login.html", {
            "r2": "Debe iniciar sesión"
        })


def editar_nacionalidad(request, nacionalidad_id):
    nacionalidad = get_object_or_404(Nacionalidad, id=nacionalidad_id)
    if request.method == "POST":
        nacionalidad.nombre = request.POST.get("nombre")
        nacionalidad.save()

        usuario = Funcionario.objects.get(id=request.session.get('idUsuario'))
        historial = RegistroAccion(usuario=usuario, accion='Editar Periodo', detalles='Periodo editado correctamente!', fecha=datetime.now())
        historial.save()
        return redirect("gestion_nacionalidades")
    return render(request, "gestion_nacionalidades/editar_nacionalidad.html", {"nacionalidad": nacionalidad})


def eliminar_nacionalidad(request, nacionalidad_id):
    nacionalidad = get_object_or_404(Nacionalidad, id=nacionalidad_id)
    nacionalidad.delete()

    usuario = Funcionario.objects.get(id=request.session.get('idUsuario'))
    historial = RegistroAccion(usuario=usuario, accion='Eliminar Periodo', detalles='Periodo eliminado correctamente!', fecha=datetime.now())
    historial.save()
    return redirect("gestion_nacionalidades")
