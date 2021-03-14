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
# EXEC
# ----------------------------------------------------
# ejecuta la terminal en un contenedor llamado "contenedor" que ya está andando
docker exec -it contenedor /bin/bash

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
# también puede pasar los nombre de varios contenedores a la vez
docker rm -f contenedor1 contenedor2 contenedor3

# elimina imagen
docker rmi dockersamples/static-site


# ----------------------------------------------------
# Ejemplo carga de Dump de MongoDB en Contenedor
# ----------------------------------------------------
podman run -d -p 127.0.0.1:27017:27017 --name basedatos -e MONGO_INITDB_ROOT_USERNAME=mongoadmin -e MONGO_INITDB_ROOT_PASSWORD=secret mongo
# entra en mongoshell
mongo mongodb://mongoadmin:secret@127.0.0.1:27017
# carga dump
mongorestore mongodb://mongoadmin:secret@127.0.0.1:27017/mibd dump



# ----------------------------------------------------
# Variables de Entorno
# ----------------------------------------------------
docker run -d -P --name some-mongo -e MONGO_INITDB_ROOT_USERNAME=mongoadmin -e MONGO_INITDB_ROOT_PASSWORD=secret mongo


# ----------------------------------------------------
# Montar directorio
# ----------------------------------------------------
docker run --name contenedor -v /home/zero/Backups:/tmp/mybackups mongo


# ----------------------------------------------------
# END EJEMPLO NGINX ESTATICO 
# ----------------------------------------------------
```

Ejemplo Dockerfile
--------------------

Todo el código de este ejemplo se encuentra en el dir **python-simple-flask**.


Dockerfile
```Dockerfile
FROM alpine:3.12.0

# si no existe el dir lo crea
# y entra en él
# todo esto en la imagen de alpine
WORKDIR /usr/src/app

# copia todo el directorio actual (host)
# al dir actual de la imagen de contenedor
COPY . .
# elimina el archivo que no es necesario
RUN rm Dockerfile

# instala las dependencias
RUN apk add --update py3-pip
RUN pip install --no-cache-dir -r ./requirements.txt

# expone el puerto
EXPOSE 5000
# igualmente cuando se corra el contenedor se debe
# usar -P ó -p 5000:5000
# docker run -d -P zero/flask

# solo debe existir un CMD dentro del Dockerfile
# este ejecuta el proyecto
CMD ["python3", "./hello.py"]

# finalmente construir la imagen
# docker build -t zero/flask .
```

Fuentes:
---------

- https://podman.io/ 
- https://docs.docker.com/get-started/overview/ 
- https://github.com/docker/labs/tree/master/beginner 
- Mouat, A. (2015). Using Docker. O'reilly. 

