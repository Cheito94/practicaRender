from typing import Counter
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Genero,Pelicula,Director,Pais,Cine
from django.contrib import messages 
# Create your views here.
def home(request):
    return render(request, 'home.html')

#RENDERIZANDO EL TEMPLATE
#listadoGeneros
# Renderizando el template de ListadoGenero
def listadoGeneros(request):
    generosBdd = Genero.objects.all()
    # Contar descripciones por cada género
    genero_counts = Counter([genero.nombre for genero in generosBdd])
    context = {
        'generos': generosBdd,
        'nombres': list(genero_counts.keys()), # Nombres de los géneros
        'descripciones_count': list(genero_counts.values()) # Conteo de descripciones por género
    }
    return render(request, 'listadoGeneros.html', context)

#listadoPaises
def listadoPaises(request):
    paisesBdd=Pais.objects.all()
    return render(request,'listadoPaises.html', {'paises':paisesBdd})

#listadoDirectores
def listadoDirectores(request):
    directoresBdd=Director.objects.all()
    return render(request,'listadoDirectores.html', {'directores':directoresBdd})

#listadoPeliculas
def listadoPeliculas(request):
    peliculasBdd=Pelicula.objects.all()
    return render(request,'listadoPeliculas.html', {'peliculas':peliculasBdd})

#SE RECIBE EL ID PARA ELIMINAR
#Genero
def eliminarGenero(request,id):
    generoEliminar = Genero.objects.get(id=id)
    generoEliminar.delete()
    messages.success(request, 'Genero eliminado con éxito')
    return redirect('listadoGeneros')
#Director
def eliminarDirector(request,id):
    directorEliminar = Director.objects.get(id=id)
    directorEliminar.delete()
    messages.success(request, 'Director eliminado con éxito')
    return redirect('listadoDirectores')
#Pais
def eliminarPais(request,id):
    paisEliminar = Pais.objects.get(id=id)
    paisEliminar.delete()
    messages.success(request, 'Pais eliminado con éxito')
    return redirect('listadoPaises')

#RENDERIZANDO NUEVOS FORMULARIOS
def nuevoGenero(request):
    return render(request, 'nuevoGenero.html')
#Director
def nuevoDirector(request):
    return render(request, 'nuevoDirector.html')
#Pais
def nuevoPais(request):
    return render(request, 'nuevoPais.html')

#INGRESO DE DATOS EN LA BDD
#Genero
def guardarGenero(request):
    nom=request.POST['nombre']
    desc=request.POST['descripcion']#POST con corchete
    fot=request.FILES.get("foto")#get con parentesis
    nuevoGenero=Genero.objects.create(nombre=nom,descripcion=desc,foto=fot)
    messages.success(request, 'Genero guardado con éxito')
    return redirect('listadoGeneros')

#Director
def guardarDirector(request):
    dni=request.POST['dni']
    nom=request.POST['nombre']
    ape=request.POST['apellido']
    fot=request.FILES.get("foto")
    nuevoDirector=Director.objects.create(dni=dni,nombre=nom,apellido=ape,foto=fot)
    messages.success(request, 'Director guardado con éxito')
    return redirect('listadoDirectores')

#Pais
def guardarPais(request):
    nom=request.POST['nombre']
    cont=request.POST['continente']
    capt=request.POST['capital']
    nuevoPais=Pais.objects.create(nombre=nom,continente=cont,capital=capt)
    messages.success(request, 'Pais guardado con éxito')
    return redirect('listadoPaises')

#RENDERIZANDO FORMULARIO DE ACTUALIZACION
#Genero
def editarGenero(request,id):
    generoEditar = Genero.objects.get(id=id)
    return render(request, 'editarGenero.html', {'generoEditar':generoEditar})

#Director
def editarDirector(request,id):
    directorEditar = Director.objects.get(id=id)
    return render(request, 'editarDirector.html', {'directorEditar':directorEditar})

#Pais
def editarPais(request,id):
    paisEditar = Pais.objects.get(id=id)
    return render(request, 'editarPais.html', {'paisEditar':paisEditar})

#ACTUALIZANDO DATOS
#Genero
def procesarActualizacionGenero(request):
    id=request.POST['id']
    nombre=request.POST['nombre']
    descripcion=request.POST['descripcion']
    generoConsultado=Genero.objects.get(id=id)
    generoConsultado.nombre=nombre
    generoConsultado.descripcion=descripcion
    generoConsultado.save()
    messages.success(request, 'Genero actualizado con éxito')
    return redirect('listadoGeneros')

#Director
def procesarActualizacionDirector(request):
    id=request.POST['id']
    dni=request.POST['dni']
    nombre=request.POST['nombre']
    apellido=request.POST['apellido']
    foto=request.FILES.get('foto')
    directorConsultado=Director.objects.get(id=id)
    directorConsultado.dni=dni
    directorConsultado.nombre=nombre
    directorConsultado.apellido=apellido
    directorConsultado.foto=foto
    directorConsultado.save()
    messages.success(request, 'Director actualizado con éxito')
    return redirect('listadoDirectores')

#Pais
def procesarActualizacionPais(request):
    id=request.POST['id']
    nombre=request.POST['nombre']
    continente=request.POST['continente']
    capital=request.POST['capital']
    paisConsultado=Pais.objects.get(id=id)
    paisConsultado.nombre=nombre
    paisConsultado.continente=continente
    paisConsultado.capital=capital
    paisConsultado.save()
    messages.success(request, 'Pais actualizado con éxito')
    return redirect('listadoPaises')

#Cines
def gestionCines(request):
    return render(request,'gestionCines.html')

def guardarCine(request):
    nom=request.POST['nombre']
    dir=request.POST['direccion']
    tel=request.POST['telefono']
    nuevoCine=Cine.objects.create(nombre=nom,direccion=dir,telefono=tel)
    return JsonResponse({
        'estado':True,
        'mensaje':'Cine registrado exitosamente',
    })

#Renderizando listadoCines
def listadoCines(request):
    cinesBdd=Cine.objects.all()
    return render(request,'listadoCines.html', {'cines':cinesBdd})


#--------------------------Director fetch-----------------------
def director(request):
    return render(request,'director.html')

def listaDirector(request):
    directores=Director.objects.all()
    return render(request,'listaDirector.html',{'directores':directores})

#Guardar Director
def guardarDirector(request):
    dni=request.POST['dni']
    nom=request.POST['nombre']
    ape=request.POST['apellido']
    fot=request.FILES.get("foto")
    nuevoDirector=Director.objects.create(dni=dni,nombre=nom,apellido=ape,foto=fot)
    return JsonResponse({'estado': True, 'mensaje': 'Director guardado correctamente'})

#-----------------------Estadistica----------------------------------
def estadPeliGenero(request):
    return render(request,'estadPeliGenero.html')