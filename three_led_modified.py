import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led_index = 0


def update_led():
    GPIO.output(FIRST_LED_PIN, GPIO.LOW)
    GPIO.output(SECOND_LED_PIN, GPIO.LOW)
    GPIO.output(THIRD_LED_PIN, GPIO.LOW)

    if led_index % 4 == 1:
        GPIO.output(FIRST_LED_PIN, GPIO.HIGH)
    elif led_index % 4 == 2:
        GPIO.output(SECOND_LED_PIN, GPIO.HIGH)
    elif led_index % 4 == 3:
        GPIO.output(THIRD_LED_PIN, GPIO.HIGH)


FIRST_LED_PIN = 17
SECOND_LED_PIN = 27
THIRD_LED_PIN = 22
BUTTON_PIN = 26

GPIO.setup(FIRST_LED_PIN, GPIO.OUT)
GPIO.setup(SECOND_LED_PIN, GPIO.OUT)
GPIO.setup(THIRD_LED_PIN, GPIO.OUT)
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
