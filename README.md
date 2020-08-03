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

Comandos
----------
```bash
# descarga la imagen de Linux Alpine versión 3.12.0
# existen varios repositorios de imágenes de contenedores
# una de las principales es https://hub.docker.com 
# Alpine es una distribución de Linux ultra liviana (aprox. 5mb)
# utiliza Busybox
docker pull alpine:3.12.0 

```
