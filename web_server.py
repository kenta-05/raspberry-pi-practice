from flask import Flask
import RPi.GPIO as GPIO

BUTTON_PIN = 26
LED_PIN_LIST = [17, 27, 22]

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN)
app = Flask(__name__)

for led_pin in LED_PIN_LIST:
    GPIO.setup(led_pin, GPIO.OUT)


@app.route("/")
def index():
    return "Hello, World!"


@app.route("/push-button")
def is_button_pushed():
    if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
        return "Button is pushed"
    else:
        return "Button is not pushed"


@app.route("/led/<int:led_pin>/state/<int:led_state>")
def trigger_led(led_pin, led_state):
    if led_pin in LED_PIN_LIST:

        for pin in LED_PIN_LIST:
            GPIO.output(pin, GPIO.LOW)

        GPIO.output(led_pin, led_state)
        return f"LED {led_pin} is now {led_state}"
    else:
        return f"LED {led_pin} is not available"


app.run(host="0.0.0.0", port=8500)
