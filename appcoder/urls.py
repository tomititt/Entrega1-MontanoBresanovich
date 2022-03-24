from django.urls import path
from appcoder.views import *


urlpatterns = [
    path('magos/', magos),
    path('asignaturas/', asignaturas),
    path('profesores/', profesores),
    path('extasis/', extasis),
    
]
