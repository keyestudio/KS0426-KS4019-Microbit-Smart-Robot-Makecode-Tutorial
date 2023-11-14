from keyes_Bit_Car_Driver import *
bitCar = Bit_Car_Driver()
show_L = Image("90000:""90000:""90000:""90000:""99999")
show_O = Image("09990:""90009:""90009:""90009:""09990")
a = 0
b = 0
def run_L():
    global b
    sleep(1000)
    bitCar.motorL(1, 200)
    bitCar.motorR(1, 200)
    sleep(1000)
    bitCar.motorL(0, 120)
    bitCar.motorR(1, 120)
    sleep(650)
    bitCar.motorL(1, 200)
    bitCar.motorR(1, 200)
    sleep(1000)
    bitCar.motorL(0, 0)
    bitCar.motorR(0, 0)
    b = 0
def run_O():
    global b
    sleep(1000)
    bitCar.motorL(1, 200)
    bitCar.motorR(1, 200)
    sleep(1000)
    bitCar.motorL(0, 120)
    bitCar.motorR(1, 120)
    sleep(620)
    bitCar.motorL(1, 200)
    bitCar.motorR(1, 200)
    sleep(1000)
    bitCar.motorL(0, 120)
    bitCar.motorR(1, 120)
    sleep(620)
    bitCar.motorL(1, 200)
    bitCar.motorR(1, 200)
    sleep(1000)
    bitCar.motorL(0, 120)
    bitCar.motorR(1, 120)
    sleep(620)
    bitCar.motorL(1, 200)
    bitCar.motorR(1, 200)
    sleep(1000)
    bitCar.motorL(0, 0)
    bitCar.motorR(0, 0)
    b = 0
while True:
    if button_a.was_pressed():
        a = a + 1
        if a >= 3:
            a = 0
    if button_b.was_pressed():
        b = 1
    if (a == 1):
        display.show(show_L)
        if b == 1:
            run_L()
    elif a == 2:
        display.show(show_O)
        if b == 1:
            run_O()
