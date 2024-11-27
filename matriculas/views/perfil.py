from django.shortcuts import render, redirect, get_object_or_404
from matriculas.models import Funcionario

def mostrar_perfil(request):
    if 'idUsuario' in request.session:
        usuario_id = request.session['idUsuario']
        perfil = get_object_or_404(Funcionario, id=usuario_id)
        return render(request, 'gestion_perfil/perfil.html', {
            'perfil': perfil
        })
    else:
        return redirect('/login')

def editar_perfil(request):
    if 'idUsuario' in request.session:
        usuario_id = request.session['idUsuario']
        perfil = get_object_or_404(Funcionario, id=usuario_id)

        if request.method == "POST":
            nombres = request.POST.get("txtnom")
            paterno = request.POST.get("txtpat")
            materno = request.POST.get("txtmat")
            correo = request.POST.get("txtema")
            clave = request.POST.get("txtpas")

            perfil.nombres = nombres
            perfil.paterno = paterno
            perfil.materno = materno
            perfil.correo = correo

            if clave:
                from matriculas.utils import hash_password
                perfil.password = hash_password(clave)

            perfil.save()

            return render(request, 'perfil/perfil.html', {
                'perfil': perfil,
                'r': 'Perfil actualizado correctamente'
            })

        return render(request, 'perfil/editar_perfil.html', {
            'perfil': perfil
        })
    else:
        return redirect('/login')
