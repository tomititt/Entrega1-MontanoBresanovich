from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from appcoder.forms import AsignaturasFormulario
from appcoder.models import *
from appcoder.forms import MagosFormulario
from appcoder.forms import ProfesoresFormulario


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

            asignatura_nueva = Asignatura(nombre=data['nombre'], clase=data['clase'])
            asignatura_nueva.save()
            asignaturalist = Asignatura.objects.all()

            return render(request, 'appcoder/index.html', {'asignaturalist': asignaturalist})

    else:
        asignatura = AsignaturasFormulario()

        return render(request, 'appcoder/asignaturasFormulario.html', {'asignatura': asignatura} )

def formulario_magos(request):

    if request.method == "POST":
        mago = MagosFormulario(request.POST)
        print(mago)

        if mago.is_valid:
            data = mago.cleaned_data

            mago_nuevo = Mago(nombre=data['nombre'], apellido=data['apellido'], casa=data['casa'])
            mago_nuevo.save()
            magolist = Mago.objects.all()

            return render(request, 'appcoder/index.html', {'magolist': magolist})
    else:
        mago = MagosFormulario()
        return render(request, 'appcoder/magosFormulario.html', {'mago':mago})

def formulario_profesores(request):

    if request.method == "POST":
        profesor = ProfesoresFormulario(request.POST)
        print(profesor)

        if profesor.is_valid:
            data = profesor.cleaned_data

            profesor_nuevo = Profesor(nombre=data['nombre'], apellido=data['apellido'], materia=data['materia'])
            profesor_nuevo.save()
            profesorlist = Profesor.objects.all()

            return render(request, 'appcoder/index.html', {'profesorlist': profesorlist})
    else:
        profesor = ProfesoresFormulario()
        return render(request, 'appcoder/profesoresFormulario.html', {'profesor':profesor})

def busca_magos(request):

    data = request.GET['nombre']
    print(data)
    if data:
        mago = Mago.objects.filter(nombre__icontains = data)

        return render(request, 'appcoder/components/buscamagos.html', {"mago": mago[0], "id": data})



    return render(request, 'appcoder/components/buscamagos.html')


