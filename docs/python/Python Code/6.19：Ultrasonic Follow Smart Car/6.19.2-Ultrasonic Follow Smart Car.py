from keyes_Bit_Car_Driver import *
import neopixel
np = neopixel.NeoPixel(pin5, 18)
from random import randint
bitCar = Bit_Car_Driver()
while True:
    distance = 0
    distance = bitCar.get_distance()
    if distance >= 10 and distance <= 30:
        bitCar.motorL(1, 100)
        bitCar.motorR(1, 100)
        for pixel_id1 in range(0, len(np)):
            np[pixel_id1] = (255, 0, 0)
            np.show()
    if distance <= 6:
        bitCar.motorL(0, 100)
        bitCar.motorR(0, 100)
        for pixel_id1 in range(0, len(np)):
            np[pixel_id1] = (255, 255, 0)
            np.show()
    if distance > 6 and distance < 10 or distance > 30:
        bitCar.motorL(0, 0)
        bitCar.motorR(0, 0)
        for pixel_id1 in range(0, len(np)):
            np[pixel_id1] = (255, 255, 255)
            np.show()
