# docker-basics

Docker
-------

Podman
-------
Podman es un motor de contenedores que NO necesita correr un servicio (**daemonless**) como Docker lo hace.
Sirve para desarrollar, gestionar y correr Contenedores OCI en Linux.
Contenedores pueden correr como un usuario normal (**rootless**), no es necesario ser **root**

```bash
# podemos hacer que reemplace a Docker
# simplemente usando el comando alias
# y todo funcionará igual o mejor
alias docker=podman
```

Terminología
-------------
**Imágenes**: El sistema de archivos y configuración de la aplicación usada para crear contenedores.

**Contenedores**: Instancias de imágenes. Comparten Kernel con otras imágenes y corren como procesos aislados.

**Docker Daemon**: El servicio (background service) que gestiona la construcción, ejecución y distribución de contenedores.

**Docker Client**: El comando (CLI) que permite interactuar con el Daemon.

**Docker Store**: El registro de imágenes de Docker.

Comandos
----------
```bash
# descarga la imagen de Linux Alpine versión 3.12.0
# existen varios repositorios de imágenes de contenedores
# una de las principales es https://hub.docker.com 
# Alpine es una distribución de Linux ultra liviana (aprox. 5mb)
# utiliza Busybox
docker pull alpine:3.12.0 

# lista todas las imágenes en tu sistema
docker images

# corre la imagen del contenedor especificada
# y ejecuta el comando
# luego sale
docker run alpine:3.12.0 ls -l
docker run alpine:3.12.0 echo "hola mundo"
# si deseo correr una terminal 
# debe utilizar los parametros -i (modo interactivo) y -t (tty)
docker run -it alpine:3.12.0 /bin/sh  
# muestra más información sobre la imagen
docker inspect alpine:3.12.0

# ----------------------------------------------------
# EJEMPLO NGINX ESTÁTICO
# ----------------------------------------------------
# -d crea un contenedor desatachado de nuestra terminal (sigue corriendo después de cerrar la terminal)
# -P publica todos los puertos expuestos a puertos aleatorios del Host
# --name permite especificar un nombre para el contenedor y hacer más fácil su referencia
docker run -d -P --name sitio-estatico dockersamples/static-site
# muestra los procesos que están corriendo actualmente
docker ps
# muestra todos los procesos (corriendo y terminados)
docker ps --all
# muestra los puertos expuestos por el contenedor
docker port sitio-estatico

# detiene y luego elimina el contenedor
docker stop sitio-estatico
docker rm sitio-estatico
# un shortcut de lo anterior sería
# donde -f o --force
docker rm -f sitio-estatico

# elimina imagen
docker rmi dockersamples/static-site

# ----------------------------------------------------
# END EJEMPLO NGINX ESTATICO 
# ----------------------------------------------------


```
