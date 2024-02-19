from flask import Flask
import RPi.GPIO as GPIO

BUTTON_PIN = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN)
app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, World!"


@app.route("/push-button")
def is_button_pushed():
    if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
        return "Button is pushed"
    else:
        return "Button is not pushed"


app.run(host="0.0.0.0", port=8500)
