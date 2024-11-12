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
pip install mtcnn
pip install tensorflow
```

## Decisión del filtro a realizar
Después de realizar un _brainstorming_ sobre cuál queríamos que fuera el filtro que íbamos a desarrollar
durante esta práctica, decidimos que queríamos recuperar uno de los primeros filtros populares de nuestra generación,
el perro de snapchat.

<img src="assets%2Fdog%20filter.png" width="50%">

