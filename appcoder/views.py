from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from appcoder.forms import AsignaturasFormulario
from appcoder.models import *

# Create your views here.

def inicio(request):
    date_init = datetime.now()
    dict_user = {"user": "tmonti", "date": date_init}
    return render(request, "appcoder/index.html", dict_user)

def magos(request):
    return render(request, "appcoder/magos.html")

def asignaturas(request):
    return render(request, "appcoder/asignaturas.html")

def profesores(request):
    return render(request, "appcoder/profesores.html")

def extasis(request):
    return render(request, "appcoder/extasis.html")

def formulario_asignatura(request):

    if request.method == "POST":
        asignatura = AsignaturasFormulario(request.POST)
        print(asignatura)

        if asignatura.is_valid:
            data = asignatura.cleaned_data

            asignatura_nueva = Asignatura(data['nombre'], data['clase'])
            asignatura_nueva.save()


    return render(request, 'appcoder/asignaturasFormulario.html')

