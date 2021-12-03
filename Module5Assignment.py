#!/user/bin/python3
import sys
from time import sleep
GREEN_LED_PATH = "sys/class/gpio/gpio4"
YELLOW_LED_PATH = "sys/class/gpio/gpio5"
RED_LED_PATH = "sys/class/gpio/gpio21"
PATHS = [GREEN_LED_PATH,RED_LED_PATH,YELLOW_LED_PATH]
SYSFS_DIR = "sys/class/gpio/"
GREEN_LED_NUM = "4"
YELLOW_LED_NUM = "5"
RED_LED_NUM = "21"

def writeLED(filename, value, path):
    if path in PATHS:
        fo = open(path + filename,"w")
        fo.write(value)
        fo.close()
        return
    else:
        print("Error: incorrect path")

print("Setting up the LED GPIO")
try:
    number = GREEN_LED_NUM
    writeLED(filename="export",value=number,path=SYSFS_DIR)
    writeLED(filename="direction",value="out",path=GREEN_LED_PATH)
except:
    writeLED(filename="export",value=YELLOW_LED_NUM,path=SYSFS_DIR)
    writeLED(filename="direction",value="out",path=YELLOW_LED_PATH)

    writeLED(filename="export",value=RED_LED_NUM,path=SYSFS_DIR)
    writeLED(filename="direction",value="out",path=RED_LED_PATH)



print("All LEDs enabled")

while(True):
    writeLED(filename="value",value="1",path=GREEN_LED_PATH)
    sleep(15)
    writeLED(filename="value",value="0",path=GREEN_LED_PATH)
    writeLED(filename="value",value="1",path=YELLOW_LED_PATH)
    sleep(5)
    writeLED(filename="value",value="0",path=YELLOW_LED_PATH)
    writeLED(filename="value",value="1",path=RED_LED_PATH)
    sleep(15)
    writeLED(filename="value",value="0",path=RED_LED_PATH)
