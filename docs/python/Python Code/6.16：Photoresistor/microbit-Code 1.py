from microbit import *

while True:
    val = pin1.read_analog()
    print("analog signal:", val)
    sleep(100)
