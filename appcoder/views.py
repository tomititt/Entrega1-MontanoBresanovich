from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def magos(request):
    return HttpResponse("vista de magos")

def asignaturas(request):
    return HttpResponse("vista de asignaturas")

def profesores(request):
    return HttpResponse("vista de profesores")

def extasis(request):
    return HttpResponse("vista de extasis")

