# Cañon 

Actividad 4. Juego del tiro parabólico

Esta actividad del curso **Herramientas computacionales. El arte de la programación** tiene cómo finalidad mejorar nuestro uso del lenguaje de programación *python* (especialmente de las librerías *freegames* y *turtle*) y aprender el sistema de manejo de versiones *Git* a través de la página web *GitHub* y del uso de una intérfaz de línea de comandos (CLI por sus siglas en inglés) (principalmente este último objetivo). 

Para esta actividad se realizarón cambios en el código del juego de la serpiente (**snake.py**) proveniente de Grant jenks <https://grantjenks.com/docs/freegames/#cannon>, los cambios realizados fueron:

1. Hacer que la velocidad para el proyectil y los balones sea más rápida
2. Hacer que el juego nunca termine, de manera que los balones al salir de la ventana se re posicionen
3. Insertar un boton de autodestrucción


### Descripción 
En este juego gráfico se lanza un proyectil redondo (bola roja) a través de pulsar con el cursor una posición de la ventana perteneciente al juego, el proyectil se lanza exactamente desde el lado inferior izquierdo de la ventana y su trayectoria forma una parábola (de allí su nombre) la posición del cursor al darle click determina el alto y ancho de la parábola. El objetivo del juego es lanzar el proyectil de tal manera que este toque los balones azules (al tocarlos desaparecen) y cuidar que ningún balon azul toque el lado izquierdo de la pantalla. 

### ¿Cómo ejecutarlo?
- Irse a la consola de comandos (bash, zsh, especialmente de tipo UNIX)
- Clonar este repositorio (Comando `git clone https://github.com/AntonioLaurance/FreeGamesCanon.git`)
- Establecer como directorio de trabajo el directorio del repositorio
- Ejecutar el intérprete de *python* con el código de este archivo (comando `python3 cannon.py`)

*Nota: El último comando sólo funciona si se tiene instalada una versión 3 del intérprete de python en la computadora.*
