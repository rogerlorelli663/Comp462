import serial
try:
    ser = serial.Serial('/dev/ttyACM0', 115200)

    while 1:
        bytes = ser.readline()
        bytes.split(b'\r\n')
        string = bytes.decode('utf-8')
        print(string, end='')

except serial.serialutil.SerialException:
    print("Error, No Connection")

except KeyboardInterrupt:
    print("\nStopping")