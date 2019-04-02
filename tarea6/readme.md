# Práctica 6
## Fotos recursivas


## Información del curso

Proceso Digital de Imagenes - Facultad de Ciencias, UNAM.

* Profesor: Manuel Cristóbal López Michelone
* Ayudante: Yessica Martínez Reyes
* Laboratorio: César Hernández Solís

## Descripción de la práctica

* Fotos recursivas en tonos de grises
* Fotos recursivas en colores reales

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
$ sudo make prepare-env
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

Para la aplicación de un filtro se ejecutará el siguiente comando:
```bash
$ make FILTER_ID="<0|1>" IMG_PATH="img_path" run
```
Opciones de Filtros:
* `0` Fotos recursivas en tonos de grises
* `1` Fotos recursivas en colores reales

Ejemplo de ejecución para aplicación de filtros:
```bash
$ make FILTER_ID="0" IMG_PATH="../test_cases/0.jpg" run
```
```bash
$ make FILTER_ID="1" IMG_PATH="../test_cases/0.jpg" run
```

---

## Comentarios
Agregué unas imágenes para probar los filtros, ubicadas en `/test_cases/*.jpg`.

Hay unas imágenes ya generadas a partir de las que están en 
`/test_cases/*.jpg` en el directorio `/output/*.jpg`, para ver como actúan 
los filtros.

Por el momento los filtros **solo funciona** con imagenes de **500x500**.

Para salir de la interfaz gráfica basta con apretar una tecla cualquiera con 
la aplicación abierta, porque tiene un bug que cuando le das click en cerrar 
se queda zombie el proceso.

Por ser un lenguaje interpretado, la aplicación de filtro llega a ser lenta.

## Integrante(s)

* Ángel Iván Gladín García - *(`angelgladin@ciencias.unam.mx`)*
