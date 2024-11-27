from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from matriculas.models import RegistroAccion

def historial_acciones(request):
    acciones = RegistroAccion.objects.all().order_by('-fecha')
    return render(request, 'historial_acciones.html', {'acciones': acciones})
