from django import forms

class EstudianteForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    camada = forms.IntegerField()

class BuscarEstudianteForm(forms.Form):
    nombre = forms.CharField(max_length=40)

class ProfesorForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    curso = forms.CharField(max_length=40)

class BuscarProfesorForm(forms.Form):
    nombre = forms.CharField(max_length=40)

class CursoForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    camada = forms.IntegerField()

class BuscarCursoForm(forms.Form):
    nombre = forms.CharField(max_length=40)

class AdminForm(forms.Form):
    nombre_estudiante = forms.CharField(max_length=40)
    apellido_estudiante = forms.CharField(max_length=40)
    nombre_profesor = forms.CharField(max_length=40)
    apellido_profesor = forms.CharField(max_length=40)
    curso = forms.CharField(max_length=40)
    camada = forms.IntegerField()