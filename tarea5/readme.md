# Práctica 5
## Oleo, Esteganografía y Sepia


## Información del curso

Proceso Digital de Imagenes - Facultad de Ciencias, UNAM.

* Profesor: Manuel Cristóbal López Michelone
* Ayudante: Yessica Martínez Reyes
* Laboratorio: César Hernández Solís

## Descripción de la práctica

* Sepia
* Oleo (color, tono de gris)
* Esteganografía (ocultar un texto ASCII en una imagen BMP)
    * Ocultar
    * Descubirir

## Entorno

* **`OS`**: Ubuntu 18.04.2 LTS o macOS Mojave 10.14.2
* **`Python`**: Python 3.7.0
* **`pip3`**: pip 18.0
* **`opencv`**: opencv-python==4.0.0.21

## Ejecución del programa

Se creo un archivo `Makefile` para facilitar la preparación del entorno y 
ejecutar el programa.

Se requiere tener el binario `make` instalado. Si estás en Ubuntu basta con poner 
```bash
$ sudo apt install make

```

Antes de proceder a ejecutar el programa, se requiere tener instalado `pip3` 
(un manejador de paquetes de Python 3) y el paquete de OpenCV.
Para esto, lo automaticé con un comando que instala `pip3` en caso de no 
estar instalado e instalar `OpenCV`.


Para instalar las dependencias necesarias (en Ubuntu) se procederá a ejecutar 
el siguiente comando con privelegios de administrador (ósea `sudo`).

Se asume que estás usando Ubuntu, si no, lo tendrás que hacer manual, igual 
no es la gran ciencia.

```bash
$ sudo make prepare-env
```
Si desconfías de esto proceso (por el hecho de hacerlo como 
administrador) o tienes otra distribución de Linux, puedes instalar por 
tu cuenta `pip3` y el paquete`opencv-python==4.0.0.21`.

Una vez ya configurado nuestro entorno de trabajo procederemos a ejecutar 
la aplicación.

---

Para limpiar el proyecto se deberá ejectar el comando:
```bash
$ make clean
```

---

Para la aplicación de un filtro se ejecutará el siguiente comando:
```bash
$ make FILTER_ID="<0|1|2>" IMG_PATH="img_path" run_filter
```
Opciones de Filtros:
* `0` Sepia
* `1` Oleo color
* `2` Oleo tono de grises

Ejemplo de ejecución para aplicación de filtros:
```bash
$ make FILTER_ID="0" IMG_PATH="../test_cases/1.jpg" run_filter
```

---

Para esteganografía:

Ejemplo de ejecución para estenografía:
* Para ocultar texto en una imagen
```bash
$ make MODE="1" IMG_PATH="../test_cases/1.jpg" TXT_PATH="../test_cases/1.txt" run_esteg
```
Al ejecutar ese programa se generará la imagen con el texto cifrado en 
`/output/secret.png`.

* Para descubrir texto de una imagen
```bash
$ make MODE="2" IMG_PATH="../test_cases/secret.png" run_esteg
```
Se mostrará el texto que fue cifrado en la imagen.
Tambien se puede mostrar el texto de una imagen que fue cifrada con el 
comando anterior.

---

En el `MODE="1"` o `MODE="2"` se generarán archivos en un nuevo directorio 
llamado `output` en el directorio del proyecto.

## Comentarios
Agregué unas imágenes para probar los filtros, ubicadas en `/test_cases/*.jpg`.

Para salir de la interfaz gráfica basta con apretar una tecla cualquiera con 
la aplicación abierta, porque tiene un bug que cuando le das click en cerrar 
se queda zombie el proceso.

Por ser un lenguaje interpretado, la aplicación de filtro llega a ser lenta.

## Integrante(s)

* Ángel Iván Gladín García - *(`angelgladin@ciencias.unam.mx`)*
