#!/user/bin/python
import math
import smbus
from time import sleep

power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c
SENSOR_ADDR = 0x68
LCD_ADDR = 0x27
bus = smbus.SMBus(1)

LCD_WIDTH = 16   # Maximum characters per line

# Define some device constants
LCD_CHR = 1 # Mode - Sending data
LCD_CMD = 0 # Mode - Sending command

LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
LCD_LINE_3 = 0x94 # LCD RAM address for the 3rd line
LCD_LINE_4 = 0xD4 # LCD RAM address for the 4th line

LCD_BACKLIGHT  = 0x08  # On
#LCD_BACKLIGHT = 0x00  # Off

ENABLE = 0b00000100 # Enable bit

# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005

def lcd_init():
 # Initialise display
    lcd_byte(0x33,LCD_CMD) # 110011 Initialise
    lcd_byte(0x32,LCD_CMD) # 110010 Initialise
    lcd_byte(0x06,LCD_CMD) # 000110 Cursor move direction
    lcd_byte(0x0C,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off
    lcd_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size
    lcd_byte(0x01,LCD_CMD) # 000001 Clear display
    sleep(E_DELAY)

def lcd_byte(bits, mode):

    # Send byte to data pins
    # bits = the data
    # mode = 1 for data
    #        0 for command
    bits_high = mode | (bits & 0xF0) | LCD_BACKLIGHT
    bits_low = mode | ((bits << 4) & 0xF0) | LCD_BACKLIGHT

    # High bits
    bus.write_byte(LCD_ADDR, bits_high)
    lcd_toggle_enable(bits_high)

    # Low bits
    bus.write_byte(LCD_ADDR, bits_low)
    lcd_toggle_enable(bits_low)

def lcd_toggle_enable(bits):
    # Toggle enable
    sleep(E_DELAY)
    bus.write_byte(LCD_ADDR, (bits | ENABLE))
    sleep(E_PULSE)
    bus.write_byte(LCD_ADDR,(bits & ~ENABLE))
    sleep(E_DELAY)

def lcd_string(message,line):
    # Send string to display

    message = message.ljust(LCD_WIDTH," ")

    lcd_byte(line, LCD_CMD)

    for i in range(LCD_WIDTH):
        lcd_byte(ord(message[i]),LCD_CHR)

def read_byte(reg):
    return bus.read_byte_data(SENSOR_ADDR,reg)

def read_word(reg):
    h = bus.read_byte_data(SENSOR_ADDR, reg)
    l = bus.read_byte_data(SENSOR_ADDR,reg+1)
    value = (h << 8) + l
    return value

def read_word_i2c(reg):
    val = read_word(reg)
    if val >= 0x8000:
        return -((65535 - val) + 1)
    else:
        return val

bus.write_byte_data(SENSOR_ADDR, power_mgmt_1, 0)

def main():
    # Main program block

    # Initialise display
    lcd_init()
    while True:
        acc_X = read_word_i2c(0x3b)
        scaled_acc_X = acc_X / 16384.0
        lcd_string("Acceleration_X:", LCD_LINE_1)
        lcd_string(str(round(scaled_acc_X,3)), LCD_LINE_2)
        sleep(1)

        acc_Y = read_word_i2c(0x3d)
        scaled_acc_Y = acc_Y / 16384.0
        lcd_string("Acceleration_Y:", LCD_LINE_1)
        lcd_string(str(round(scaled_acc_Y,3)), LCD_LINE_2)
        sleep(1)

        acc_Z = read_word_i2c(0x3f)
        scaled_acc_Z = acc_Z / 16384.0
        lcd_string("Acceleration_Z:", LCD_LINE_1)
        lcd_string(str(round(scaled_acc_Z,3)), LCD_LINE_2)
        sleep(1)


if __name__ == '__main__':

    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        lcd_byte(0x01, LCD_CMD)