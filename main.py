from irrigation_control import control_irrigation

try:
    while True:
        control_irrigation()
except KeyboardInterrupt:
    print("Programa interrompido.")
finally:
    import RPi.GPIO as GPIO
    GPIO.cleanup()  # Limpa as configurações dos pinos GPIO ao final
