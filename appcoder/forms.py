from django import forms

class AsignaturasFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    clase = forms.IntegerField()

class MagosFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    casa = forms.CharField(max_length=40)


class ProfesoresFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    materia = forms.CharField(max_length=40)
    
