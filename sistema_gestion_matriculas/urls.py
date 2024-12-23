from django.contrib import admin
from django.urls import path

from matriculas.views import general, matriculas, funcionarios, cursos, nacionalidades, historial_acciones, perfil, docente


urlpatterns = [
    path('admin/', admin.site.urls),
    # General
    path('', general.index),
    path('login', general.login),
    path('logout', general.logout),
    path("menu_admin", general.menu_admin),
    path("menu_docente", general.menu_docente),

    # Matriculas
    path('matriculas/agregar', matriculas.mostrar_agregar),
    path('matriculas/cargar_cursos', matriculas.cargar_cursos),
    path("matriculas/agregar_matricula", matriculas.registrar_matricula),

    path('matriculas/editar/<int:id>', matriculas.mostrar_editar),
    path('matriculas/editar_matricula/<int:id>', matriculas.editar_matricula),

    path('matriculas/eliminar/<int:id>', matriculas.eliminar_matricula),
    path('matriculas/listar', matriculas.mostrar_listado),
    
    # Funcionarios
    path('funcionarios/agregar', funcionarios.mostrar_agregar),
    path('funcionarios/editar/<int:id>', funcionarios.mostrar_editar),
    path('funcionarios/eliminar/<int:id>', funcionarios.mostrar_eliminar),
    path('funcionarios/listar', funcionarios.mostrar_listado),

    # cursos
    path('cursos/', cursos.mostrar_gestion_cursos, name='gestion_cursos'),
    path('cursos/filtrar/periodo', cursos.filtrar_por_periodo),
    path('cursos/editar/<curso_id>/', cursos.editar_curso, name='editar_curso'),
    path('cursos/eliminar/<int:pk>/', cursos.eliminar_curso, name='eliminar_curso'),
    path('cursos/periodos/', cursos.mostrar_gestion_periodos, name='gestion_periodos'),
    path('cursos/periodos/editar/<int:id>/', cursos.editar_periodo, name='editar_periodo'),
    path('cursos/periodos/eliminar/<int:id>/', cursos.eliminar_periodo, name='eliminar_periodo'),

    # docente
    path('docente/cursos', docente.mostrar_cursos, name='cursos_docente'),
    path('docente/cursos/filtrar/periodo', docente.filtrar_por_periodo),

    #nacionalidad
    path("nacionalidades/", nacionalidades.gestionar_nacionalidades, name="gestion_nacionalidades"),
    path("nacionalidades/editar/<int:nacionalidad_id>/", nacionalidades.editar_nacionalidad, name="editar_nacionalidad"),
    path("nacionalidades/eliminar/<int:nacionalidad_id>/", nacionalidades.eliminar_nacionalidad, name="eliminar_nacionalidad"),

    #historial
    path('historial/', historial_acciones.historial_acciones, name='historial_acciones'),

    #Perfil
    path('perfil/', perfil.mostrar_perfil, name='perfil'),
    path('perfil/editar', perfil.editar_perfil, name='editar_perfil'),
]
