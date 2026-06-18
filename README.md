# Proyecto Final - Python - CODERHOUSE

## 👪 Integrantes 
- [Juan Ignacio Perez](https://github.com/JuanIgnacioPerez)


## 📜 Requerimientos 

- Se debera de manera individual. Crearas una aplicaion web estilo blog programada en Python en Django. Esta web tendra admin, perfiles, paginas y formularios
- La entrega se realizara enviando un link de GitHub, en el readme de Github debera estar el nombre completo de los tres/dos participantes y una descripcion de dos o tres renglones contando que hizo cada uno
- En el github debe haber un video o link a video donde nos muestran su web funcionando en no mas de diez minutos.
- Dentro de github debera existir una carpeta con por lo menos 3 casos de pruebas debidamente documentados.
- Contar con algun acceso visible a la vista de "acerca de mi" donde se contara acerca de los dueños de la pagina manejando en el route about/. (En castellano un "acerca de mi" contando un poco de los creadores de la web y del proyecto)
- Contar con algun acceso visible a la vista blogs que debe alojarse en el route page/. (Es decir un html que permite listar todos los blogs del BD, con una informacion minima de dicho blog.)
- Acceder a una pantalla que contendra las paginas. Al clickear en "leer mas" debe navegar al detalle de la page mediante un route pages/<pageld>. (Osea al hacer click se ve mas detalles d elo que se veia en el apartado anterior.)
- Si no existe ninguna pagina mostrar un "No hay paginas aun". (Aclarando, si en la pagina hacemos click en algun lugar que no existe que diga eso, o que lleve un html con esos mensajes, no dejar botones que no respondan.)
- Para crear, editar o eliminar las fotos debe estar registrado como administrador.
- Cada blog, es deecir cada model blog debe tener como minimo, un titulo, subtitulo, cuerpo, autor, fecha y una imagen (minimo y obligatorio, puede tener mas)
- Si los estudiantes deciden resolverlo de manera grupal, deben avisar al tutor y enviarle los nombres de los estudiantes que conforman el grupo de trabajo. Luego, agregar una caratula o instancia en el PF con los nombres de los estudiantes.
- Tener una app de registro donde se puedan registrar los usuarios en el route accounts/signup, un usuario esta compuesto por: email, contraseña y nombre de usuario.
- Tener una app de login en el route accounts/login/ la cual permita loguearse con los datos de administrador o usuario normal.
- Tener una pp de perfiles en el route accounnts/profile/ la cual muestra la info de nuestro usuario y permite poder modificar y/o borrar: imagen, nombre, descripcion, un link a una pagina web, email y contraseña.
  
## 📗 Bibliotecas externas

- Bootstrap
- Fontawesome

## ⬇️ Instalacion
El backend de esta pagina esta subido en vercel, por lo que podriamos utilizarlo realizando los siguientes comandos

1. Clonamos el repositorio
```
https://github.com/juanperez170/Proyecto-Final-Python.git
```
2. Nos posicionamos en la carpeta del Proyecto
```
cd Proyecto
```
3. Verificamos que estemos en la carpeta Proyecto
```
ls
```
4. Iniciamos el servidor
```
python manage.py runserver
```
5. Abrimos la url
```
http://127.0.0.1:8000/app-final
```
6. Una vez situado en la pagina principal se podran observar todas las partes de la pagina, desde el navbar y el footer, hasta las pestañas de productos.
7. Para agregar producto con el formulario, primero nos debemos loguear como administrador en el apartado login del navbar
```
http://127.0.0.1:8000/app-final/login/
```
8. Dirigirnos al apartado "Lista Peliculas" del navbar, seguido por hacer click al boton "Agregar Peliculas"
```
http://127.0.0.1:8000/app-final/lista-peliculas/
```
9. El paso anterior sirve tambien para "Lista Series"
```
http://127.0.0.1:8000/app-final/lista-series/
```
Para verificar que este todo correcto, ingresamos con el usuario admin, para eso entramos a la url
```
http://127.0.0.1:8000/admin
```
y utilizamos como usuario: juanignacio y como contraseña: 123456




