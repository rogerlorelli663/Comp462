#!/usr/bin/env python
import signal
import RPi.GPIO as GPIO
import time


A = 12
B = 16
C = 32
D = 22
E = 38
F = 10
G = 8
DP = 36
SEG7_PINS = [A,B,C,D,E,F,G,DP]
NINE = [A,B,C,F,G]
EIGHT = [A,B,C,D,E,F,G]
SEVEN = [A,B,C]
SIX = [C,D,E,F,G]
FIVE = [A,C,D,F,G]
FOUR = [B,C,F,G]
THREE = [A,B,C,D,G]
TWO = [A,B,D,E,G]
ONE = [B,C]
ZERO = [A,B,C,D,E,F]

i_green = 0
i_yellow = 0
i_red = 0
GREEN_LED = 7
YELLOW_LED = 29
RED_LED = 40

called = False

epoc = 0.2
GREEN_RED_TIMER = 30
YELLOW_TIMER = 15
GRcalculated_time = GREEN_RED_TIMER / epoc
Ycalculated_time = YELLOW_TIMER / epoc

out_list = [GREEN_LED,YELLOW_LED,RED_LED]

traffic_light_mode = 0

def timer(counter):
    #display the counter on the 7-segment
    GPIO.output(SEG7_PINS,0)
    if counter <= 1:
        GPIO.output(ZERO,1)
    elif counter <= 2:
        GPIO.output(ONE,1)
    elif counter <= 3:
        GPIO.output(TWO,1)
    elif counter <= 4:
        GPIO.output(THREE,1)
    else:
        GPIO.output(SEG7_PINS,1)

def my_callback(channel):
    print("Button pressed")
    global traffic_light_mode
    global i_green
    global i_yellow
    print(f"Traffic Mode: {traffic_light_mode}")
    if traffic_light_mode == 0:
        traffic_light_mode = 1
        i_green = (GREEN_RED_TIMER - 2) / epoc
        i_yellow = (YELLOW_TIMER - 1) / epoc
    time.sleep(5)

# Set up the GPIO pins and the event-interupts here
# Button
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(37, GPIO.RISING, bouncetime=300)
GPIO.add_event_callback(37, my_callback)

# LEDS
GPIO.setup(out_list, GPIO.OUT, initial = GPIO.LOW)

# 7 Segment
GPIO.setup(SEG7_PINS, GPIO.OUT, initial = GPIO.LOW)


try:
    loops = 0

    while loops<3:
            loops += 1
            #green mode
            traffic_light_mode = 0
            GPIO.output(GREEN_LED, 1)
            while i_green < GRcalculated_time: # change it if needed
                time.sleep(epoc) # change it if needed
                i_green += 1
            GPIO.output(GREEN_LED,0)
            i_green = 0

            # yellow mode
            traffic_light_mode = 1
            GPIO.output(YELLOW_LED, 1)
            while i_yellow < Ycalculated_time:  # change it if needed
                time.sleep(epoc)  # change it if needed
                i_yellow += 1
            GPIO.output(YELLOW_LED, 0)
            i_yellow = 0

            # red mode
            traffic_light_mode = 2
            GPIO.output(RED_LED, 1)
            while i_red < GRcalculated_time:  # change it if needed
                temp = (GREEN_RED_TIMER - (i_red * epoc)) / 2
                if temp <= 4:
                    print(f"Timer: {temp}")
                    timer(temp)
                time.sleep(epoc)  # change it if needed
                i_red += 1
                # call timer function according to the value of i_red
            GPIO.output(RED_LED, 0)
            GPIO.output(SEG7_PINS, 0)
            i_red = 0

except KeyboardInterrupt:
    GPIO.cleanup()
    exit(1)
GPIO.cleanup()  # To clear all the changes to the used
