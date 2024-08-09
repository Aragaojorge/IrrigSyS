import Adafruit_DHT
import RPi.GPIO as GPIO
from config import PIN_SOIL_MOISTURE, PIN_DHT22, PIN_RAIN_SENSOR

def read_soil_moisture():
    moisture_value = GPIO.input(PIN_SOIL_MOISTURE)
    return moisture_value

def read_dht22():
    sensor = Adafruit_DHT.DHT22
    humidity, temperature = Adafruit_DHT.read_retry(sensor, PIN_DHT22)
    return humidity, temperature

def read_rain_sensor():
    rain_detected = GPIO.input(PIN_RAIN_SENSOR)
    return rain_detected
