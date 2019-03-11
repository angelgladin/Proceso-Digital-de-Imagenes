# Práctica 4
## Quitar marcas de agua


## Información del curso

Proceso Digital de Imagenes - Facultad de Ciencias, UNAM.

* Profesor: Manuel Cristóbal López Michelone
* Ayudante: Yessica Martínez Reyes
* Laboratorio: César Hernández Solís

## Descripción de la práctica

* Quitar la marca de agua

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
make IMG_PATH="img_path" run 
```
donde en el parámetro `IMG_PATH` estará la ruta de la imagen.

---

Ejemplo de ejecución:
```bash
make IMG_PATH="../imagenes-marca-agua/einvigi_10_halldor_1.jpg" run
```

## Comentarios
Solamente funciona con los filtros de agua de las imágenes que el maestro nos dió.

Al final de la ejecución se mostrarña en pantalla la imagen sin marca de agua.

## Integrante(s)

* Ángel Iván Gladín García - *(`angelgladin@ciencias.unam.mx`)*
