import Adafruit_DHT
import RPi.GPIO as GPIO
from config import PIN_SOIL_MOISTURE, PIN_DHT22, PIN_RAIN_SENSOR
import psycopg2
from datetime import datetime, timedelta


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

def persist_data():
    # Capturar a data do dia e definir a hora para 10:30
    timestamp = datetime.now().replace(hour=10, minute=30, second=0, microsecond=0)
    
    # Ler os valores dos sensores
    soil_moisture = read_soil_moisture()
    temperature = read_dht22()
    rain_sensor = read_rain_sensor()
    
    try:
        # Cria a conexão com o db sensor_data
        conn = psycopg2.connect("dbname='irrig_sys' user='jorge' password='123456' host='localhost'")
        
        # Abri um cursor para performar inserção de dados no db
        cur = conn.cursor()
        
        # Executar uma inserção
        cur.execute(
            "INSERT INTO sensor_data (timestamp, soil_moisture, temperature, rain_sensor) VALUES (%s, %s, %s, %s)",
            (timestamp, soil_moisture, temperature, rain_sensor)
        )
        
        # Commit para salvar as mudanças no banco de dados
        conn.commit()
        
        print("Dados inseridos com sucesso.")
        
    except Exception as e:
        print("Ocorreu um erro ao inserir dados:", e)
    
    finally:
        # Fechar o cursor e a conexão
        cur.close()
        conn.close()

