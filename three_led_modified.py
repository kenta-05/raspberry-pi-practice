import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

click_count = 0
LED_PIN_LIST = [17, 27, 22]
BUTTON_PIN = 26


def update_led(selected_pin):
    for pin in LED_PIN_LIST:
        if pin == selected_pin:
            GPIO.output(pin, GPIO.HIGH)
        else:
            GPIO.output(pin, GPIO.LOW)


# def update_led():
#     click_count = click_count % len(LED_PIN_LIST)

#     if click_count % len(LED_PIN_LIST) != 0:
#         GPIO.output(LED_PIN_LIST[click_count - 1], GPIO.HIGH)


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
            click_count += 1
            led_index = (click_count - 1) % len(LED_PIN_LIST)
            update_led(LED_PIN_LIST[led_index])
