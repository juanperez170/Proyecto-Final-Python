from django.urls import path
from django.contrib.auth.views import LogoutView
from AppFinal.views import *


urlpatterns = [
    path('',inicio,name="inicio"),
    path('peliculas/',peliculas, name="peliculas"),
    path('series/',series, name="series"),
    path('usuarios/',usuarios, name="usuarios"),
    path('formulario-pelicula/',crear_pelicula,name="formularioPelicula"), 
    path('lista-peliculas/', lista_peliculas, name='ListaPeliculas'),
    path('busqueda-pelicula/',busquedaPelicula,name="BusquedaPelicula"),
    path('buscar/',buscar,name="Buscar"),
    path('error/',error,name="error404"),
    path('eliminarPeliculas/<int:id>', eliminar_pelicula, name="EliminarPeliculas"),
    path('editarPelicula/<int:id>', editar_pelicula, name="EditarPelicula"),
    path('formulario-serie/',crear_serie,name="formularioSerie"), 
    path('lista-series/', lista_series, name='ListaSeries'),
    path('eliminarSeries/<int:id>', eliminar_serie, name="EliminarSeries"),
    path('editarSerie/<int:id>', editar_serie, name="EditarSerie"),
    path('login/', loginView, name="Login"),
    path('register/', register, name="Registrar"),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name="Logout"),
    path('editar-pefil/', editar_perfil, name="EditarPefil"),
    path('nosotros/', nosotros, name="Nosotros"),
    path('detallePelicula/<int:pk>/', PeliculaDetalle.as_view(), name='pelicula'),
    path('agregar-avatar/', agregar_avatar, name="AgregarAvatar"),
    path('peliculacomentario/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    

]



