# Importa el módulo 'os' para interactuar con el sistema operativo (por ejemplo, obtener variables de entorno).
import os

# Importa las clases y funciones necesarias de Flask.
from flask import Flask, render_template, request, jsonify

# Crea una instancia de la aplicación Flask.
# - __name__: Indica el nombre del módulo actual.
# - static_folder='static': Especifica la carpeta donde se almacenan los archivos estáticos (CSS, JS, imágenes).
app = Flask(__name__, static_folder='static')

# Variable global para almacenar el índice UV.
indice_uv = "..."  # Valor inicial

# Ruta principal que maneja solicitudes GET y HEAD.
@app.route('/', methods=['GET', 'HEAD'])
def index():
    # Renderiza la plantilla 'index.html' y pasa el valor de 'indice_uv' a la plantilla.
    return render_template('index.html', indice_uv=indice_uv)

# Ruta para recibir datos del índice UV mediante una solicitud POST.
@app.route('/recibir', methods=['POST'])
def recibir():
    # Declara que se usará la variable global 'indice_uv'.
    global indice_uv

    # Intenta recibir los datos en formato JSON.
    data = request.get_json()
    if data and "indice_uv" in data:
        # Si los datos son JSON y contienen "indice_uv", actualiza la variable global.
        indice_uv = data["indice_uv"]
    else:
        # Si no es JSON, intenta recibir los datos como un formulario.
        indice_uv = request.form.get('indice_uv')

    # Si no se recibió ningún valor para 'indice_uv', devuelve un mensaje de error.
    if indice_uv is None:
        return jsonify({"error": "No se recibió índice UV"}), 400  # Código de estado HTTP 400: Bad Request
    
    # Imprime el valor recibido en la consola para depuración.
    print(f"Índice UV recibido: {indice_uv}")

    # Devuelve una respuesta JSON indicando que los datos fueron recibidos correctamente.
    return jsonify({"mensaje": "Datos recibidos", "indice_uv": indice_uv}), 200  # Código de estado HTTP 200: OK

# Ruta para obtener el valor actual del índice UV.
@app.route('/obtener_uv')
def obtener_uv():
    # Devuelve el valor actual de 'indice_uv' en formato JSON.
    return jsonify({"indice_uv": indice_uv})

# Importa nuevamente el módulo 'os' (esto es redundante y puede eliminarse).
import os

# Bloque principal que se ejecuta cuando el script es llamado directamente.
if __name__ == "__main__":
    # Obtiene el puerto de la variable de entorno 'PORT' o usa el puerto 5000 por defecto.
    port = int(os.environ.get("PORT", 5000)) 
    # Inicia la aplicación Flask en modo de depuración, escuchando en todas las interfaces de red (0.0.0.0).
    app.run(debug=True, host="0.0.0.0", port=port)
