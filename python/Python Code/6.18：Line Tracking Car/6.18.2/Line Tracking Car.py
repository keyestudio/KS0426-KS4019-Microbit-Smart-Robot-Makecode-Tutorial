from keyes_Bit_Car_Driver import *
import neopixel
bitCar = Bit_Car_Driver()
np = neopixel.NeoPixel(pin5, 18)
display.show(Image.HAPPY)

while True:
    val_RR = pin12.read_digital()
    val_LL = pin13.read_digital()
    for pixel_id1 in range(0, len(np)):
        np[pixel_id1] = (255, 100, 100)
        np.show()
    if val_LL == 0 and val_RR == 1:
        bitCar.motorL(1, 80)
        bitCar.motorR(0, 30)
    elif val_LL == 1 and val_RR == 0:
        bitCar.motorL(0, 30)
        bitCar.motorR(1, 80)
    elif val_LL == 1 and val_RR == 1:
        bitCar.motorL(1, 60)
        bitCar.motorR(1, 60)
    else:
        bitCar.motorL(0, 0)
        bitCar.motorR(0, 0)
