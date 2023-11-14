from microbit import *
val_LL = 0
val_RR = 0

while True:
    val_LL = pin2.is_touched()
    val_RR = pin11.read_digital()

    if val_LL is True and val_RR == 0:
        display.show(Image.HAPPY)

    elif val_LL is True and val_RR == 1:
        display.show(Image("00900:""00090:""99999:""00090:""00900"))

    elif val_LL is False and val_RR == 0:
        display.show(Image("00900:""09000:""99999:""09000:""00900"))

    else:
        display.show(Image("00900:""09990:""90909:""00900:""00900"))
