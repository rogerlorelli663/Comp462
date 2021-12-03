# code modified, tweaked and tailored from code by bertwert
# on RPi forum thread topic 91796
import RPi.GPIO as GPIO
import dht11
from statistics import median
from time import sleep

#Duty Cycle computations
TotalPWMPeriod = 20
dutyMSLeft = 1 # -90 deg
dutyMSRight = 2 # 90 deg
dutyMSNeutral = median((dutyMSLeft,dutyMSRight)) # 0 deg / closed position
dutyPercNeutral = dutyMSNeutral/TotalPWMPeriod * 100
dutyMSOpen = median((dutyMSNeutral,dutyMSRight)) # Open Position 45 deg
dutyPercOpen = dutyMSOpen/TotalPWMPeriod * 100

time = 0.001

GPIO.setmode(GPIO.BCM)

SENSOR = 23
SERVO = 18

GPIO.setup(SERVO, GPIO.OUT)

pwm=GPIO.PWM(18, 50)
pwm.start(0)

instance = dht11.DHT11(pin = SENSOR)
# GPIO ports for the 7seg pins
segments = (16,12,17,26,19,20,4,13)
# 7seg_segment_pins (11,7,4,2,1,10,5,3) +  100R inline
dp = 13
for segment in segments:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, 0)

# GPIO ports for the digit 0-3 pins
digits = (21,24,25,27)
# 7seg_digit_pins (12,9,8,6) digits 0-3 respectively

for digit in digits:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, 1)

num = {' ': (0, 0, 0, 0, 0, 0, 0, 0),
       '.': (0, 0, 0, 0, 0, 0, 0, 1),
       '0': (1, 1, 1, 1, 1, 1, 0, 0),
       '1': (0, 1, 1, 0, 0, 0, 0, 0),
       '2': (1, 1, 0, 1, 1, 0, 1, 0),
       '3': (1, 1, 1, 1, 0, 0, 1, 0),
       '4': (0, 1, 1, 0, 0, 1, 1, 0),
       '5': (1, 0, 1, 1, 0, 1, 1, 0),
       '6': (1, 0, 1, 1, 1, 1, 1, 0),
       '7': (1, 1, 1, 0, 0, 0, 0, 0),
       '8': (1, 1, 1, 1, 1, 1, 1, 0),
       '9': (1, 1, 1, 1, 0, 1, 1, 0)}

try:
    threshold = float(input("Please Enter Threshold Value"))
    while True:
        timer = 0
        result = instance.read()
        temp = result.temperature

        if temp < threshold:
            pwm.ChangeDutyCycle(dutyPercNeutral)
        elif temp > threshold:
            pwm.ChangeDutyCycle(dutyPercOpen)

        temp = str(result.temperature)
        print(temp)

        while timer < 5:
            for digit in range(len(temp)):
                try:
                    for loop in range(0, 8):
                        GPIO.output(segments[loop], num[temp[digit]][loop])
                    GPIO.output(digits[digit], 0)
                    sleep(time)
                    timer += time
                    GPIO.output(digits[digit], 1)
                except IndexError:
                    print(f"Temperature: {temp}")
                    print(digit)
                except KeyboardInterrupt:
                    exit(1)
finally:
    GPIO.cleanup()