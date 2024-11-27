from django.shortcuts import render, get_object_or_404, redirect
from matriculas.models import Curso

def mostrar_gestion_cursos(request):
    tipo = request.session.get('tipo')
    estadoSesion = request.session.get('estadoSesion')
    if tipo and estadoSesion:
        if tipo == 'admin':
            if request.method == "POST":
                nombre = request.POST.get('nombre')
                letra = request.POST.get('letra')
                if nombre:
                    Curso.objects.create(nombre=nombre)
                    return redirect('gestion_cursos')  

            cursos = Curso.objects.all()
            return render(request, 'gestion_cursos/gestion_cursos.html', {
                'tipo': tipo,
                'cursos': cursos,
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
    curso = get_object_or_404(Curso, id=curso_id)
    if request.method == "POST":
        curso.nombre = request.POST.get("nombre")
        curso.save()
        return redirect("gestion_cursos")
    return render(request, "gestion_cursos/editar_curso.html", {"curso": curso})

def eliminar_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    curso.delete()
    return redirect('gestion_cursos')
