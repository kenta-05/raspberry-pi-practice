import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

current_led = 0

FIRST_LED_PIN = 17
SECOND_LED_PIN = 27
THIRD_LED_PIN = 22
BUTTON_PIN = 26

GPIO.setup(FIRST_LED_PIN, GPIO.OUT)
GPIO.setup(SECOND_LED_PIN, GPIO.OUT)
GPIO.setup(THIRD_LED_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN)


def all_leds_off():
    GPIO.output(FIRST_LED_PIN, GPIO.LOW)
    GPIO.output(SECOND_LED_PIN, GPIO.LOW)
    GPIO.output(THIRD_LED_PIN, GPIO.LOW)


while True:
    try:
        time.sleep(0.3)
        if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
            all_leds_off()
            if current_led < 3:
                current_led += 1
            else:
                current_led = 0

        if current_led == 0:
            all_leds_off()
        elif current_led == 1:
            GPIO.output(FIRST_LED_PIN, GPIO.HIGH)
        elif current_led == 2:
            GPIO.output(SECOND_LED_PIN, GPIO.HIGH)
        elif current_led == 3:
            GPIO.output(THIRD_LED_PIN, GPIO.HIGH)
    except KeyboardInterrupt:
        GPIO.cleanup()
    except Exception as e:
        print(f"An error occurred: {e}")
