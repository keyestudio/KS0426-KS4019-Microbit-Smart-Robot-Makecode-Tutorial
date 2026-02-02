from microbit import *
import neopixel
np = neopixel.NeoPixel(pin5, 18)
np.clear()

while True:
    val1 = pin1.read_analog()
    val2 = int((val1/1023)*255)

    for pixel_id in range(0, len(np)):
        np[pixel_id] = (255 - val2, 255 - val2, 255 - val2)
        np.show()
    sleep(100)
