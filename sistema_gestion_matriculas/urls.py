from django.contrib import admin
from django.urls import path

from matriculas.views import general
from matriculas.views import matriculas
from matriculas.views import funcionarios


urlpatterns = [
    path('admin/', admin.site.urls),
    # General
    path('', general.index),
    path('login', general.login),
    path('logout', general.logout),
    path("menu_admin", general.menu_admin),
    path("menu_funcionario", general.menu_funcionario),

    # Matriculas
    path('matriculas/agregar', matriculas.mostrar_agregar),
    path('matriculas/editar', matriculas.mostrar_editar),
    path('matriculas/eliminar', matriculas.mostrar_eliminar),
    path('matriculas/listar', matriculas.mostrar_listado),
    
    # Funcionarios
    path('funcionarios/agregar', funcionarios.mostrar_agregar),
    path('funcionarios/editar', funcionarios.mostrar_editar),
    path('funcionarios/eliminar', funcionarios.mostrar_eliminar),
    path('funcionarios/listar', funcionarios.mostrar_listado),
]
