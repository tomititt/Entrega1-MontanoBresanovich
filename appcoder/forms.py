from django import forms

class AsignaturasFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    clase = forms.IntegerField()
