from microbit import *
from keyes_Bit_Car_Driver import *

bitCar = Bit_Car_Driver()

while True:
    bitCar.headlights(255, 0, 0)
    sleep(1000)
    bitCar.headlights(0, 255, 0)
    sleep(1000)
    bitCar.headlights(0, 0, 255)
    sleep(1000)
    bitCar.headlights(0, 255, 255)
    sleep(1000)
    bitCar.headlights(255, 0, 255)
    sleep(1000)
    bitCar.headlights(255, 255, 0)
    sleep(1000)
    bitCar.headlights(255, 255, 255)
    sleep(1000)
