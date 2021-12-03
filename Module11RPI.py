#!/user/bin/python
import math
import smbus
from time import sleep

power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c
ARDUINO_ADDR = 0x44

bus = smbus.SMBus(1)

def read_value(reg):
    data = []
    data.append(bus.read_byte_data(ARDUINO_ADDR, reg))
    data.append(bus.read_byte_data(ARDUINO_ADDR, reg+1))
    data.append(bus.read_byte_data(ARDUINO_ADDR, reg+2))
    data.append(bus.read_byte_data(ARDUINO_ADDR, reg+3))
    print(data)
    #return cm, inches

def main():
    while True:
        read_value(0x00)
        #cm, inches = read_value(0x00)
        #print(f"{round(cm, 2)} cm")
        #print(f"{round(inches, 2)} inches")
        sleep(5)





if __name__ == '__main__':

    try:
        main()
    except KeyboardInterrupt:
        pass

