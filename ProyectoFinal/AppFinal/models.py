from django.db import models
from django.contrib.auth.models import User

class Pelicula(models.Model):

    nombre = models.CharField(max_length=40)
    subtitulo = models.CharField(max_length=40)
    imagenpelicula = models.ImageField(upload_to='pelicula/', null=True, blank=True)
    descripcion = models.CharField(max_length=600)
    reseña = models.CharField(max_length=600)
    youtube = models.URLField()

    def _str_(self):
        return f'{self.nombre} - {self.subtitulo}'

    
class Serie(models.Model):

    nombre = models.CharField(max_length=40)
    subtitulo = models.CharField(max_length=40)
    imagenserie = models.ImageField(upload_to='pelicula/', null=True, blank=True)
    temporada = models.IntegerField()
    descripcion = models.CharField(max_length=600)
    reseña = models.CharField(max_length=600)
    youtube = models.URLField()

    def _str_(self):
        return f'{self.nombre} - {self.temporada}'
    

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    enlace_web = models.URLField(max_length=200, blank=True)
    imagen = models.ImageField(upload_to='#', blank=True)

class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', blank=True, null=True)

class Comentario(models.Model):
    comentario = models.ForeignKey(Pelicula, related_name='comentarios', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    mensaje = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaComentario']

    def __str__(self):
        return '%s - %s' % (self.nombre, self.comentario)