#*********************MEDIDOR UV, CALCULO, ENVIO DE INFORMACION Y DEEPSLEEP ********************************
#***********************************************************************************************

from machine import Pin, ADC, RTC, deepsleep
import time
import network
import urequests
import ujson

#[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
#EJECUCION CONEXION WIFI Y ENVIO DE DATOS A LA PAGINA.
#[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]


WIFI_SSID = "Galaxy A55 5G 54E3" #Se ajusta segun a la red que se quiera conectar
WIFI_PASSWORD = "Sapo1234" #igualmente es la clave de la red
FLASK_URL = "https://uva-th0i.onrender.com/recibir" #Servidor donde se envian los datos  

def conectarWiFi(): #intenta conectar la esp a internet, lo intenta durante 10 iteraciones sino conecta devuelve error
    print("📡 Conectando a WiFi...")
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)

    for i in range(10):
        if wlan.isconnected():
            print("✅ WiFi conectado")
            print("🛜 IP:", wlan.ifconfig()[0])
            return wlan
        print(f"🔁 Intento {i+1} de 10...")
        time.sleep(1)

    print("❌ No se pudo conectar a WiFi")
    return wlan


def enviarAFlask(indiceUV, wlan): #Envia el indice en formato JSON e intenta reconectar a la red si se pierde la conexion
    if not wlan.isconnected():
        print("❌ No hay conexión WiFi, reconectando...")
        wlan = conectarWiFi()
        if not wlan.isconnected():
            return False

    print("📤 Enviando a Flask...")
    datos = ujson.dumps({"indice_uv": round(indiceUV, 1)})
   
    for intento in range(3):
        try:
            respuesta = urequests.post(FLASK_URL, data=datos, headers={"Content-Type": "application/json"})
            print("📡 Flask código:", respuesta.status_code)
            print("📄 Respuesta:", respuesta.text)
            respuesta.close()
            return respuesta.status_code == 200
        except Exception as e:
            print(f"❌ Error enviando a Flask (Intento {intento+1}): {e}")
            time.sleep(2)

    return False


#[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
#EJECUCION CALCULOS INDICE UV
#[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]

# Asignación de pines para LEDs dentro de una lista y asignacion Buzzer
luces=[Pin(2,Pin.OUT), Pin(4,Pin.OUT), Pin(5,Pin.OUT), Pin(18,Pin.OUT), Pin(19,Pin.OUT)]
buz=Pin(13, Pin.OUT)

sensor = ADC(Pin(32))# Configuración del sensor UV
sensor.atten(ADC.ATTN_11DB)  # Rango atenuado de 0 a 3.3V

def voltajeIndice(voltaje): #convierte el voltaje en en rango del indice UV
    return voltaje/0.3  # Sensibilidad del sensor, llega hasta el 11, sensibilidad del sensor, en dado caso que reciba 3.3 voltios, se interpreta como indice de 11 o superior

def lecturaVoltaje():
    valorLeido=sensor.read() #desde 0 hasta 4095, 12 bits
    voltaje=(valorLeido/4095.0) * 3.3  # Conversión a voltaje
    indiceUV=voltajeIndice(voltaje)      # Conversión a índice UV
    print(f"Valor bruto: {valorLeido}, Voltaje: {voltaje}, Índice UV: {indiceUV}") #Muestra de los valores
    return indiceUV

def controlLuces(indiceUV): #funcion para gestionar encendido de luces y buzzer
    niveles=[1,2.51,5.51,7.51,10.51]  # Niveles de índice UV para encender las luces, indices de (1-2),(3-5),(6-7),(8-10),(11+)
   
    for luz in luces: # Apagar todas las luces
        luz.value(0)

    for i, nivel in enumerate(niveles): # Prender luces según el índice UV, enumerate da el indice y el valor de "niveles", nivel seria el valor del indice i
        if (indiceUV>=nivel):
            luces[i].value(1) #el mismo valor de indice se enciende en la lista luces

    # Control del buzzer
    if (indiceUV>=10.51):
        buz.value(1)
        time.sleep(1)
        buz.value(0)
       
#[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
#                               CONFIGURACION DEEPSLEEP
#                                 EJECUCION PRINCIPAL
#[][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
   
rtc=RTC()

# Encender el LED al inicio para indicar que la ESP32 está despierta
print("La ESP32 ha despertado!\n")
luces[0].value(1) #encender primer led para confirmar
time.sleep_ms(150)
luces[0].value(0)

if not rtc.memory(): # Inicializar el contador si no existe
    rtc.memory(b'0')  # Inicializar el contador en 0 pero se ingresa como byte, por eso se ve como b'0'

# Leer el contador actual
contador=int(rtc.memory().decode()) #se lee la memoria RTC y con .decode(), convierte los bytes en cadena de caracteres, luego toda esta lectura se convierte en entero

if (contador<3):  # Cuenta 3 ciclos (0, 1, 2)
    print(f"Ciclo {contador + 1}: Iniciando.")
    time.sleep(1)  # Esperar un momento antes de entrar en deepsleep

    print("Entrando en deepsleep, La ESP32 despertará después de 5 segundos.\n")
    contador=contador+1
    rtc.memory(str(contador).encode())  # Guardar el contador en la memoria RTC, convierte el contador a cadena y luedo la codifica en bytes ya que la memoria RTC solo almacena bytes
    #el rtc.memory() es usado para escribir o leer los datos almacenado en la memoria RTC
    deepsleep(2000)  # 5 segundos en milisegundos

#--------------------------------------------------   EJECUCION PRINCIPAL  --------------------------------------------------
else:
    print("\nEjecutando la siguiente seccion de código luego de hacer DEEPSLEEP durante 30 segundos.")
   
    tiempoMaximo=120000  # 30 segundos en milisegundos, esto durará el ciclo
    inicio=time.ticks_ms()  # Obtener el tiempo inicial(nos da el tiempo actual desde que se inicio la esp32) - se asigna ese valor a "inicio"
    wlan=conectarWiFi()
   
    while (time.ticks_diff(time.ticks_ms(), inicio) < tiempoMaximo): #diferencia entre el tiempo actual y el "inicio" sea menor al tiempoMaximo
       
        indiceUV=lecturaVoltaje()
        controlLuces(indiceUV)
        enviarAFlask(indiceUV, wlan)
        time.sleep(1)  # Espera 3 segundos antes de la siguiente lectura
   
    #------------------------------------------------------------------------------------------------------------------------------

    rtc.memory(b'0')  
    print("\nReiniciando el contador.\n")



