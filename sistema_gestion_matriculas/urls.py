from django.contrib import admin
from django.urls import path

from matriculas.views import general
from matriculas.views import matriculas
from matriculas.views import funcionarios
from matriculas.views import cursos
from matriculas.views import nacionalidades
from matriculas.views import historial_acciones


urlpatterns = [
    path('admin/', admin.site.urls),
    # General
    path('', general.index),
    path('login', general.login),
    path('logout', general.logout),
    path("menu_admin", general.menu_admin),

    # Matriculas
    path('matriculas/agregar', matriculas.mostrar_agregar),
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
    path('cursos/editar/<curso_id>/', cursos.editar_curso, name='editar_curso'),
    path('cursos/eliminar/<int:pk>/', cursos.eliminar_curso, name='eliminar_curso'),

    #nacionalidad
     path("nacionalidades/", nacionalidades.gestionar_nacionalidades, name="gestion_nacionalidades"),
    path("nacionalidades/editar/<int:nacionalidad_id>/", nacionalidades.editar_nacionalidad, name="editar_nacionalidad"),
    path("nacionalidades/eliminar/<int:nacionalidad_id>/", nacionalidades.eliminar_nacionalidad, name="eliminar_nacionalidad"),

    #historial
    path('historial/', historial_acciones.historial_acciones, name='historial_acciones'),
]
