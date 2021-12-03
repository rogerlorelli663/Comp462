import datetime
from time import sleep
import serial

try:
    ser = serial.Serial('/dev/ttyACM0', 9600)

    while 1:
        bytes = ser.readline()
        date_time = datetime.datetime.now()
        bytes.split(b'\r\n')
        string = bytes.decode('utf-8')
        string = int(string)
        with open("page3.html", "r") as html_file:
            content = html_file.readlines()
        for i in range(len(content)):
            content[i] = content[i].strip()

        index = content.index('</table>')
        content.insert(index, '<tr>')
        content.insert(index+1, '<td>')
        content.insert(index+2, f'{string}')
        content.insert(index+3, '</td>')
        content.insert(index+4, '<td>')
        content.insert(index+5, f'{date_time.strftime("%Y-%m-%d %H:%M:%S.%f")}')
        content.insert(index+6, '</td>')
        content.insert(index+7, '</tr>')

        with open("page3.html", "w") as html_file:
            for line in content:
                html_file.write(line)

        sleep(10)

except serial.serialutil.SerialException:
    print("Error, No Connection")

except KeyboardInterrupt:
    print("\nStopping")