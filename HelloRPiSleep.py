## If the service is not stopped/disabled then it will continue to run in the background,
## using resources.
from time import sleep
counter = 0
while True:
    print(f"{counter}: Hello Raspberry Pi!")
    counter += 1
    sleep(7)