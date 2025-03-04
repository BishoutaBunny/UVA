En el archivo "render.yaml" se puede ver el siguiente funcionamiento:
services:
#Indica que se van a definir uno o más servicios en Render.
#Un servicio puede ser una aplicación web, una base de datos, un trabajo en segundo plano, etc.

- type: web
#Define el tipo de servicio. En este caso, es una aplicación web (web).
#Esto le dice a Render que este servicio va a manejar tráfico HTTP/HTTPS.

name: flask-app
#Es el nombre que le das a este servicio en Render.
#Puedes elegir cualquier nombre que tenga sentido para tu aplicación.

env: python
#Especifica el entorno de ejecución. En este caso, es python, lo que le indica a Render que tu aplicación está escrita en Python.
#Render usará este entorno para instalar dependencias y ejecutar tu aplicación.

region: oregon
#Define la región donde se desplegará tu aplicación. En este caso, es Oregon (una región de AWS en EE. UU.).
#Render tiene varias regiones disponibles, y puedes elegir la que esté más cerca de tus usuarios.

buildCommand: "pip install -r requirements.txt"
#Es el comando que Render ejecutará para construir tu aplicación.
#En este caso, instala las dependencias de Python listadas en el archivo requirements.txt.

startCommand: "gunicorn app:app"
#Es el comando que Render ejecutará para iniciar tu aplicación.
#Aquí se usa Gunicorn para servir la aplicación Flask. app:app le dice a Gunicorn que busque la aplicación en el archivo app.py y use la instancia llamada app.
