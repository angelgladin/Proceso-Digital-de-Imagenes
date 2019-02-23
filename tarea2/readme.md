# Práctica 2
## Filtros de Convoloción



## Información del curso

Proceso Digital de Imagenes - Facultad de Ciencias, UNAM.

* Profesor: Manuel Cristóbal López Michelone
* Ayudante: Yessica Martínez Reyes
* Laboratorio: César Hernández Solís

## Descripción de la práctica

Aplicación de los filtros listados abajo a una imagen dada.

* Blur
* Motion Blur
* Encontrar Bordes
* Sharpen
* Emboss
* Mediana

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
tu cuenta `pip3` y el paquete`opencv-python==4.0.0.21`.

Una vez ya configirado nuestro entorno de trabajo procederemos a ejecutar 
la aplicación.

Para ello teclearemos el siguiente comando:
```bash
make FILTER_ID="<0|1|2|3|4|5>" IMG_PATH="img_path" run 
```
donde en el parámetro de `FILTER_ID` pondremos el identificador del 
filtro (que abajo listo) y en el parámetro de `IMG_PATH` estará la 
ruta de la imagen.

Opciones de Filtros:

* `0` Blur
* `1` Motion Blur
* `2` Encontrar bordes
* `3` Sharpen
* `4` Emboss (En enste filtro se le pedirá al usuario una vez ejecutado 
el programa una opción)
* `5` Mediana

---

Ejemplo de ejecución:
```bash
make FILTER_ID="1" IMG_PATH="../test_cases/1.jpg" run
```

## Comentarios
Agregué unas imágenes para probar los filtros, ubicadas en `/test_cases/*.jpg`.

Para salir de la interfaz gráfica basta con apretar una tecla cualquiera con 
la aplicación abierta, porque tiene un bug que cuando le das click en cerrar 
se queda zombie el proceso.

Como se programo en Python (ser interpretado) la aplicación de los filtros es algo 
lenta, tardándose un tiempo apróximado de *1 minuto* (o menos) en una computadora 
con un procesador `Intel Mobile Core i5 "Kaby Lake" (I5-7360U)`.


## Integrante(s)

* Ángel Iván Gladín García - *(`angelgladin@ciencias.unam.mx`)*
