from microbit import *
from keyes_Bit_Car_Driver import *
bitCar = Bit_Car_Driver()
val_LL = 0
while True:
    bitCar.headlights(0, 0, 0)
    val_LL = pin2.is_touched()
    print("digital signal:", val_LL)
    sleep(200)
