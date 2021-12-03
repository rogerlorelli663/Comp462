
#!/user/bin/python
import math
import smbus
from time import sleep

power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c
address = 0x68
bus = smbus.SMBus(1)

def read_byte(reg):
    return bus.read_byte_data(address,reg)

def read_word(reg):
    h = bus.read_byte_data(address, reg)
    l = bus.read_byte_data(address,reg+1)
    value = (h << 8) + l
    return value

def read_word_i2c(reg):
    val = read_word(reg)
    if val >= 0x8000:
        return -((65535 - val) + 1)
    else:
        return val

def dis(a,b):
    return math.sqrt(a*a + b*b)

def get_y_rotation(x,y,z):
    radians = math.atan2(x,dis(y,z))
    return -math.degrees(radians)

def get_x_rotation(x,y,z):
    radians = math.atan2(y,dis(x,z))
    return math.degrees(radians)

bus.write_byte_data(address, power_mgmt_1, 0)

while True:
    try:
        print("Gyro: ")
        gyro_X = read_word_i2c(0x43)
        gyro_Y = read_word_i2c(0x45)
        gyro_Z = read_word_i2c(0x47)

        print(f"X: {gyro_X}")
        print(f"Y: {gyro_Y}")
        print(f"Z: {gyro_Z}")

        print("Acceleration: ")
        acc_X = read_word_i2c(0x3b)
        acc_Y = read_word_i2c(0x3d)
        acc_Z = read_word_i2c(0x3f)

        scaled_acc_X = acc_X / 16384.0
        scaled_acc_Y = acc_Y / 16384.0
        scaled_acc_Z = acc_Z / 16384.0

        print(f"X Rotation: {get_x_rotation(scaled_acc_X,scaled_acc_Y,scaled_acc_Z)}")
        print(f"Y Rotation: {get_y_rotation(scaled_acc_X,scaled_acc_Y,scaled_acc_Z)}")
        sleep(5)
    except KeyboardInterrupt:
        print()
        exit(0)