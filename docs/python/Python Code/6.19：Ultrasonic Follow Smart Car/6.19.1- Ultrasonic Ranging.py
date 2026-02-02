from microbit import *
from keyes_Bit_Car_Driver import *
import music
bitCar = Bit_Car_Driver()
tune = ["C4:4"]
while True:
    i = 0
    distance = bitCar.get_distance()
    print("distance:", distance)
    if distance < 10:
        while i < 1:
            music.play(tune)
            sleep(200)
            music.play(tune)
            sleep(200)
            i += 1
