from microbit import *
import neopixel
from random import randint
red = 255
green = 0
blue = 0
np = neopixel.NeoPixel(pin5, 18)
flag = 1
while True:
    while flag == 1:
        for pixel_id in range(0, len(np)):
            red = red - 35
            if red <= 0:
                red = 0
            green = green + 35
            if green >= 255:
                green = 255
            blue = blue + 35
            if blue >= 255:
                blue = 255
            np[pixel_id] = (red, green, blue)
            np.show()
            sleep(100)
        for pixel_close in range(0, len(np)):
            np[pixel_close] = (0, 0, 0)
            np.show()
            sleep(100)
        flag = 0
