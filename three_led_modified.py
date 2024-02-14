import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led_index = 0
LED_PIN_LIST = [17, 27, 22]
BUTTON_PIN = 26


def update_led():
    led_index = led_index % len(LED_PIN_LIST)

    if led_index % len(LED_PIN_LIST) != 0:
        GPIO.output(LED_PIN_LIST[led_index - 1], GPIO.HIGH)


for pin in LED_PIN_LIST:
    GPIO.setup(pin, GPIO.OUT)

GPIO.setup(BUTTON_PIN, GPIO.IN)

previous_button_state = GPIO.input(BUTTON_PIN)

while True:
    time.sleep(0.01)
    button_state = GPIO.input(BUTTON_PIN)
    if button_state != previous_button_state:
        previous_button_state = button_state
        if button_state == GPIO.HIGH:
            led_index += 1
            update_led()
