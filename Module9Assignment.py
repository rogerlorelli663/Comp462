#!/usr/bin/env python
import signal
import RPi.GPIO as GPIO
from time import sleep

# Mode State
mode = 0

# BCM Pins
button = 26
sensor = 6
motor1 = 4
motor2 = 22
enable = 18

# PWM calc for speed
fast = 100
medium = fast / 1.5
slow = medium / 2

def set_motor():
    global mode
    # do PWM on motor here
    if mode == 0:
        pwm.ChangeDutyCycle(0)
    elif mode == 1:
        pwm.ChangeDutyCycle(slow)
    elif mode == 2:
        pwm.ChangeDutyCycle(medium)
    elif mode == 3:
        pwm.ChangeDutyCycle(fast)
    else:
        print(f"Error mode {mode} Stopping Program")
        raise KeyboardInterrupt

def my_button_callback(channel):
    global mode
    print("Button pressed")
    print(f" Fan Mode: {mode}")
    if mode < 3:
        mode = mode + 1
    else:
        mode = 0



def my_sensor_callback(channel):
    global mode
    print("Sensor Triggered")
    print(f" Fan Mode: {mode}")
    if mode == 0:
        mode = 1
    else:
        mode = 0

# Set up the GPIO pins and the event-interrupts here
GPIO.setmode(GPIO.BCM)

# DC Motor controller
GPIO.setup(enable, GPIO.OUT)
GPIO.setup(motor1, GPIO.OUT)
GPIO.setup(motor2, GPIO.OUT)

# Direction
GPIO.output(motor1, True)
GPIO.output(motor2, False)

# PWM
pwm = GPIO.PWM(enable,100)
pwm.start(0)

# Button
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(button, GPIO.RISING, callback=my_button_callback, bouncetime=300)

# Sensor
GPIO.setup(sensor, GPIO.IN)
GPIO.add_event_detect(sensor, GPIO.RISING, callback=my_sensor_callback, bouncetime=300)

try:

    while True:
        set_motor()
        sleep(1)

except KeyboardInterrupt:
    pwm.stop()
    exit(1)
finally:
    GPIO.cleanup()  # To clear all the changes to the used
