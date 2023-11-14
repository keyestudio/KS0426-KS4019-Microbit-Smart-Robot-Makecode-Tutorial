from keyes_Bit_Car_Driver import *
import neopixel
bitCar = Bit_Car_Driver()
np = neopixel.NeoPixel(pin5, 18)
distance = 0
val_L = 0
val_R = 0
while True:
    distance = bitCar.get_distance()
    val_L = pin2.is_touched()
    val_R = pin11.read_digital()
    if distance > 3 and distance <= 6 and val_L is False and val_R == 1:
        bitCar.motorL(0, 0)
        bitCar.motorR(0, 0)
        for pixel_id1 in range(0, len(np)):
            np[pixel_id1] = (250, 0, 0)
            np.show()
    elif distance <= 3 or val_L is True and val_R == 0:
        bitCar.motorL(0, 80)
        bitCar.motorR(0, 80)
        for pixel_id1 in range(0, len(np)):
            np[pixel_id1] = (160, 32, 240)
            np.show()
    elif distance > 6 and val_L is False and val_R == 1:
        bitCar.motorL(1, 80)
        bitCar.motorR(1, 80)
        for pixel_id1 in range(0, len(np)):
            np[pixel_id1] = (0, 0, 255)
            np.show()
    elif val_L is True and val_R == 1:
        bitCar.motorL(0, 80)
        bitCar.motorR(1, 80)
        for pixel_id1 in range(0, len(np)):
            np[pixel_id1] = (0, 255, 0)
            np.show()
    elif val_L is False and val_R == 0:
        bitCar.motorL(1, 80)
        bitCar.motorR(0, 80)
        for pixel_id1 in range(0, len(np)):
            np[pixel_id1] = (255, 255, 0)
            np.show()
    else:
        bitCar.motorL(0, 0)
        bitCar.motorR(0, 0)
        for pixel_id1 in range(0, len(np)):
            np[pixel_id1] = (255, 0, 0)
            np.show()
