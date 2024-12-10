from django.shortcuts import render
from django.db.models import Q

from matriculas.models import Curso, Periodo, Funcionario



def mostrar_cursos(request):
    periodos = Periodo.objects.all().values()
    return render(request, 'docentes/gestion_cursos.html', {
        'periodos': periodos
    })

def filtrar_por_periodo(request):
    idFuncionario = request.session.get('idUsuario')
    funcionario = Funcionario.objects.get(id=idFuncionario)

    id = request.POST.get('cboper2')
    periodo = Periodo.objects.get(id=id)
    cursos = Curso.objects.filter(periodo=periodo).values()
    periodos = Periodo.objects.all().values()


    cursos_jefatura = Curso.objects.filter(
        Q(profesor_jefe = funcionario)
        & Q(periodo = periodo)
        ).values()
    
    cursos_clases = Curso.objects.filter(
        Q(profesores__id = funcionario.pk)
        & Q(periodo = periodo)
        ).values()
    

    return render(request, 'docentes/gestion_cursos.html', {
        'cursos': cursos,
        'periodos': periodos,
        'cursos_jefatura': cursos_jefatura,
        'cursos_clases': cursos_clases
    })