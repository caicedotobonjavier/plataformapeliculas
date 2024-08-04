# plataformapeliculas
Este repositorio almacenara un proyecto de una plataforma de películas

Se realizara con Django Rest Framework

tendra solo 2 app, una de usuario donde se realizara lo siguiente:

APP Users

1 -> se crearan los usuario con serializadores, el serializador primero valida que la informacion del usuario este correcta y que las contraseñas coindidan, este al crear un usuario nuevo enviara un correo electronico a el correo registrado por el usuario

2-> lo redireccionara a activar el usuario, donde debera ingresar el codigo recibido por correo y si este es correcto activara la cuenta

3-> se crearan los perfiles que usuario desee tener y cuando este vea una pelicula esta se registrara con el perfil

4-> se tendra tambien la funcionalidad de validar por token los usuarios, cambiar sus contraseñas de usuario y perfiles


APP Movies

en esta app se registraran las peliculas y sus categorias y se realizara lo seguiente:

1-> con serializador se registraran las nuevas categorias

2-> con serializador se registraran las nueva peliculas

3-> este contendra el seguir_viendo que es la lista de las peliculas que se han visto desde un perfil

