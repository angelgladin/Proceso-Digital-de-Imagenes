# Práctica 1
## Filtros

* Profesor: Manuel Cristóbal López Michelone
* Ayudante: Yessica Martínez Reyes
* Laboratorio: César Hernández Solís

Proceso Digital de Imagenes - Facultad de Ciencias, UNAM.

## Descripción de la práctica

Aplicación de los filtros listados abajo a una imagen dada.

* RGB
* Brillo
* Alto contraste
* Inverso
* Mosaico
* Escala de grises


## Entorno

* **`OS`**: Ubuntu 18.04.2 LTS o macOS Mojave 10.14.2
* **`Python`**: Python 3.7.0
* **`pip3`**: pip 18.0

## Ejecución del programa

Se creo un archivo `Makefile` para facilitar la preparación del entorno y 
ejecutar el programa.

Se requiere tener el binario `make instalado`. Si estás en Ubuntu basta con poner 
```bash
sudo apt install make

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
sudo make prepare-env
```
Si desconfías de esto proceso (por el hecho de hacerlo como 
administrador) o tienes otra distribución de Linux, puedes instalar por 
tu cuenta `pip3` y `opencv-python==4.0.0.21`.

Una vez ya configirado nuestro entorno de trabajo procederemos a ejecutar 
la aplicación.

Para ello teclearemos el siguiente comando:
```bash
make FILTER_ID="<0|1|2|3|4|5|6|7|8>" IMG_PATH="img_path" run 
```
donde en el parámetro de `FILTER_ID` pondremos el identificador del 
filtro (que abajo listo) y en el parámetro de `IMG_PATH` estará la 
ruta de la imagen.

Opciones de Filtro

* `0` Filtro RGB. En este filtro el usuario da los tres valores de la tripleta
(R, G, B).
* `1` Filtro Rojo. En este filtro solo se "pinta" el color rojo de la siguinte 
forma (R, 0, 0).
* `2` Filtro Verde. En este filtro solo se "pinta" el color verde de la siguinte 
forma (0, G, 0).
* `3` Filtro Azul. En este filtro solo se "pinta" el color azul de la siguinte 
forma (0, 0, B).
* `4` Brillo
* `5` Alto contraste
* `6` Inverso
* `7` Mosaico
* `8` Escala de grises

---

Ejemplo de ejecución:
```bash
make FILTER_ID="6" IMG_PATH="../test_cases/2.jpg" run
```

## Comentarios
Agregué unas imágenes para probar los filtros, ubicadas en `/test_cases/*.jpg`.

Para salir de la interfaz gráfica basta con apretar una tecla cualquiera con 
la aplicación abierta, porque tiene un bug que cuando le das click en cerrar 
se queda zombie el proceso.

## Integrante(s)

* Ángel Iván Gladín García - *(`angelgladin@ciencias.unam.mx`)*
