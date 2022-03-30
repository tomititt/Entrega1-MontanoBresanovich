from django.urls import path
from appcoder.views import *


urlpatterns = [
    path('', inicio, name = "Inicio"),
    path('magos/', magos, name = "Magos"),
    path('asignaturas/', asignaturas, name = "Asignaturas"),
    path('profesores/', profesores, name = "Profesores"),
    path('extasis/', extasis, name = "EXTASIS"),
    path('asignaturasformulario/', formulario_asignatura, name = 'Formulario'),
    path('magosformulario/', formulario_magos, name = 'Formulario'),
    path('profesoresformulario/', formulario_profesores, name = 'Formulario'),
    path('buscamagos', busca_magos, name = 'Busqueda'),
    
]
