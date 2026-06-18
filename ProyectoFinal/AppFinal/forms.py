from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import *

class FormPelicula(forms.Form):
    nombre = forms.CharField(max_length=40)
    subtitulo = forms.CharField(max_length=40)
    imagen= forms.ImageField(required=False)
    descripcion = forms.CharField(max_length=600)
    reseña = forms.CharField(max_length=600)
    youtube = forms.URLField()

class FormSerie(forms.Form):
    nombre = forms.CharField(max_length=40)
    subtitulo = forms.CharField(max_length=40)
    imagen = forms.ImageField(required=False)
    temporada = forms.IntegerField()
    descripcion = forms.CharField(max_length=150)
    reseña = forms.CharField(max_length=150)
    youtube = forms.URLField()

class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254)
    username = forms.CharField(max_length=30)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Repita Contraseña', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')

class UserEditForm(UserChangeForm):

    email = forms.EmailField(max_length=254)
    username = forms.CharField(max_length=30)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Repita Contraseña', widget=forms.PasswordInput())

    class Meta:
        model=User
        fields = ("email", "username", "password1", "password2")

class AvatarFormulario(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ("imagen",)

class FormularioComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('nombre', 'mensaje')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'mensaje' : forms.Textarea(attrs={'class': 'form-control'}),
             }


