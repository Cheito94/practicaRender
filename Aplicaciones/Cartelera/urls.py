#configurando redireccionamiento
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    #Modelo Genero
    path('listadoGeneros/',views.listadoGeneros, name='listadoGeneros'),
    path('eliminarGenero/<id>',views.eliminarGenero, name='eliminarGenero'),
    path('nuevoGenero/', views.nuevoGenero, name="nuevoGenero"),
    path('guardarGenero/',views.guardarGenero, name="guardarGenero"),
    path('editarGenero/<id>',views.editarGenero, name="editarGenero"),
    path('procesarActualizacionGenero/',views.procesarActualizacionGenero, name="procesarActualizacionGenero"),

    #Modelo Pelicula
    path('listadoPeliculas/',views.listadoPeliculas, name="listadoPeliculas"),

    #Modelo Director
    path('listadoDirectores/',views.listadoDirectores, name="listadoDirectores"),
    path('eliminarDirector/<id>',views.eliminarDirector, name='eliminarDirector'),
    path('nuevoDirector/', views.nuevoDirector, name="nuevoDirector"),
    path('editarDirector/<id>',views.editarDirector, name="editarDirector"),
    path('guardarDirector/',views.guardarDirector, name="guardarDirector"),
    path('procesarActualizacionDirector/',views.procesarActualizacionDirector, name="procesarActualizacionDirector"),
    
    #Modelo Pais
    path('listadoPaises/',views.listadoPaises, name='listadoPaises'),
    path('nuevoPais/', views.nuevoPais, name="nuevoPais"),
    path('guardarPais/',views.guardarPais, name="guardarPais"),
    path('eliminarPais/<id>',views.eliminarPais, name='eliminarPais'),
    path('editarPais/<id>',views.editarPais, name="editarPais"),
    path('procesarActualizacionPais/',views.procesarActualizacionPais, name="procesarActualizacionPais"),

    #Modelos Cines
    path('listadoCines/',views.listadoCines, name='listadoCines'),
    path('gestionCines/',views.gestionCines, name='gestionCines'),
    path('guardarCine/', views.guardarCine, name='guardarCine'),

    #Director fetch
    path('director/',views.director, name="director"),
    path('listaDirector/',views.listaDirector, name="listaDirector"),

    #Tabla de Estadistica
    path('estadPeliGenero/',views.estadPeliGenero, name="estadPeliGenero")

]