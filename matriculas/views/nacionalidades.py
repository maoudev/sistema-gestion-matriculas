from django.shortcuts import render, get_object_or_404, redirect
from matriculas.models import Nacionalidad  

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
        return redirect("gestion_nacionalidades")
    return render(request, "gestion_nacionalidades/editar_nacionalidad.html", {"nacionalidad": nacionalidad})


def eliminar_nacionalidad(request, nacionalidad_id):
    nacionalidad = get_object_or_404(Nacionalidad, id=nacionalidad_id)
    nacionalidad.delete()
    return redirect("gestion_nacionalidades")
