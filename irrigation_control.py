import RPi.GPIO as GPIO
import time
from sensors import read_soil_moisture, read_dht22, read_rain_sensor
from config import PIN_RELAY

def control_irrigation():
    SOIL_MOISTURE_THRESHOLD = 1
    MAX_TEMPERATURE = 30
    MIN_HUMIDITY = 50

    soil_moisture = read_soil_moisture()
    humidity, temperature = read_dht22()
    rain_detected = read_rain_sensor()

    if soil_moisture == SOIL_MOISTURE_THRESHOLD and not rain_detected:
        if temperature > MAX_TEMPERATURE or humidity < MIN_HUMIDITY:
            GPIO.output(PIN_RELAY, GPIO.HIGH)
            print("Bomba de irrigação ativada.")
        else:
            GPIO.output(PIN_RELAY, GPIO.LOW)
            print("Bomba de irrigação desativada.")
    else:
        GPIO.output(PIN_RELAY, GPIO.LOW)
        print("Solo úmido ou chuva detectada. Bomba desativada.")

    time.sleep(10)
