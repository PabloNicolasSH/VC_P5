# PRÁCTICA 5. VISIÓN POR COMPUTADOR

> Trabajo realizado por:
> - David Koschel Henríquez
> - Pablo Nicolás Santana Hernández

## Preparación del _Environment_ de Conda
Creamos un entorno para el desarrollo de la práctica con los siguientes comandos:
```
conda create --name VC_P5 python=3.11.5
conda activate VC_P5
```
Y en este entorno instalamos las siguientes librerías de las que hacemos uso:
```
pip install opencv-python
pip install mediapipe
pip install tensorflow
```

## Decisión del filtro a realizar
Después de realizar un _brainstorming_ sobre cuál queríamos que fuera el filtro que íbamos a desarrollar
durante esta práctica, decidimos que queríamos recuperar uno de los primeros filtros populares de nuestra generación,
el perro de snapchat.

<div style="text-align: center">
    <img src="assets%2Fdog%20filter.png" width="200">
</div>

El comportamiento de este filtro sería que se han de colocar las orejas de perro sobre la cabeza y la nariz encima de
la nariz. Además, cuando se abre la boca aparece la lengua del perro. Por si todo esto no fuera suficiente, decidimos que
a las personas impares en la imagen les aparecería el filtro básico y a las pares el de dálmata, para así tener variedad.

## Desarrollo de la Práctica
Empezamos creando un código sencillo para resaltar dónde estaban los puntos que detectaba nuestro modelo. Conociendo los puntos detectados empezamos
a colocarle el filtro y al principio usamos _MTCNN_. Sin embargo, el número de puntos detectados era escaso y no nos permitía hacer correctamente el cálculo de apertura
de la boca para la aparición de la lengua. Es por eso, que decidimos probar con _dlib_, pero como nos daba problemas, saltamos
directamente a usar _MediaPipe_ de _Google_. Con el detector correcto en marcha pudimos terminar de desarrollar la práctica y generar nuestro filtro.

# Trabajo desarrollado
## Archivos de imagen necesarios
- `dog_ears.png`: Orejas de perro
- `dog_nose.png`: Nariz de perro
- `dog_tongue.png`: Lengua de perro (mostrada cuando la boca está abierta)
- `dalmatian_ears.png`: Orejas de dálmata
- `dalmatian_nose.png`: Nariz de dálmata

## Funcionalidad del código
El código desarrollado contiene una función para el tratamiento de los cosméticos usados y un bucle en el que se colocan estos
cosméticos sobre las caras detectadas. Se hace uso de la variable _**max_num_faces**_ configurada con el valor 3, para solo
colocar los cosméticos sobre las 3 primeras caras detectadas, pero se puede modificar su valor.

### Función overlay_image
La función overlay_image combina imágenes con transparencia en el background en las coordenadas especificadas. La superposición se ajusta
para evitar errores cuando la imagen se sale de los límites del marco.

### Resultado obtenido
El resultado que hemos obtenido es el que se muestra a continuación:

![Resultado1.gif](assets%2Fresults%2FResultado1.gif)
![Resultado2.gif](assets%2Fresults%2FResultado2.gif)

Para poder grabar esta demo generamos una _webcam_ virtual con _OBS_ y grabamos la pantalla, ya que queríamos mostrar el resultado con dos personas a la vez.
