# Proyecto del Primer Cuatrimestre Fundamentos de Programación (Curso  \<22\>/\<23\>)
Autor/a: \<Max Cameron Corti\>   uvus:\<NRF5668\>

Aquí debes añadir la descripción del dataset y un enunciado del dominio del proyecto.


## Estructura de las carpetas del proyecto

* **/src**: Contiene los diferentes módulos de Python que conforman el proyecto.
  * **\<modulo1.py\>**: Este modulo contiene una funcione que lea el archivo y para eso utilizo una namedtuple.
  * **\<modulo1_test.py\>**: Para realizar el código aqui simplemente paso el nombre del archivo que contiene los datos sobre los autobuses por la función de leer ficheros, llamada del módulo 1.
  * **\<modulo2.py\>**: Aquí he definido varias funciones que sirven para convertir variables de tipos strings en enteros, floats, booleanos y datetimes. 
* **/data**: Contiene el dataset o datasets del proyecto
    * **\<dataset1.csv\>**: Son unas lineas con varias columnas de información sobre los autobuses de Tussam.
    * **\<dataset2.csv\>**: Para este ejercicio no hacía falta más datasets.
    
## Estructura del *dataset*


La primera línea del dataset es una cabecera que explica a que vienen asignados los valores de cada columna a partir de la segunda fila. Los datos son de algunos autobuses de la empresa Tussam.
El dataset está compuesto por \<7\> columnas, con la siguiente descripción:

* **\<columna 1>**: de tipo \<string\>, representa la matrícula del autobús
* **\<columna 2>**: de tipo \<string\>, representa la fabricante del autobús
* **\<columna 3>**: de tipo \<datetime, en concreto el date\>, representa la fecha de inicio
* **\<columna 4>**: de tipo \<entero\>, representa la capacidad del autobús
* **\<columna 5>**: de tipo \<entero\>, representa el número de asientos en cada autobús
* **\<columna 2>**: de tipo \<string\>, representa el número de kilometros que lleva el autobús
* **\<columna 1>**: de tipo \<bool\>, indica si el autobús está articulado o no

....

## Tipos implementados

He implementado un namedtuple que se encuentra en el módulo 1 para nombrar a los elementos del dataset.
## Funciones implementadas
Añade aquí descripciones genéricas de las funciones, que luego debes acompañar con comentarios de tipo documentación en el código

### \<modulo 1\>

* **<funcion 1>**: Descripción de la función 1.
Es la función: lee_datos_del_fichero() y lea los elementos de un fichero cuando este implementada
* **<funcion 2>**: Descripción de la función 2.
* ...

### \<test modulo 1\>

* **<test funcion 1>**: Descripción de las pruebas realizadas a la función 1.
Meto en la variable "datos" la lista creada por la funcion lee_datos_del_fichero

* 
### \<modulo 2\>

* **<funcion 1>**: Descripción de la función 1.
convertir_entero convierte una variable dada en una entera cuando sea posible
* **<funcion 2>**: Descripción de la función 2.
convertir_float convierte una variable dada en una float cuando sea posible
* **<funcion 3>**: Descripción de la función 3.
convertir_fechas convierte una variable dada en una date cuando sea posible
* **<funcion 4>**: Descripción de la función 4.
convertir_boole convierte una variable dada en una boole cuando sea posible
