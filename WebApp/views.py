from django.shortcuts import HttpResponse, render, redirect
from WebApp.models import Estudiante, Profesor, Curso
from WebApp.forms import *

def inicio(request):
    #Cargamos pagina de inicio
    return render(request, "WebApp/inicio.html")

def estudiantes(request):
    #Cargamos las forms y la enviamos al HTML
    context = {
        "form": EstudianteForm(),
        "form_buscar": BuscarEstudianteForm(),
    }
    return render(request, "WebApp/estudiantes.html", context=context)

def crear_estudiante(request):
    #Definimos como Crear Estudiantes, tomamos los datos del form y los cargamos en la clase modelo usando metodo POST
    if request.method == "POST":
        mi_formulario = EstudianteForm(request.POST)
        if mi_formulario.is_valid():
            info = mi_formulario.cleaned_data
            estudiante_save = Estudiante(
                nombre=info["nombre"],
                apellido=info["apellido"],
                camada=info["camada"]
            )
            estudiante_save.save()
            return redirect("WebApp/estudiantes.html")
    return render(request, "WebApp/estudiantes.html")

def buscar_estudiante(request):
    # Formulario Buscar, devolvemos los datos encontrados
    mi_formulario = BuscarEstudianteForm(request.GET)
    if mi_formulario.is_valid():
        informacion = mi_formulario.cleaned_data
        estudiantes_filtrados = Estudiante.objects.filter(nombre__icontains=informacion["nombre"])
        context = {
            "estudiantes": estudiantes_filtrados
        }
    return render(request, "WebApp/buscar_estudiante.html", context=context)

def profesores(request):
    # Cargamos las forms y la enviamos al HTML
    context = {
        "form": ProfesorForm(),
        "form_buscar": BuscarProfesorForm(),
    }
    return render(request, "WebApp/profesores.html", context=context)

def crear_profesor(request):
    # Definimos como Crear Profesores, tomamos los datos del form y los cargamos en la clase modelo
    if request.method == "POST":
        mi_formulario = ProfesorForm(request.POST)
        if mi_formulario.is_valid():
            info = mi_formulario.cleaned_data
            profesor_save = Profesor(
                nombre=info["nombre"],
                apellido=info["apellido"],
                cursos=info["curso"]
            )
            profesor_save.save()
            return redirect("WebAppProfesores")
    return render(request, "WebApp/profesores.html")

def buscar_profesor(request):
    # Formulario Buscar, devolvemos los datos encontrados
    mi_formulario = BuscarProfesorForm(request.GET)
    if mi_formulario.is_valid():
        informacion = mi_formulario.cleaned_data
        profesores_filtrados = Profesor.objects.filter(nombre__icontains=informacion["nombre"])
        context = {
            "profesores": profesores_filtrados
        }
    return render(request, "WebApp/buscar_profesor.html", context=context)

def cursos(request):
    # Cargamos las forms y la enviamos al HTML
    context = {
        "form": CursoForm(),
        "form_buscar": BuscarCursoForm(),
    }
    return render(request, "WebApp/cursos.html", context=context)

def crear_curso(request):
    # Definimos como Crear Cursos, tomamos los datos del form y los cargamos en la clase modelo
    if request.method == "POST":
        mi_formulario = CursoForm(request.POST)
        if mi_formulario.is_valid():
            info = mi_formulario.cleaned_data
            curso_save = Curso(
                nombre=info["nombre"],
                camada=info["camada"],
            )
            curso_save.save()
            return redirect("WebAppCursos")
    return render(request, "WebApp/cursos.html")

def buscar_curso(request):
    # Formulario Buscar, devolvemos los datos encontrados
    mi_formulario = BuscarCursoForm(request.GET)
    if mi_formulario.is_valid():
        informacion = mi_formulario.cleaned_data
        cursos_filtrados = Curso.objects.filter(nombre__icontains=informacion["nombre"])
        context = {
            "cursos": cursos_filtrados
            }
    return render(request, "WebApp/buscar_curso.html", context=context)

def admin(request):
    # Cargamos las forms y todos los Estudiantes, Profesores y Cursos y lo enviamos al HTML
    all_estudiantes = Estudiante.objects.all()
    all_profesores = Profesor.objects.all()
    all_cursos = Curso.objects.all()
    context = {
        "form": AdminForm(),
        "estudiantes": all_estudiantes,
        "profesores": all_profesores,
        "cursos": all_cursos
    }
    return render(request, "WebApp/administracion.html", context=context)
def add_admin(request):
    #Añadimos desde un formulario a todas las clases. En este caso no usamos una variable intermedia y cargamos directo a las clases
    if request.method == "POST":
        mi_formulario = AdminForm(request.POST)
        if mi_formulario.is_valid():
            info = mi_formulario.cleaned_data
            Curso(
                nombre=info["curso"],
                camada=info["camada"]
            ).save()
            Estudiante(
                nombre=info["nombre_estudiante"],
                apellido=info["apellido_estudiante"],
                camada=info["camada"]
            ).save()
            Profesor(
                nombre=info["nombre_profesor"],
                apellido=info["apellido_profesor"],
                cursos=info["curso"]
            ).save()

            return redirect("WebAppAdmin")

    return render(request, "WebApp/administracion.html")