from microbit import *
val_RR = 0
while True:
    val_RR = pin12.read_digital()
    print("digital signal:", val_RR)
    sleep(200)
