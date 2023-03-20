from django.contrib import admin
from WebApp.models import Estudiante, Profesor, Curso

# Register your models here.
admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Curso)