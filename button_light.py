import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

BUTTON_PIN = 26
LED_PIN = 17

GPIO.setup(BUTTON_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

while True:
    if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
        GPIO.output(LED_PIN, GPIO.HIGH)
    else:
        GPIO.output(LED_PIN, GPIO.LOW)

GPIO.cleanup()
