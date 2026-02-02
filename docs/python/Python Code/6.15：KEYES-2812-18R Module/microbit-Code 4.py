from microbit import *
import neopixel
np = neopixel.NeoPixel(pin5, 18)
from random import randint
R = 0
G = 0
B = 0
while True:
   for index in range(0, 18):
        R = randint(10, 255)
        G = randint(10, 255)
        B = randint(10, 255)
        np.clear()
        np[index] = (R, G, B)
        np.show()
        sleep(500)

