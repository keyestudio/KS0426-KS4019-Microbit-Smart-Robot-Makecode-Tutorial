from microbit import *
val_LL = 0
val_RR = 0
while True:
    val_RR = pin12.read_digital()
    val_LL = pin13.read_digital()

    if val_LL == 0 and val_RR == 1:
        display.show(Image("00009:""00009:""00009:""00009:""00009"))

    elif val_LL == 1 and val_RR == 0:
        display.show(Image("90000:""90000:""90000:""90000:""90000"))

    elif val_LL == 1 and val_RR == 1:
        display.show(Image.HEART_SMALL)

    else:
        display.show(Image.HEART)
