Practica Creativa 2 

Debido a que tenemos que entregar un fichero zip con los archivos necesarios para cada tarea, hemos establecido un orden de ejecucion:

-Se generará un fichero por cada tarea requerida 
-Esa misma tarea llamara al github de la practica (git clone (https://github.com/Nerio-Messino/Repositorio_Instancias.git) para descargar las cosas necesarias como las instalaciones previas y los ficheros de la aplicacion 
-Cada fichero implementará las funciones requeridas que se pide en las prácticas.

Algo a mencionar es que hemos tenido que crear un repositorio de github para poder tener la app pero con el fichero requierements.txt ligeramente distinto , quitando algunas versiones .
En el bloque 1 se nos pide desplegar la aplicacion en una maquina virtual , de manera que : 
*Se pide inspeccionar el código de la aplicación para que en el título aparezca el nombre del grupo que está realizando la práctica. Este valor deberá obtenerse por medio de la variable de entorno <GRUPO_NUMERO>. También deberá arrancar la aplicación en un puerto diferente al predeterminado.*

*Se requiere que la aplicación sea accesible desde el exterior por medio de la IP pública que tenga asignada la VM, por ejemplo: http://<ip-publica>:<puerto>/productpage*

Por tanto nuestro codigo accede a la variable de entorno GROUP_NUMBER ( que en nuestro caso es el 03 ) y lo pone al lado del titulo.

En el bloque 2 se nos pide desplegar la aplicacion pero usando un dockerfile .de manera que :
*Definir el fichero Dockerfile para ejecutar la aplicación web en el puerto 9080*

*Crear la imagen de docker usando el siguiente formato: <numero_de_grupo>/product-page  donde product-page es el nombre del servicio por lo que no es necesario cambiarlo a diferencia de <numero_de_grupo>*

*Pasar la variable de entorno <GROUPO_NUMERO> al contenedor para que se muestre en el título de la página (en la etiquéta “title” de la página html servida) el número del grupo.*

*Arrancar el contenedor con el nombre siguiendo el siguiente formato <numero_de_grupo>-<nombre_del_servicio> y que la web sea accesible desde el exterior.*

Hemos creado el docker con: *sudo docker build -t 03/productpage*
y luego lo hemos inicializado con *sudo docker run -p 9080:9080 - t 03/productpage*
Cabe destacar que hemos tenido que instalar docker y docker compose en la maquina virtual y luego para poder ejecutar el docker , hemos tenido que hacer que se descargarse git antes de clonar el repositorio ya que con la imagen de python 3.7.7-slim nos decia que no era capaz de llevar cosas como "git" ya que es una imagen ligera.
