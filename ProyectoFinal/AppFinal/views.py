from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView,CreateView
from django.http import HttpRequest,HttpResponse
from .models import *
from .forms import FormPelicula,FormSerie, CustomRegistrationForm, UserEditForm, AvatarFormulario,FormularioComentario
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse_lazy


def lista_peliculas(req):
    peliculas = Pelicula.objects.all()
    return render(req, "lista_peliculas.html", {"lista_peliculas": peliculas})


def lista_series(req):
    series = Serie.objects.all()
    return render(req, "lista_series.html", {"lista_series": series})


def inicio(req):
    try:
        avatar = Avatar.objects.get(user=req.user.id)
        return render(req, "inicio.html", {"url_avatar": avatar.imagen.url})
    except:
        return render(req, "inicio.html")

def peliculas(req, start=0):
    cant_por_pagina = 8

    if req.GET.get('direction') == 'next':
        start += 1
    elif req.GET.get('direction') == 'previous':
        start -= 1

    inicio = int(start)*cant_por_pagina
    final = (int(start) + 1)*cant_por_pagina
    lista_peliculas = Pelicula.objects.all()[inicio:final]

    return render(req, "peliculas.html", {"lista_peliculas": lista_peliculas, "current_page": start})


def series(req, start=0):
    cant_por_pagina = 8

    if req.GET.get('direction') == 'next':
        start += 1
    elif req.GET.get('direction') == 'previous':
        start -= 1

    inicio = int(start)*cant_por_pagina
    final = (int(start) + 1)*cant_por_pagina
    lista_series = Serie.objects.all()[inicio:final]

    return render(req, "series.html", {"lista_series": lista_series, "current_page": start})

def usuarios(req):
    return render(req, "inicio.html")

def error(req):
    return render(req, "error404.html")

def nosotros(req):
    return render(req, "nosotros.html")

def detalle_pelicula(req):
    return render(req, "detallePelicula.html")


# CRUD PELICULAS
# @staff_member_required(login_url='/app-final/login')


# Funcion Crear Pelicula

def crear_pelicula(request):
    if request.method == 'POST':
        form = FormPelicula(request.POST, request.FILES)
        if form.is_valid():
            data=form.cleaned_data
            pelicula=Pelicula(
                nombre=data['nombre'],
                subtitulo=data['subtitulo'],
                imagenpelicula=data['imagen'],
                descripcion=data['descripcion'],
                reseña=data['reseña'],
                youtube=data['youtube'])
            pelicula.save()

            return render(request,"formPelicula.html")
    else:
        form = PeliculaForm()
    return render(request, 'formPelicula.html', {'form': form})

# Funcion Eliminar Pelicula

def eliminar_pelicula(req, id):

    if req.method == 'POST':

        pelicula = Pelicula.objects.get(id=id)
        pelicula.delete()

        pelicula = Pelicula.objects.all()

        return render(req, "lista_peliculas.html", {"peliculas": peliculas})

# Funcion Editar Pelicula
    
def editar_pelicula(req, id):
        
    pelicula = Pelicula.objects.get(id=id)

    if req.method == 'POST':

        miFormulario = FormPelicula(req.POST, req.FILES)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            pelicula.nombre=data["nombre"]
            pelicula.subtitulo=data["subtitulo"]
            pelicula.imagenpelicula=data["imagen"]
            pelicula.descripcion=data["descripcion"]
            pelicula.reseña=data["reseña"]
            pelicula.youtube=data["youtube"]
            pelicula.save()

            return render(req, "inicio.html")
    else:

        miFormulario = FormPelicula(initial={
            "nombre": pelicula.nombre,
            "subtitulo": pelicula.subtitulo,
            "imagen": pelicula.imagenpelicula,
            "descripcion": pelicula.descripcion,
            "reseña": pelicula.reseña,
            "youtube": pelicula.youtube,
        })
        return render(req, "editarPelicula.html", {"miFormulario": miFormulario, "id": pelicula.id})

# CRUD SERIES

# Funcion Crear Serie

def crear_serie(request):
    if request.method == 'POST':
        form = FormSerie(request.POST, request.FILES)
        if form.is_valid():
            data=form.cleaned_data
            serie=Serie(
                nombre=data['nombre'],
                subtitulo=data['subtitulo'],
                imagenserie=data['imagen'],
                temporada=data ['temporada'],
                descripcion=data['descripcion'],
                reseña=data['reseña'],
                youtube=data['youtube'])
            serie.save()

            return render(request,"formSerie.html")
    else:
        form = FormSerie()
    return render(request, 'formSerie.html', {'form': form})

# Funcion Eliminar Serie

def eliminar_serie(req, id):

    if req.method == 'POST':

        serie = Serie.objects.get(id=id)
        serie.delete()

        serie = Serie.objects.all()

        return render(req, "lista_series.html", {"series": series})

# Funcion Editar Serie
    
def editar_serie(req, id):
        
    serie = Serie.objects.get(id=id)

    if req.method == 'POST':

        miFormulario = FormSerie(req.POST, req.FILES)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            serie.nombre=data["nombre"]
            serie.subtitulo=data["subtitulo"]
            serie.imagenserie=data["imagen"]
            serie.temporada=data["temporada"]
            serie.descripcion=data["descripcion"]
            serie.reseña=data["reseña"]
            serie.youtube=data["youtube"]
            serie.save()

            return render(req, "inicio.html")
    else:

        miFormulario = FormSerie(initial={
            "nombre": serie.nombre,
            "subtitulo": serie.subtitulo,
            "imagen": serie.imagenserie,
            "temporada": serie.temporada,
            "descripcion": serie.descripcion,
            "reseña": serie.reseña,
            "youtube": serie.youtube,
        })
        return render(req, "editarSerie.html", {"miFormulario": miFormulario, "id": serie.id})


# BUSQUEDA

def busquedaPelicula(req):
    return render(req,"busquedaPelicula.html")

def buscar(req:HttpRequest):
    if req.GET["nombre"]:
        nombre=req.GET["nombre"]
        nombres=Pelicula.objects.filter(nombre__icontains=nombre)
        return render(req, "resultadoBusqueda.html",{"nombres":nombres})
    
    else:
        return HttpResponse(f'Debe agregar una pelicula')
    
class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ['nombre', 'subtitulo', 'imagenpelicula', 'descripcion', 'reseña', 'youtube']

# LOGIN

def loginView(req):

    if req.method == 'POST':

        miFormulario = AuthenticationForm(req, data=req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            usuario = data["username"]
            psw = data["password"]

            user = authenticate(username=usuario, password=psw)
            if user:
                login(req, user)
                return render(req, "inicio.html", {"mensaje": f"Bienvenido usuario {usuario}!"})
            
        return render(req, "inicio.html", {"mensaje": f"Datos incorrectos"})
    else:
        miFormulario = AuthenticationForm()
        return render(req, "login.html", {"miFormulario": miFormulario})

# REGISTRO

def register(req):
    if req.method == 'POST':
        miFormulario = CustomRegistrationForm(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            usuario = data["username"]

            miFormulario.save()
            return render(req, "inicio.html", {"mensaje": f"Usuario {usuario} creado con éxito!"})
        
        return render(req, "inicio.html", {"mensaje": f"Formulario invalido"})

    else:
        miFormulario = CustomRegistrationForm()
        return render(req, "registro.html", {"miFormulario": miFormulario})

# EDITAR PERFIL

def editar_perfil(req):

    usuario = req.user
    if req.method == 'POST':

        miFormulario = UserEditForm(req.POST, instance=req.user)

        if miFormulario.is_valid():
            
            data = miFormulario.cleaned_data
            usuario.email = data["email"]
            usuario.username = data["username"]
            usuario.set_password(data["password1"])
            usuario.save()

            return render(req, "inicio.html", {"mensaje": "Datos actualizados con éxito!"})
        else:
            return render(req, "editarPerfil.html", {"miFormulario": miFormulario})

    else:
        miFormulario = UserEditForm(instance=usuario)
        return render(req, "editarPerfil.html", {"miFormulario": miFormulario})

# LOGOUT

# MODELOS BASADOS EN VISTAS

class CursoList(LoginRequiredMixin, ListView):
    model = Pelicula
    template_name = "lista_peliculas.html"
    context_object_name = "peliculas"

class PeliculaDetalle(LoginRequiredMixin, DetailView):
    model = Pelicula
    context_object_name = 'pelicula'
    template_name = 'detallePelicula.html'
    
# avatar
@login_required 
def agregar_avatar(req):

    if req.method == 'POST':

        miFormulario = AvatarFormulario(req.POST, req.FILES)

        if miFormulario.is_valid():            
            data = miFormulario.cleaned_data
            avatar = Avatar(user=req.user, imagen=data["imagen"])
            avatar.save()

            return render(req, "inicio.html", {"mensaje": "Avatar actualizados con éxito!"})

    else:
        miFormulario = AvatarFormulario()
        return render(req, "avatar.html", {"miFormulario": miFormulario})

    
# COMENTARIOS

class ComentarioPagina(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = FormularioComentario
    template_name = 'comentario.html'
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        form.instance.comentario_id = self.kwargs['pk']
        return super(ComentarioPagina, self).form_valid(form)

