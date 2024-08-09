import RPi.GPIO as GPIO

# Configuração dos pinos GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Definição dos pinos dos sensores
PIN_SOIL_MOISTURE = 14
PIN_DHT22 = 4
PIN_RAIN_SENSOR = 15
PIN_RELAY = 18

# Configuração do pino do relé como saída
GPIO.setup(PIN_RELAY, GPIO.OUT)
GPIO.output(PIN_RELAY, GPIO.LOW)  # Inicialmente desliga a bomba
