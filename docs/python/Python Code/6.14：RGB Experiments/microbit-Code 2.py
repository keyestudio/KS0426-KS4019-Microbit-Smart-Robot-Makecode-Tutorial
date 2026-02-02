from microbit import *
from keyes_Bit_Car_Driver import *
bitCar = Bit_Car_Driver()
ledr = 0
ledg = 0
ledb = 0
while True:
    for index in range(51):
        bitCar.headlights(ledr, 0, 0)
        sleep(100)
        ledr += 5
    for index in range(51):
        bitCar.headlights(ledr, 0, 0)
        sleep(100)
        ledr += -5
    for index in range(51):
        bitCar.headlights(0, ledg, 0)
        sleep(100)
        ledg += 5
    for index in range(51):
        bitCar.headlights(0, ledg, 0)
        sleep(100)
        ledg += -5
    for index in range(51):
        bitCar.headlights(0, 0, ledb)
        sleep(100)
        ledb += 5
    for index in range(51):
        bitCar.headlights(0, 0, ledb)
        sleep(100)
        ledb += -5
