# Proyecto 1
## FotoMorsaicos


## Información del curso

Proceso Digital de Imagenes - Facultad de Ciencias, UNAM.

* Profesor: Manuel Cristóbal López Michelone
* Ayudante: Yessica Martínez Reyes
* Laboratorio: César Hernández Solís

## Descripción de la práctica

Viene en el `doc.pdf`.

## Entorno

* **`OS`**: Ubuntu 18.04.2 LTS o macOS Mojave 10.14.2
* **`Python`**: Python 3.7.0
* **`pip3`**: pip 18.0
    * **`opencv-python==4.0.0.21`**
    * **`numpy==1.16.1`**


## Ejecución del programa

Se creo un archivo `Makefile` para facilitar la preparación del entorno y 
ejecutar el programa.

Se requiere tener el binario `make` instalado. Si estás en Ubuntu basta con poner 
```bash
$ sudo apt install make

```

Antes de proceder a ejecutar el programa, se requiere tener instalado `pip3` 
(un manejador de paquetes de Python 3) y el paquete de OpenCV y numpy.
Para esto, lo automaticé con un comando que instala `pip3` en caso de no 
estar instalado e instalar las dependencias necesarias.


Para instalar las dependencias necesarias (en Ubuntu) se procederá a ejecutar 
el siguiente comando con privelegios de administrador (ósea `sudo`).

Se asume que estás usando Ubuntu, si no, lo tendrás que hacer manual, igual 
no es la gran ciencia.

```bash
$ sudo make install_deps
```
Si desconfías de esto proceso (por el hecho de hacerlo como 
administrador) o tienes otra distribución de Linux, puedes instalar por 
tu cuenta `pip3` los paquetes arriba mencionados.

Una vez ya configurado nuestro entorno de trabajo procederemos a ejecutar 
la aplicación.

---

Para limpiar el proyecto (siempre realizar esta acción antes de 
ejecutar el programa) se deberá ejectar el comando:
```bash
$ make clean
```

---

**Muy importante seguir los pasos en el orden indicado para su correcto funcionamiento**

---

Al poner `make` vienen instrucciones y el uso de cada comando.

---

Primero se deberá ejecutar el comando siguiente para preparar el ambiente
del proyecto. Éste comando creará carpetas necesarias para su correcto funcionamiento.
```bash
$ make prepare_env
```

Después se deberán importar la galería de fotos a usar (en nuestro caso el profesor 
nos otorgó una galería) y poner todas las fotos en directorio dentro del proyecto
`/input/images/`.

Una vez hecho ésto, se comprimirán las fotos para poder manipularlas eficientemente.
Para hacer dicho proceso se deberá ejecutar
```bash
$ make run_compressor IMAGES_PATH=input/images/
```
Al finalizar se mostrará un mensaje que dirá
> Imágenes comprimidas satisfactoriamente :D

Ahora se deberán indexar todas la fotos, para esto se deberá ejecutar el 
siguiente comando
```bash
$ make run_image_indexer
```
Y al finalizar aparecerá un mensaje como el siguiente
> Se creo satisfactoriamente el archivo que indexa la imágenes :D

---

Para la aplicación se un *foto morsaico* se deberá aplicar de la siguiente manera
```bash
$ make run_filter IMG_PATH=input/0.jpg
```
Donde `0.jpg` es una imagen a la que le queremos aplicar el filtro, 
**muy importante** debe de estar en `/input/`.

---

Al finalizar, se habrá generado un HTML con con el filtro aplicado en la directorio 
de `output` con un nombre generado por un *UUID*.

## Comentarios
Se uso la métrica lineal.

Se dejaron imágenes preprocesadas para probarlo en `tmp/imgs` y un archivo que 
las indexa sin necesidad de una biblioteca, por lo que si se quiere probar se 
puede usar solo usando `make run_filter IMG_PATH=input/`.

## Integrante(s)

* Ángel Iván Gladín García - *angelgladin@ciencias.unam.mx*
