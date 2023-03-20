from django.urls import path
from WebApp import views

urlpatterns = [
    path('', views.inicio, name="WebAppInicio"),
    path('estudiantes/', views.estudiantes, name="WebAppEstudiantes"),
    path('estudiantes/crear', views.crear_estudiante, name="WebAppCrearEstudiantes"),
    path('estudiantes/buscar', views.buscar_estudiante, name="WebAppBuscarEstudiantes"),
    path('profesores/', views.profesores, name="WebAppProfesores"),
    path('profesores/crear', views.crear_profesor, name="WebAppCrearProfesor"),
    path('profesores/buscar', views.buscar_profesor, name="WebAppBuscarProfesor"),
    path('cursos/', views.cursos, name="WebAppCursos"),
    path('cursos/crear', views.crear_curso, name="WebAppCrearCurso"),
    path('cursos/buscar', views.buscar_curso, name="WebAppBuscarCurso"),
    path('administracion', views.admin, name="WebAppAdmin"),
    path('administracion/add', views.add_admin, name="WebAppAdminAdd"),
]
