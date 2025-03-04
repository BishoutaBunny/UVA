#!/bin/bash:
#Esta línea se llama shebang y le dice al sistema que este script debe ejecutarse usando el intérprete de Bash.
#Es necesario para que el sistema sepa cómo ejecutar el script.

gunicorn -w 4 -b 0.0.0.0:5000 app:app:
#este es el comando que inicia tu aplicación Flask usando Gunicorn.
#gunicorn: Es el servidor WSGI que se usa para servir aplicaciones Python en producción.

#-w 4: Especifica el número de workers (procesos) que Gunicorn usará para manejar solicitudes. En este caso, se configuran 4 workers.
#Los workers permiten que tu aplicación maneje múltiples solicitudes al mismo tiempo, lo que mejora el rendimiento.

#-b 0.0.0.0:5000: Define la dirección y el puerto en el que Gunicorn escuchará las solicitudes.
#0.0.0.0 significa que Gunicorn escuchará en todas las interfaces de red (es decir, la aplicación será accesible desde cualquier dirección IP).
#5000 es el puerto en el que se ejecutará la aplicación.

app:app: Especifica cómo Gunicorn debe encontrar tu aplicación Flask.
#El primer app es el nombre del archivo Python (por ejemplo, app.py).
#El segundo app es el nombre de la instancia de Flask dentro de ese archivo.
