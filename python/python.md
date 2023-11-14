# MicroPython Tutorial

![](media/758709e88f83d841a93103a528cae849.png)

## Getting Started With MicroPython

[https://learn.adafruit.com/micropython-basics-what-is-micropython -faq-2792685](https://learn.adafruit.com/micropython-basics-what-is-micropython#faq-2792685)

What is MicroPython?

[MicroPython](https://www.micropython.org/) is a tiny open source [Python programming language](https://www.python.org/) interpreter that runs on small embedded development boards. With MicroPython you can write clean and simple Python code to control hardware instead of having to use complex low-level languages like C or C++ (what Arduino uses for programming).

The simplicity of the Python programming language makes MicroPython an excellent choice for beginners who are new to programming and hardware. However MicroPython is also quite full-featured and supports most of Python's syntax so even seasoned Python veterans will find MicroPython familiar and fun to use.

More details please log in official micro:bit website:

https://microbit-micropython.readthedocs.io/en/latest/index.html

<https://microbit-micropython.readthedocs.io/en/latest/tutorials/introduction.html>

Python has two types of editors（web version and offline version)

Web version: <https://python.microbit.org/v/1.1>

![](media/693f76f5975fc256dbc1d2880c80edeb.png)

The other one is the offline compiler tool-----Mu![IMG_256](media/153c77edd571f12fce0e3282ab6fb530.png)

(Download Mu：<https://codewith.mu/en/download>)

Mu Official Website：<https://codewith.mu/>

Mu, a Python code editor, is suitable for starters.

Mu doesn’t support 32-bit Windows. The latest version is Mu 1.1.0-beta 2

Download Mu

Click“This PC”and right- click to select Properties to check the version of your computer.

![](media/3a58be549e85e640654494c09f3a219f.png)

Below is shown system type of your computer.

![](media/e774ae15dcb81968d9a2a553af57ac96.png)

Enter link: <https://codewith.mu/en/download> to download the corresponding version of Mu.

![](media/ceb4cfa6c81ce3959cec504412767e39.png)

Run and Install Mu , Find out the folder where Mu is downloaded and double-click file to install Mu

![IMG_256](media/8bcfe24cd37e0e5accae1f94cf155640.png)

![](media/aee9cbabeff51123a24af22840073aed.png)

**Mac OSX：**<https://codewith.mu/en/howto/1.1/install_macos>

The installation method is similar.

Windows 10  We will demonstrate how to download Mu on Windows 10.

![](media/877beb7b3f5ccf7e5d849b7aaa8d661d.png)

Tap“Run anyway”.

![](media/c87475e50dd03a0d0d2dcf166f33a837.png)

Confirm the version of Mu and tap“Next”.

![IMG_256](media/8dcf428c559d93fe2b6a4d7413ed2eb7.png)

Then select“I Agree”

![IMG_256](media/2a3983ba2217310771485caf9c0fa98c.png)

Click“Next”and“Install”

![IMG_256](media/65e13e3ab507963045edfb4b9a803103.png)

![IMG_256](media/f49eaea9f5dcf334ff5b263fa11aaf0e.png)

You have to wait for a while until the installation is finished.

![IMG_256](media/87da96658f644f40f73e07d3fc3ca1f0.png)

Finally, click“Finish”

![IMG_256](media/ecf3d3881ec8751824963428a70d7701.png)

Click Mu icon to get started.

![](media/30d0d03f40511139bf51f95d3a6ee21a.png)

Mu’s main interface is shown below:

![](media/0d017772e0be523a9976d8f802257530.png)

## Projects

The projects from 1 to 9 are the introduction of LED matrix and built-in sensors on the micro:bit board.

### 1：Heartbeat

**Description：**

Prepare a Micro:bit board and USB cable. Next we will conduct a basic experiment that a heartbeat pattern flashes on micro:bit board.

What you need to get started:

Link micro:bit board with computer via USB cable.

Open the offline version of Mu

**Test Code：**

Open Mu software, click Mode, then click“BBC micro：bit”and“OK”

![](media/ce7538ad76100ce9f54d9f05870ba0ef.png)

Tap“Load”, select“microbit-Heartbeat.py”file and click“open”

| File Type   | Route                          | File Name             |
|-------------|--------------------------------|-----------------------|
| Python file | ../Python Code/6.1：Heart beat | microbit-Heartbeat.py |

![](media/528306ef33a9ace70c2708ded273a7b8.png)

![](media/4cef305d30e5057d09ecf9e87a89141c.png)

There is another way to import code. Open Mu software and drag file“microbit-Heart beat.py”into it.

![dsBuffer.bmp](media/bdfdde51ab664b2bca3c31f9dee69ce7.png)

You can also input code in the editing window yourself.(note:all English words and symbols must be written in English)

```python
from microbit import *

while True:
    display.show(Image.HEART)
    sleep(500)
    display.show(Image.HEART_SMALL)
    sleep(500)
```

The following is a list of built-in images. If you are interested, you can select one of the following built-in images to replace the "Image.HEART" in the function show () in the figure above.

• Image.HEART

• Image.HEART_SMALL

• Image.HAPPY

• Image.SMILE

• Image.SAD

• Image.CONFUSED

• Image.ANGRY

• Image.ASLEEP

• Image.SURPRISED

• Image.SILLY

• Image.FABULOUS

• Image.MEH

• Image.YES

• Image.NO

• Image.CLOCK12, Image.CLOCK11, Image.CLOCK10, Image.CLOCK9, Image.CLOCK8, Image.CLOCK7, Image.CLOCK6, Image.CLOCK5,

Image.CLOCK4, Image.CLOCK3, Image.CLOCK2,Image.CLOCK1

• Image.ARROW_N, Image.ARROW_NE, Image.ARROW_E, Image.ARROW_SE, Image.ARROW_S, Image.ARROW_SW, Image.ARROW_W, Image.ARROW_NW

• Image.TRIANGLE

• Image.TRIANGLE_LEFT

• Image.CHESSBOARD

• Image.DIAMOND

• Image.DIAMOND_SMALL

• Image.SQUARE

• Image.SQUARE_SMALL

• Image.RABBIT

• Image.COW

• Image.MUSIC_CROTCHET

• Image.MUSIC_QUAVER

• Image.MUSIC_QUAVERS

• Image.PITCHFORK

• Image.PACMAN

• Image.TARGET

• Image.TSHIRT

• Image.ROLLERSKATE

• Image.DUCK

• Image.HOUSE

• Image.TORTOISE

• Image.BUTTERFLY

• Image.STICKFIGURE

• Image.GHOST

• Image.SWORD

• Image.GIRAFFE

• Image.SKULL

• Image.UMBRELLA

• Image.SNAKE，Image.ALL_CLOCKS，Image.ALL_ARROWS

Connect micro:bit board to computer with USB cable, click“Flash”to download code to micro:bit board.

![5(1)](media/18c70cf16dcf8c9694a1af8b12530cf9.png)

![](media/fee2f0f238a623c727b7a43418d97948.png)

The code, even it is wrong, can be downloaded to micro:bit board successfully, yet not working on micro:bit board.

Click“Flash”to download code to micro:bit.

![](media/b3617881628ec4860245d42668343769.png)

Click“REPL”and press the reset button on micro:bit, the error information will be displayed on REPL window, as shown below:

![](media/e4388c58829ba85568d1e054b0c8d233.png)

Click“REPL”again to turn off REPL mode, then you could refresh new code.

To make sure code correct, you only need to tap“Check”. The errors will be shown on the window.

![](media/f8c25d32fdafcfa24d8df86bc63be25f.png)

Modify the code according the prompt and click“Check”

![](media/448a50c26bc943e863e0cbf00f2e5677.png)

More tutorials, log in website please:<https://codewith.mu/en/tutorials/>

**Test Result:**

After testing, click“Flash”and download code to micro:bit, plug in power with USB cable. The micro:bit board shows“❤”and“![](media/04fdfc9060943954e7938bb1a741d626.png)”in loop way.

**Code Explanation：**

| **from**  microbit import       | Import the library file of micro：bit                        |
| ------------------------------- | ------------------------------------------------------------ |
| **while True:**                 | This is a permanent loop that makes micro:bit execute the code of it. |
| display.show(Image.HEART)       | micro：bit shows“❤”pattern                                   |
| sleep(500)                      | Delay in 500ms                                               |
| display.show(Image.HEART_SMALL) | micro：bit displays“![](media/04fdfc9060943954e7938bb1a741d626.png)” |

### 2：Light Up A Single LED

![](media/8c3f540a07aab97e1608ba8770837f7b.png)

**Description：**

Micro:bit motherboard consists of 25 light-emitting diodes, 5 pcs in a group. They correspond to x and y axis, therefore, the 5\*5 matrix is formed. Moreover, every diode locates at the point of x and y axis.

Virtually, we could control a LED by setting coordinate points. For instance, set coordinate point（0，0）to turn on the LED at row 1 and column 1; light up LED at the row 1 and column 3, we could set（2，0) and so on.

![](media/41c834c1592b4ecbec3066082c25f10b.png)

**Components:**

1.  Link micro:bit board with computer via USB cable.

2.  Open the offline version of Mu

**Test Code：**

Enter Mu software and open the file“microbit-Light up an LED .py”to import code:

| Type        | Route                               | File Name                    |
|-------------|-------------------------------------|------------------------------|
| Python file | ../Python code/6.2：Light up an LED | microbit-Light up an LED .py |

You can also input code in the editing window yourself.(note: all English words and symbols must be written in English)

```python
from microbit import *

val1 = Image("09000:""00000:""00000:""00000:""00000:")
val2 = Image("00000:""00000:""00000:""00000:""00090:")
val3 = Image("00000:""00000:""00000:""00000:""00000:")

while True:
    display.show(val1)
    sleep(500)
    display.show(val3)
    sleep(500)
    display.show(val2)
    sleep(500)
    display.show(val3)
    sleep(500)
```

Click“Check”to examine error in the code. The program proves wrong if underlines and cursors are shown.

![](media/b8022e717770b105d50d87a40a1c67ea.png)

If the code is correct, connect micro:bit to computer and click“Flash”to download code to micro:bit board

![](media/b53bb74cd132c97edb9a70b2a2190b4a.png)

**Test Result：**

After downloading code, plug in power with USB cable, you will see the LED at(1,0) flashes for 0.5s then the LED at (3,4) blinks for 0.5s, in loop way.

**Code Explanation：**

| **from** microbit import                                     | import the library file of micro:bit                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| val1 = Image("09000:""00000:""00000:""00000:""00000:") <br /><br /><br />val2 = Image("00000:""00000:""00000:""00000:""00090:")  val3 = Image("00000:""00000:""00000:""00000:""00000:") | Set Image() to val1 <br />Set pixel of LED on micro:bit to the value in 0\~9  <br />Pixel of each LED on micro:bit can be set in one of ten values If set pixel to 0 (zero), which means in close state, literally, 0 is brightness, 9 is best brightness <br />Set Image() to val2 <br />Set Image() to val3 |
| **while True:**                                              | This is a permanent loop that makes micro:bit execute the code of it. |
| display.show(val1)  <br />sleep(500)  <br />display.show(val3)  <br />sleep(500) | LED at (1,0) blinks for 0.5s                                 |
| display.show(val2)  <br />sleep(500)  <br />display.show(val3)  <br />sleep(500) | LED at (3,4) flashes for 0.5s                                |

Reference

sleep(ms) : delay time

For more details about delay, please refer to: [https://microbit-micropython.readthedocs.io/en/latest/utime.html](https://microbit-micropython.readthedocs.io/en/latest/utime.html)

### 3：5* 5 LED Dot Matrix

![](media/8c3f540a07aab97e1608ba8770837f7b.png)

**Description：**

Dot matrix gains popularity in our life, such as LED screen, bus station and the mini TV in the lift.

The dot matrix of Micro:bit board consists of 25 light emitting diodes. In previous lesson, we control LED of Micro:bit board to form patterns, numbers and character strings by setting the coordinate points. Moreover, we could adopt another way to complete the display of patterns, numbers and character strings.

**Components:**

1.  Link micro:bit board with computer via USB cable.

2.  Open the offline version of Mu

**Test Code：**

**Code 1：**

You could open“Code 1.py”file to Import code 

| File Type   | Route                                  | File Name |
|-------------|----------------------------------------|-----------|
| Python file | ../Python code/6.3：5×5 LED Dot Matrix | Code 1.py |

You can also input code in the editing window yourself.(note:all English words and symbols must be written in English)

```python
from microbit import *

val = Image("00900:""00900:""90909:""09990:""00900")

display.show(val)
```

Click “Check” to examine error in the code. The program proves wrong if underlines and cursors are shown.

![](media/1fc05cf964a5d7927ec704c6b7f1acdd.png)

 If the code is correct, connect micro:bit to computer and click“Flash”to download code to micro:bit board

![](media/7f87636ae757d87584c8d5552e00c513.png)

**Code 2：**

Enter Mu software and open“Code 2.py“file to import code

| File Type   | Route                                  | File Name |
|-------------|----------------------------------------|-----------|
| Python file | ../Python code/6.3：5×5 LED Dot Matrix | Code 2.py |

You can also input code in the editing window yourself.(note:all English words and symbols must be written in English)

```PYTHON
from microbit import *
val = Image("00900:""00900:""90909:""09990:""00900")
display.show('1')
sleep(500)
display.show('2')
sleep(500)
display.show('3')
sleep(500)
display.show('4')
sleep(500)
display.show('5')
sleep(500)
display.show(val)
sleep(500)
display.scroll("hello!")
sleep(200)
display.show(Image.HEART)
sleep(500)
display.show(Image.ARROW_NE)
sleep(500)
display.show(Image.ARROW_SE)
sleep(500)
display.show(Image.ARROW_SW)
sleep(500)
display.show(Image.ARROW_NW)
sleep(500)
display.clear()
```

Click “Check” to examine error in the code. The program proves wrong if underlines and cursors are shown.

![](media/4d2888634c7d86e2cb6186d8c50b7174.png)

If the code is correct, connect micro:bit to computer and click“Flash”to download code to micro:bit board.

![](media/98f588b6c1b4a2d3ef4efca3e7c030e6.png)

**Test Result：**

Download code 1 to micro:bit and keep USB cable connected , we will see the![](media/d4e278da768e447ed344d581e671f57a.png) icon.

Download code 2. Micro: bit starts showing number 1, 2, 3, 4, and 5, then cyclically display![](media/d4e278da768e447ed344d581e671f57a.png),“Hello!”, ![](media/66b31365d42274ef94ce9a3fcea1cd6c.png),![](media/39fe4029acb5fb675d875c58e382d148.png),![](media/45fcde65eb80a942d3903e400a346587.png),![](media/9e34fdb19d72918bde242994a3c94c1f.png) and![](media/2a45fca9d836ce38674c347c70c81e02.png)patterns.

**Code Explanation：**

| Code                                                         | Explanation                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| **from** microbit **import** \*                              | import the library file of micro:bit                         |
| val = Image("09000:""00000:""00000:""00000:""00000:")        | Set Image() to variable val                                  |
| display.show(val)                                            | micro:bit shows“→”                                           |
| display.show('1')                                            | micro:bit shows“1”                                           |
| sleep(500)                                                   | Delay in 500ms                                               |
| display.scroll("hello!")                                     | micro:bit scrolls to show“hello!”                            |
| display.show(Image.HEART)                                    | micro:bit displays“❤”pattern                                 |
| display.show(Image.ARROW_NE) <br />display.show(Image.ARROW_SE) <br />display.show(Image.ARROW_SW)  <br />display.show(Image.ARROW_NW) | micro:bit shows“Northeast”arrow <br />micro:bit displays“Southeast”arrow <br />micro:bit shows“Southwest”arrow <br />micro:bit displays“Northwest”arrow |
| display.clear()                                              | The LED dot matrix of micro:bit clears                       |

**Reference：**

display.scroll() ：scroll to display the value on screen. If the value is integer or float, transfer it into character string via str（）.

The display scrolls to show the values, if it is integer or float, we use str（）to transfer into character strings.

More details, please refer to<https://microbit-micropython.readthedocs.io/en/latest/utime.html>

### 4：Programmable Buttons

![](media/06be84fb11b1fd07cd0cbb392132b903.png)

**Description：**

The button can control the on and off of the circuit. The button is attached to the circuit. The circuit is disconnected when the button is not pressed. The circuit is connected as soon as it is pressed, but it is disconnected after being released.

Both ends of button are like two mountains. There is a river in between.

The internal metal piece connect the two sides to let the current pass, just like building a bridge to connect the two mountains.

Micro:bit board has three buttons, the reset button on the back and two programmable buttons on the front. By pressing these buttons, the corresponding characters will be displayed on dot matrix.

**Components:**

1.  Link micro:bit board with computer via USB cable.

2.  Open the offline version of Mu

**Test Code：**

**Code 1：**

Open the file“Code 1.py“ in Mu software

| File Type   | Route                                    | File Name |
|-------------|------------------------------------------|-----------|
| Python file | ../Python code/6.4：Programmable Buttons | Code 1.py |

You can also input code in the editing window yourself.(note:all English words and symbols must be written in English)

```python
from microbit import *

while True:
    if button_a.is_pressed():
        display.show("A")
    elif button_a.is_pressed() and button_b.is_pressed():
        display.scroll("AB")
    elif button_b.is_pressed():
        display.show("B")
```

Click “Check” to examine error in the code. The program proves wrong if underlines and cursors are shown.

![](media/093160b7639ca86ad83ae4d7ea389871.png)

If the code is correct, connect micro:bit to computer and click“Flash”to download code to micro:bit board.

Then tap“Flash”to download code to micro:bit.

![](media/a2662ba8f13554b031daa944993f0fb1.png)

**Code 2：**

Open the file“Code 2.py”in Mu

| File Type   | Route                                 | File Name |
|-------------|---------------------------------------|-----------|
| Python file | ../Projects/6.4：Programmable Buttons | Code 2.py |

You can also input code in the editing window yourself.(note:all English words and symbols must be written in English)

```python
from microbit import *
a = 0
b = 0
val1 = Image("00000:""00000:""00000:""00000:""00900")
val2 = Image("00000:""00000:""00000:""00900:""99999")
val3 = Image("00000:""00000:""00900:""99999:""99999")
val4 = Image("00000:""00900:""99999:""99999:""99999")
val5 = Image("00900:""99999:""99999:""99999:""99999")
val6 = Image("99999:""99999:""99999:""99999:""99999")
display.show(val1)

while True:
    while button_a.is_pressed() == True:
        sleep(10)
        if button_a.is_pressed() == False:
            a = a + 1
            if(a >= 5):
                a = 5
            break
    while button_b.is_pressed() == True:
        sleep(10)
        if button_b.is_pressed() == False:
            a = a - 1
            if(a <= 0):
                a = 0
            break
    if a == 0:
        display.show(val1)
    if a == 1:
        display.show(val2)
    if a == 2:
        display.show(val3)
    if a == 3:
        display.show(val4)
    if a == 4:
        display.show(val5)
    if a == 5:
        display.show(val6)
```

Click “Check” to examine error in the code. The program proves wrong if underlines and cursors are shown.

![](media/1140fc004ffa65ecdf206193919f2f0f.png)

![](media/94849305cba4d1cb307d2d73376f4e18.png)

If the code is correct, connect micro:bit to computer and click“Flash”to download code to micro:bit board. Then click“Flash”to download code to micro:bit board.

![](media/e1fe9b6dc1304cae9a190b55a8b22892.png)

![](media/94849305cba4d1cb307d2d73376f4e18.png)

**Test Result：**

Upload code 1 and plug in micro:bit via USB cable, press“A”on Micro:bit board, character“A”will be displayed; in case that B is pressed, letter“B”will appear. So will show“AB”if you press A and B buttons simultaneously.

Upload code 2 and plug in board via USB cable. Press button A, a row of luminous LEDs are added, when B is pressed, a row of luminous LEDs are deducted.

**Code Explanation：**

| Code                                                         | Explanation                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| **from** microbit **import** \*                              | import the library file of micro:bit                         |
| **while True:**                                              | This is a permanent loop that makes micro:bit execute the code of it. |
| **if** button_a.is_pressed(): <br />display.show("A") <br />**elif** button_a.is_pressed() **and** <br />button_b.is_pressed(): <br />display.scroll("AB") <br />**elif** button_b.is_pressed(): <br />display.show("B") | If button A is pressed <br />micro:bit shows“A” <br />If button A and B are pressed at same time <br />micro:bit displays“AB” <br />If button B is pressed <br />micro:bit shows“B” |
| **while** button_a.is_pressed() == **True**: sleep(10) <br />**if** button_a.is_pressed() == **False**: <br />a = a + 1 <br />**if**(a \>= 5): <br />a = 5 <br />break <br />**while** button_b.is_pressed() == **True**: <br />sleep(10) <br />**if** button_b.is_pressed() == **False**: <br />a = a - 1 <br />**if**(a \<= 0): <br />a = 0 <br />break <br />**if** a == 0: display.show(val1) <br />**if** a == 1: <br />display.show(val2) <br />**if** a == 2: <br />display.show(val3) <br />**if** a == 3: <br />display.show(val4) <br />**if** a == 4: <br />display.show(val5) <br />**if** a == 5: <br />display.show(val6) | When the button A is pressed <br />Delay in 10ms to eliminate the shaking of button A <br />when button A is released, <br />Variable a adds 1 <br />If variable a≥5 <br />Variable a=5 <br />exit the loop  <br />when button B is pressed <br />Delay in 10ms to eliminate the shaking of button B <br />When the button B is released <br />Variable a reduces 1 gradually <br />When a≤0 <br />Variable a=0 <br />exit the loop <br />When a=0 <br />micro:bit shows pattern val1 <br />When a=1 <br />micro:bit displays pattern val2 <br />When a=2 <br />micro:bit shows pattern val3 <br />If a=3 <br />micro:bit displays pattern val4 <br />If a=4 <br />micro:bit shows pattern val5 <br />If a=5 <br />micro:bit displays pattern val6 |

### 5: Temperature Measurement

**Description：**

Micro:bit main board contains temperature sensor, as micro:bit is small pocket-sized computer, it has a micro processor. That means this is a tiny electronic component with less power than normal computer processor, which is
one of the reason your micro：bit is so small and can run on batteries.

The micro:bit processor runs the program you create for your micro:bit so when you write a program in online editors, then transfer it to your micro:bit. The processor is where your program runs.

**Note: the temperature sensor is included in the processor.**

![](media/206c8ec1c3f11d2de8d0f42fdf5b6b47.png)

**Components:**

1.  Link micro:bit board with computer via USB cable.

2.  Open the offline version of Mu

**Test Code：**

**Code 1：**

Open“Code 1.py“ file in Mu

| File Type   | Route                                         | File Name |
|-------------|-----------------------------------------------|-----------|
| Python file | ../Python code/6.5：Temperature Measurement / | Code 1.py |

You can also input code in the editing window yourself.(note:all English words and symbols must be written in English)

```python
from microbit import *

while True:

    Temperature = temperature()

    print("Temperature:", Temperature, "C")

    sleep(500)
```

Click“Check”to examine error in the code. The program proves wrong if underlines and cursors are shown. 

![IMG_256](media/ebfabcefe31fd4f4093fd63e5d284ad9.png)

If the code is correct, connect micro:bit to computer and click“Flash”to download code to micro:bit board.

![](media/7eb957d5c7b39372af31a4b2bd264525.png)

After downloading test code 1 to micro:bit board, keep USB connected and click**“REPL”and press the reset button on micro:bit.** Then REPL window will show the ambient temperature value, as shown below:( C stands for temperature unit)

![IMG_256](media/db5c433810c37c8d9f75a62ff99eb1e5.png)

**Code 2：**

Open“Code 2.py” in Mu

| File Type   | Route                                        | File Name |
|-------------|----------------------------------------------|-----------|
| Python file | ../Python code/6.5：Temperature Measurement  | Code 2.py |

Or, you could input code in the editing window by yourself.

The temperature value can be set in compliance with the real temperature.

```python
from microbit import *

while True:

    if temperature() >= 35:
        display.show(Image.HEART)

    else:
        display.show(Image.HEART_SMALL)
```

Click “Check” to examine error in the code. The program proves wrong if underlines and cursors are shown. 

![](media/de39f120be5bc9a7a0834bc4e3b5bc00.png)

If the code is correct, connect micro:bit to computer and click“Flash”to download code to micro:bit board

![](media/2262cefaaa9143fc37ad6d53d6404b49.png)

**Test Result**

Upload the code 2 plug in micro:bit via USB cable, when the ambient temperature is less than 35℃, 5\*5LED will
show![](media/4b1765e12b413dc5d562f2a16d32392f.png). When the temperature is equivalent to or greater than 35℃, the pattern![](media/f2705fbc4886efcfaac96589ca255f66.png) will appear.

**Code Explanation：**

| Code                                                         | Explanation                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| **from** microbit **import** \*                              | import the library file of micro:bit                         |
| **while True:**                                              | This is a permanent loop that makes micro:bit execute the code of it. |
| Temperature = temperature()                                  | Set temperature() to Temperature                             |
| print("Temperature:", Temperature, "C")                      | BBC micro:bit REPL prints temperature value                  |
| sleep(500)                                                   | Delay in 500ms                                               |
| **if** temperature() \>= 35: <br />display.show(Image.HEART)  <br />**else**:  <br />display.show(Image.HEART_SMALL) | If temperature value ≥35℃  <br />micro:bit shows“♥” <br />If temperature value\<35℃  <br />micro:bit displays“![](media/04fdfc9060943954e7938bb1a741d626.png)” |

### 6：Micro:bit’s Compass

![](media/24c31bb0174e2ac672203e5c36c6875e.png)

**1. Description：**

This project mainly introduces the use of the Micro:bit’s compass. In addition to detecting the strength of the magnetic field, it can also be used to determine the direction, an important part of the heading and attitude reference
system (AHRS) as well.   It uses FreescaleMAG3110 three-axis magnetometer. Its I2C interface communicates with the outside, the range is ±1000µT, the maximum data update rate is 80Hz.
Combined with accelerometer, it can calculate the position. Additionally, it is applied to magnetic detection and compass blocks.

Then we could read the value detected by it to determine the location. We need to calibrate the Micro:bit board when magnetic sensor works.

The correct calibration method is to rotate the Micro:bit board. In addition, the objects nearby may affect the accuracy of readings and calibration.

**2. Components:**

1.  Link micro:bit board with computer via USB cable.

2.  Open the offline version of Mu

**3. Test Code：**

**Code 1：**

**When the button A is pressed, the window displays the value of compass.**

Open file“Code 1.py“ in Mu

| File Type   | Route                                   | File Name |
|-------------|-----------------------------------------|-----------|
| Python file | ../Python code/6.6：Micro:bit’s Compass | Code 1.py |

You can also input code in the editing window yourself.(Note:all English words and symbols must be written in English)

```python
from microbit import *

compass.calibrate()

while True:

    if button_a.is_pressed():
        display.scroll(compass.heading())

```

Click“Check”to examine error in the code. The program proves wrong if underlines and cursors are shown. 

![](media/c5cf34a6b570ed75af57634daf62796b.png)

If the code is correct, connect micro:bit to computer and click“Flash”to download code to micro:bit board

![](media/d9bbfd110a525e5a43c76abd0a22f43b.png)

**Code Explanation：**

We need to calibrate micro：bit due to different magnetic field in different areas. Micro:bit will prompt you to calibrate when you use it first time.

Transfer code 1 to micro:bit, plug in micro:bit via USB cable and press button A.“TILT TO FILL SCREEN”appears on micro:bit. Then enter the calibration interface, the calibration method is to rotate the micro:bit board and display a full square pattern(25 LEDs are on), as shown in the following figure:

![1(5)](media/acf3b8c0dee027d9e555fc708831f874.jpeg)

The calibration is finished until you view the smile pattern![](media/a4faf86fb027b2f4c3dacaeee5d47d2b.png)appear.

The serial monitor will show 0°, 90°, 180°and 270° when pressing A.

**Code 2：**

Make micro: bit board point to the north, south, east and west horizontally , LED dot matrix displays the corresponding direction patterns.

![](media/d1a4e9f62bdf690ba809ae35c347b233.png)

For the above picture, the arrow pointing to the upper right when the value ranges from 292.5 to 337.5. 0.5 can’t be input in the code, thereby, the values we get are 293 and 338

Open“Code 2.py“ file in Mu

| File Type   | Route                                   | File Name |
|-------------|-----------------------------------------|-----------|
| Python file | ../Python code/6.6：Micro:bit’s Compass | Code 2.py |

Or, you could input code in the editing window by yourself.

```python
from microbit import *
compass.calibrate()
x = 0
while True:
    x = compass.heading()
    if x >= 293 and x < 338:
        display.show(Image("00999:""00099:""00909:""09000:""90000"))
    elif x >= 23 and x < 68:
        display.show(Image("99900:""99000:""90900:""00090:""00009"))
    elif x >= 68 and x < 113:
        display.show(Image("00900:""09000:""99999:""09000:""00900"))
    elif x >= 113 and x < 158:
        display.show(Image("00009:""00090:""90900:""99000:""99900"))
    elif x >= 158 and x < 203:
        display.show(Image("00900:""00900:""90909:""09990:""00900"))
    elif x >= 203 and x < 248:
        display.show(Image("90000:""09000:""00909:""00099:""00999"))
    elif x >= 248 and x < 293:
        display.show(Image("00900:""00090:""99999:""00090:""00900"))
    else:
        display.show(Image("00900:""09990:""90909:""00900:""00900"))
```

Click“Check”to examine error in the code. The program proves wrong if underlines and cursors are shown. 

![](media/70cd7ec37561e9e2d512d2e9dd9166ca.png)

If the code is correct, connect micro:bit to computer and click“Flash”to download code to micro:bit board

![](media/4de55e27643528af326ebf9cabe4054c.png)

**4.Test Result：**

Upload code 2 onto micro:bit board and don’t plug off USB cable. After calibration, tilt Micro:bit board, the LED dot matrix displays the direction signs.

**Code Explanation：**

| Code                                                         | Explanation                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| **from** microbit **import** \*                              | import the library file of micro:bit                         |
| compass.calibrate()                                          | Compass calibration                                          |
| **while True:**                                              | This is a permanent loop, which makes micro:bit execute the code of it. |
| **if** button_a.is_pressed():  <br />display.scroll(compass.heading()) | When the button A is pressed Micro:bit scrolls to show the value of compass |
| x = 0                                                        | Set variable x=0                                             |
| x = compass.heading()                                        | Set the value of compass to variable x                       |
| if...else if...else                                          | Condition judgement statement:if...else if...else            |
| display.show(Image("00999:""00099:""00909:""09000:""90000")) <br />display.show(Image("99900:""99000:""90900:""00090:""00009")) <br />display.show(Image("00900:""09000:""99999:""09000:""00900")) <br />display.show(Image("00009:""00090:""90900:""99000:""99900")) <br />display.show(Image("00900:""00900:""90909:""09990:""00900")) <br />display.show(Image("90000:""09000:""00909:""00099:""00999")) <br />display.show(Image("00900:""00090:""99999:""00090:""00900")) <br />display.show(Image("00900:""09990:""90909:""00900:""00900")) | Micro:bit shows the Northeast arrow sign <br />Micro:bit shows the Northwest arrow sign <br />Micro:bit shows the west arrow sign <br />Micro:bit shows the Southwest arrow sign <br />Micro:bit shows the South arrow sign <br />Micro:bit shows the South arrow sign  <br />Micro:bit shows the East arrow sign <br />Micro:bit shows the North arrow sign |

### 7: Accelerometer

**1. Description：**

![](media/24c31bb0174e2ac672203e5c36c6875e.png)

The micro:bit V2 has a built-in LSM303AGR accelerometer, with the 8, 10 and 12 resolution.

We use an accelerometer to detect the posture of machine.

We will make the accelerometer to detect a few postures and check its initial value at x, y and z axis.

**2. Components:**

1.  Link micro:bit board with computer via USB cable.

2.  Open the offline version of Mu

**3. Test Code：**

**Code 1：**

Open“Code 1.py” file in Mu

| File Type   | Route                             | File Name |
|-------------|-----------------------------------|-----------|
| Python file | ../Python code/6.7：Accelerometer | Code 1.py |

You can also input code in the editing window yourself.(note:all English words and symbols must be written in English)

```python
from microbit import *

while True:
    gesture = accelerometer.current_gesture()

    if gesture == "shake":
        display.show("1")
    if gesture == "up":
        display.show("2")
    if gesture == "down":
        display.show("3")
    if gesture == "face up":
        display.show("4")
    if gesture == "face down":
        display.show("5")
    if gesture == "left":
        display.show("6")
    if gesture == "right":
        display.show("7")
    if gesture == "freefall":
        display.show("8")
```

Click “Check” to examine error in the code. The program proves wrong if underlines and cursors are shown.

![](media/d0a621d072f0be197fe69020da3c7f0c.png)

If the code is correct, connect micro:bit to computer and click“Flash”to download code to micro:bit board

![](media/9e717d740c0fc72d7d064dcf1b68b51b.png)

**Code 2：**

**Detect different acceleration values on X, Y and Z axis.**

Open file“Code 2.py”in Mu

| File Type   | Route                             | File Name |
|-------------|-----------------------------------|-----------|
| Python file | ../Python code/6.7：Accelerometer | Code 2.py |

You can also input code in the editing window yourself.(Note:all English words and symbols must be written in English)

```python
from microbit import *

while True:

    x = accelerometer.get_x()

    y = accelerometer.get_y()

    z = accelerometer.get_z()

    print("x, y, z:", x, y, z)

    sleep(100)
```

Click“Check”to examine error in the code. The program proves wrong if underlines and cursors are shown.

![](media/a481a470354fd3ebc573f621041ee9dd.png)

If the code is correct, connect micro:bit to computer and click“Flash”to download code to micro:bit board.

![](media/7ba7c6eb2373317f2de54eab3ddf0336.png)

Look up the MMA8653FC manual

The coordinates of the Micro:bit accelerometer are shown in the following igure:

![10](media/6303a0ac122680207fe856d9be38d01c.png)

The value of acceleration on the X-axis, Y-axis, and Z-axis, as well as the synthesis of acceleration (the synthesis of gravitational acceleration and other external forces). Then flip the micro:bit board, the data is shown below:

Download code 2 onto micro:bit board, and don’t pull off the USB cable.

Click“REPL”and press the reset button. The value of acceleration on X axis, Y axis and Z axis are shown below

![](media/6d30d1f183087e759b85403b0bddcbbd.png)

**4. Test Result：**

Download code 1 to micro:bit board and plug in power with USB cable shake the Micro:bit board then the number 1 appears.

When the logo points to the North, the number 2 will be displayed:

![\_DSC3687](media/1600323e3e61e331c248cbeda5ccdcfc.jpeg)

When the logo points to the South, the number 3 will be displayed:

![\_DSC3688](media/3be80acf957e53117f695801ce19c449.jpeg)

When the LED dot matrix faces up, the number 4 will be shown.

However, when dot matrix faces down, the number 5 will be displayed.

When the micro:bit is tilt to the left, the number 6 will be shown.

![\_DSC3703](media/326095934bcff0a925b4f9a09d6cf7d2.jpeg)

![\_DSC3697](media/185b0ac204e9b2c54dd8fa93d852568c.jpeg)

Yet, the board is inclined to the right, the number 7 is displayed.

When the micro:bit is free fall(accidentally making it fall), the number 8 will appear. （Note：we don’t recommend you to make it free fall because board will get damaged)

**5.Code Explanation：**

| Code                                                         | Explanation                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| **from** microbit **import** \*                              | import the library file of micro:bit                         |
| gesture = accelerometer.current_gesture()                    | Set accelerometer.current_gesture() to gesture               |
| **while True:**                                              | This is a permanent loop that makes micro:bit execute the code of it. |
| **if** gesture == "shake":  <br />display.show("1")  <br />**if** gesture == "up":  <br />display.show("2")  <br />**if** gesture == "down":  <br />display.show("3")  <br />**if** gesture == "face up":  <br />display.show("4")  <br />**if** gesture == "face down":  <br />display.show("5")  <br />**if** gesture == "left":  <br />display.show("6")  <br />**if** gesture == "right":  <br />display.show("7")  <br />**if** gesture == "freefall":  <br />display.show("8") | Shaking micro:bit board, number 1 will appear <br /><br />When log points to the North, number 2 will show up. <br /><br />When log points to the South, number 3 will be shown <br /><br />When the LED dot matrix is upward, the number 4 is shown. <br /><br />the number 5 is displayed when the LED dot matrix is downward. <br /><br />When Micro:bit board is tilt to the left, number 6 is shown. <br /><br />When micro:bit is tilt to the right, number 7 is displayed. <br /><br />When it is free fall(accidentally making it fall), number 8 appears on dot matrix. |
| x = accelerometer.get_x()  <br /><br />y = accelerometer.get_y()  <br /><br />z = accelerometer.get_z() | Read the acceleration value on x axis, the return value is integer, <br />and set x= the read value on x axis <br />Read the acceleration value on y axis, the return value is integer, <br />and set y= the read value on y axis <br />Read the acceleration value on z axis, the return value is integer, <br />and set z= the read value on z axis |
| print("x, y, z:", x, y, z)                                   | The value of acceleration will be shown                      |
| sleep(100)                                                   | Delay in 100ms                                               |

### 8: Detect Light Intensity by micro:bit

![](media/8c3f540a07aab97e1608ba8770837f7b.png)

**Description：**

This project will introduce how micro:bit detects the external light intensity. Since Micro:bit doesn’t come with photosensitive sensor, the detection of light intensity is completed through the LED matrix. When the light irradiates the LED matrix, the voltage change will be produced. Therefore, we could determine the light intensity by voltage change.

**What you need to get started**

1.  Link micro:bit board with computer via USB cable.

2.  Open the offline version of Mu


**Test Code：**

Open“microbit-Detect Light Intensity by Micro:bit .py” file in Mu  software

| File Type   | Route                                                    | File Name                                        |
|-------------|----------------------------------------------------------|--------------------------------------------------|
| Python file | ../Python code/6.8：Detect Light Intensity by Micro:bit  | microbit-Detect Light Intensity by Micro:bit .py |

You can also input code in the editing window yourself.(Note:all English words and symbols must be written in English)

```python
from microbit import *

while True:

    Lightintensity = display.read_light_level()

    print("Light intensity:", Lightintensity)

    sleep(100)

```

Click“Check”to examine error in the code. The program proves wrong if underlines and cursors are shown. 

![](media/b19b1c95da181d658ce08532c6f75040.png)

If the code is correct, connect micro:bit to computer and click“Flash”to download code to micro:bit board.

![](media/ebcd15db1728149955b26857a0ae726f.png)

**Test Result：**

Download code onto micro:bit board, don’t plug off USB cable. Click “REPL”and press the reset buttons, the light intensity value will be displayed, as shown below.

Covering the LED dot matrix, the intensity value is 0; on the contrary, the intensity value increases when placing micro:bit board under the sun.

![](media/0ec112824972ca026fcad43dc61aa5bc.png)

**5.Code Explanation：**

| Code                                        | Explanation                                                 |
| ------------------------------------------- | ----------------------------------------------------------- |
| **from** microbit **import** \*             | import the library file of micro:bit                        |
| gesture = accelerometer.current_gesture()   | Set accelerometer.current_gesture() to gesture              |
| **while True:**                             | This is permanent loop, and micro bit executes the code     |
| Lightintensity = display.read_light_level() | Set display.read_light_level() to Lightintensity            |
| print("Light intensity:", Lightintensity)   | BBC microbit REPL prints the detected light intensity value |
| sleep(100)                                  | Delay in 100ms                                              |

### 9: Speaker

![](media/ac515b9ae8891dc32f368a29f194a2fb.png)

**Description：**

There is a built-in speaker in the micro:bit board. The speaker can help you make a number of interesting projects, like playing song“Ode to Joy”.

**Preparation：**

1.  Attach the micro:bit to your computer

2.  Enter the offline Mu software


**Test Code：**

Open“microbit-Speaker .py”in Mu

| File Type   | Route                       | File Name           |
|-------------|-----------------------------|---------------------|
| Python file | ../Python code/6.9：Speaker | microbit-Speaker.py |

You can also input code in the editing window yourself.(note:all English words and symbols must be written in English)

```python
from microbit import *

import audio

while True:
    audio.play(Sound.GIGGLE)
    sleep(1000)
    audio.play(Sound.HAPPY)
    sleep(1000)
    audio.play(Sound.HELLO)
    sleep(1000)
    audio.play(Sound.YAWN)
    sleep(1000)

```

Click“Check”to examine errors in the code. If underlines and cursors are shown under the code, which means wrong program.

![](media/23e333e566a34d9236571e7ef868eb71.png)

If the code is correct, connect micro:bit to computer and click“Flash”to download code to micro:bit board

![](media/6a9eb140e75e4e837254b26fb1e9164b.png)

**Test Result：**

Download code to micro:bit and attach USB cable to power. Then the micro:bit will emit a sound .

**Code Explanation：**

| **from**  microbit  **import** \* | Import the library of the micro：bit                                           |
|-----------------------------------|--------------------------------------------------------------------------------|
| **import** audio                  | Audio library                                                                  |
| **while True:**                   | This is an infinite loop which makes the micro:bit permanently drive this code |
| audio.play(Sound.GIGGLE)          | Emit“giggle”sound                                                              |
| sleep(1000)                       | Delay in 1000ms                                                                |

### 10: Touch Sensitive Logo

![](media/644695850097c5ade080bb4848b4b481.png)

**Description：**

The touch sensitive logo is seen as an input(button). In fact, inside in the micro:bit embeds a capacitive touch sensor. It can sensor your touch and trigger a series of actions.

**Preparation：**

(1) Link micro:bit board with computer via USB cable.

(2) Open the offline version of Mu

**Test Code：**

Open the“microbit-Touch Sensitive Logo .py“ file in Mu

| File Type   | Route                                     | File Name                        |
|-------------|-------------------------------------------|----------------------------------|
| Python file | ../Python code/6.10：Touch Sensitive Logo | Microbit-Touch Sensitive Logo.py |

You can also input code in the editing window yourself.(note:all English words and symbols must be written in English)

```python
from microbit import *
time = 0
start = 0
running = False

while True:

    if button_a.was_pressed():
        running = True
        start = running_time()
    if button_b.was_pressed():
        if running:
            time += running_time() - start
        running = False
    if pin_logo.is_touched():
        if not running:
            display.scroll(int(time/1000))

    if running:
        display.show(Image.HEART)
        sleep(300)
        display.show(Image.HEART_SMALL)
        sleep(300)
    else:
        display.show(Image.ASLEEP)
```

Click“Check”to examine errors in the code. If underlines and cursors are shown under the code, which means wrong program.

![](media/171ad82abb6d81dc520c2cd75a21c4f7.png)

If the code is correct, connect micro:bit to computer and click“Flash”to download code to micro:bit board

![](media/e631d635ef02b0bb96855437fd93913d.png)

**Test Result：**

When you press button A, LED will show heart beat icon; and the button B is used to stop showing the image. In addition, touch logo then the micro:bit will count time as a stopwatch; press the reset button to restart counting time.

### 11: Microphone

![](media/3073a8af772ab91ecf264843b37d3b74.png)![](media/7f0741158e734ff8449d5b87d5ba85f4.png)

**1. Description：**

The micro:bit V2 includes a built-in microphone which can detect the sound intensity. Additionally, there is a microphone LED indicator at the back. Its indicator will turn on if you clap your hands; therefore, we can make an analog noise detection watch.

**2. Preparation：**

1.  Attach the micro:bit to your computer

2.  Enter the offline Mu software

**3. Test Code：**

Code 1：

Open the file“microbit-Microphone-1.py”in Mu

| File Type   | Route                           | File Name                |
|-------------|---------------------------------|--------------------------|
| Python file | ../Python code/6.11：Microphone | microbit-Microphone-1.py |

You can also input code in the editing window yourself.(note:all English words and symbols must be written in English)

```python
from microbit import *

while True:
    if microphone.current_event() == SoundEvent.LOUD:
        display.show(Image.HEART)
        sleep(200)
    if microphone.current_event() == SoundEvent.QUIET:
        display.show(Image.HEART_SMALL)
```

Click“Check”to examine errors in the code. If underlines and cursors are shown under the code, which means wrong program.

![](media/56f1289435344510fe6bddacc8048d01.png)

If the code is correct, connect micro:bit to computer and click“Flash”to download code to micro:bit board.

![](media/8bd0888f9d83fe537e1d459be1c758f9.png)

Download code 1 to the micro:bit and attach USB cable to power. The micro:bit will display“❤”image when you clap your hands; however, it will show“![](media/04fdfc9060943954e7938bb1a741d626.png)”when you are in the quiet environment.

**Code 2：**

Open the file“microbit- Microphone -2.py“ in Mu

| File Type   | Route                           | File Name                   |
|-------------|---------------------------------|-----------------------------|
| Python file | ../Python code/6.11：Microphone | Micro:bit- Microphone -2.py |

You can also input code in the editing window yourself.(Note:all English words and symbols must be written in English)

```python
from microbit import *
maxSound = 0
lights = Image("11111:"
              "11111:"
              "11111:"
              "11111:"
              "11111")
# ignore first sound level reading
soundLevel = microphone.sound_level()
sleep(200)

while True:
    if button_a.is_pressed():
        display.scroll(maxSound)
    else:
        soundLevel = microphone.sound_level()
        display.show(lights * soundLevel)
        if soundLevel > maxSound:
            maxSound = soundLevel
```

Click“Check”to examine errors in the code. If underlines and cursors are shown under the code, which means wrong program.

![](media/579f51b2a0292d31d7ef4535e1b02155.png)

If the code is correct, connect micro:bit to computer and click“Flash”to download code to micro:bit board.

![](media/eacd0b4e2ba068ed3fc5d171cd8bfa3a.png)

**4.Test Result：**

Download code to the micro:bit, plug in power with USB cable. When you press button A, the LED dot matrix will show the maximum sound value( reset the maximum value via reset button). The louder the detected sound, the brighter the LED dot matrix

**5.Code Explanation：**

| **from**  microbit  **import** \*                            | Import the library of micro：bit                             |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| **while True:**                                              | This is an infinite loop which makes the <br />micro:bit permanently drive this code |
| if microphone.current_event() == SoundEvent.LOUD: <br />display.show(Image.HEART) <br />sleep(200) <br />if microphone.current_event() == SoundEvent.QUIET: <br />display.show(Image.HEART_SMALL) | When microphone detects the sound <br />LED displays“❤” <br />Delay in 200ms <br /><br />If the sounding environment is quiet <br />LED shows “![](media/04fdfc9060943954e7938bb1a741d626.png)” |
| print("Light intensity:", Lightintensity)                    | BBC micro:bit REPL prints the detected light intensity value |
| maxSound = 0                                                 | The initial value of the variable maxSound is 0              |
| lights = Image("11111:""11111:""11111:""11111:""11111")      | Set Image() to variable lights                               |
| soundLevel = microphone.sound_level()                        | Set microphone.sound_level() to variable soundLevel          |
| if button_a.is_pressed(): <br />display.scroll(maxSound) <br />else: <br />soundLevel = microphone.sound_level() <br />display.show(lights \* soundLevel) <br />if soundLevel \> maxSound: <br />maxSound = soundLevel | when the button A is pressed <br />LED matrix shows the sound value <br />If not <br />Set microphone.sound_level() to variable soundLevel <br />The LED dot matrix acts like the breathing light <br />If sound level value is greater than the maximum sound value<br />The maximum sound value equals the sound level value |

### 12: Bluetooth Wireless Communication

Micro:bit board comes with NRF51822 processor, Bluetooth and 2.4GHz RF antenna, which work with Bluetooth and 2.4G wireless communication.

In this project, we connect cellphone to Micro:bit motherboard to complete the wireless connection.

With 16k RAM, micro:bit owns a low-consumption Bluetooth module and support Bluetooth communication. However, BLE heap stack occupies 12K RAM, which implies that there is no enough space to run microPython.

At present, microPython doesn’t support Bluetooth.

<https://microbit-micropython.readthedocs.io/en/latest/ble.html>

In the further lessons, we will conduct experiments with micro:bit and other sensors or modules.

**Special note: Disconnect power before installing or removing micro:bit onKeyestudio T Type Shield, which can prevent from burning micro:bit.**

### 13: Passive Sensor

![](media/da6ec0cad581a9429307efe57c566b70.png)

**Description：**

We can use Micro:bit board to make many interactive works of which the most commonly used is acoustic-optic display. The previous lessons are related to LED. However, we will elaborate the sound in this lesson.

Buzzer is inclusive of active buzzer and passive buzzer.

The passive buzzer doesn’t carry with vibrator inside, so it need external sine or square wave to drive. It can produce slight sound when connecting directly to power supply. It features controlling sound frequency and producing the sound of“do re mi fa so la si”.

A diode should be connected in reverse when driving by the square wave signal source, which will hinder the high-voltage generated to damage other components or service life when the power breaks down.

Frequency is made of a series of pitch names in English letters and Numbers. You can choose different frequencies, that is, tone. The frequency of sound is called pitch.

It involves music knowledge. In music lesson, our teacher taught“1（Do）, 2（Re）, 3(Mi), 4(Fa) , 5(Sol), 6(La), 7(Si)”

| 1（Do） | 2（Re） | 3(Mi) | 4(Fa) | 5(Sol) | 6(La) | 7(Si) |
|---------|---------|-------|-------|--------|-------|-------|
| C       | D       | E     | F     | G      | A     | B     |

The number depends on high or low tone. The larger the number, the higher the tone. When the number is same, the frequency (tone) is getting higher and higher from C to \_B.

Beats are the time delay for each note. The larger the number, the longer the delay time. A note without a line in the spectrum is a beat, with a delay of 1000 milliseconds. while a beat with an underline is 1/2 of a beat without a line, and a beat with two underlines is 1/4 of a beat without a line.

![](media/a57464c004160236cb89f0deb31f185d.png)

Here is the notation of Ode to Joy.

![乐谱](media/4a79470cc28f087a3834d168bc0c343f.jpeg)

**Components**

1.  Insert micro:bit board into slot of V2 shield..

2.  Place batteries into battery holder.

3.  Plug smart car in power.

4.  Link micro:bit board with computer via USB cable.

5.  Open the offline version of Mu


**Test Code：**

Open“microbit-Passive Buzzer.py“ file in Mu software

| File Type   | Route                               | File Name                  |
|-------------|-------------------------------------|----------------------------|
| Python file | ../Python code/6.13：Passive Buzzer | microbit-Passive Buzzer.py |

You can also input code in the editing window yourself.(Note:all English words and symbols must be written in English)

```python
from microbit import *
import music

tune = ["E5:4", "E5:4", "F5:4", "G5:4", "G5:4", "F5:4", "E5:4", "D5:4",
        "C5:4", "C5:4", "D5:4", "E5:4", "E5:4", "D5:4", "D5:4", "E5:4",
        "E5:4", "F5:4", "G5:4", "G5:4", "F5:4", "E5:4", "D5:4", "C5:4",
        "C5:4", "D5:4", "E5:4", "D5:4", "C5:2", "C5:4", "D5:4", "D5:4",
        "E5:4", "C5:4", "D5:4", "E5:2", "F5:2", "E5:4", "C5:4", "D5:4",
        "E5:2", "F5:2", "E5:4", "D5:4", "C5:4", "D5:4", "G4:4", "E5:4",
        "E5:4", "E5:4", "F5:4", "G5:4", "G5:4", "F5:4", "E5:4", "D5:4",
        "C5:4", "C5:4", "D5:4", "E5:4", "D5:4", "C5:2", "C5:4", "D5:4",
        "D5:4", "E5:4", "C5:4", "D5:4", "E5:2", "F5:2", "E5:4", "C5:4",
        "D5:4", "E5:2", "F5:2", "E5:4", "D5:4", "C5:4", "D5:4", "G4:4",
        "E5:4", "E5:4", "E5:4", "F5:4", "G5:4", "G5:4", "F5:4", "E5:4",
        "C5:4", "C5:4", "C5:4", "D5:4", "E5:4", "D5:4", "C5:2", "C5:4",
        "D5:4", "C5:2", "C5:4", "G5:4", "F5:4", "E5:2", "E5:4", "C5:4",
        "B5:4", "A5:2", "A5:4", "F5:2", "D5:2", "C5:2", "B4:2", "D5:2",
        "B4:2", "A4:2", "G4:2", "A4:2", "B4:2", "C5:2", "E5:2", "D5:2",
        "B4:2", "C5:4", "C5:2", "C5:1", "C5:4"]

while True:
    music.play(tune)

```

Click “Check” to examine error in the code. The program proves wrong if underlines and cursors are shown.

![](media/7e952f0b78ed1ed8babe6118b16a26ad.png)

If the code is correct, connect micro:bit to computer and click“Flash”to download code to micro:bit board.

![](media/d76cf404b38b3deba07f87d4803cb468.png)

**Test Result：**

Download code onto micro:bit board, and turn on the switch on robot car; “Ode to joy”song will be played in loop way.

**Code Explanation：**

| **from** microbit **import** \*                              | import the library file of micro:bit                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| **import** music                                             | import music files containing <br />the control of sound     |
| tune = [ "E5:4"， "E5:4"， "F5:4"， "G5:4"， "G5:4"， "F5:4"， <br />"E5:4", "D5:4"， "C5:4"， "C5:4"， "D5:4"， "E5:4"， "E5:4"， <br />"D5:4", "D5:4"， "E5:4"， "E5:4"， "F5:4"， "G5:4"， "G5:4"， <br />"F5:4", "E5:4"， "D5:4"， "C5:4"， "C5:4"， "D5:4"， "E5:4"， <br />"D5:4", "C5:2"， "C5:4"， "D5:4"， "D5:4"， "E5:4"， "C5:4"， <br />"D5:4", "E5:2"， "F5:2"， "E5:4"， "C5:4"， "D5:4"， "E5:2"， <br />"F5:2", "E5:4"， "D5:4"， "C5:4"， "D5:4"， "G4:4"， "E5:4"， <br />"E5:4", "E5:4"， "F5:4"， "G5:4"， "G5:4"， "F5:4"， "E5:4"， <br />"D5:4", "C5:4"， "C5:4"， "D5:4"， "E5:4"， "D5:4"， "C5:2"， <br />"C5:4", "D5:4"， "D5:4"， "E5:4"， "C5:4"， "D5:4"， "E5:2"， <br />"F5:2", "E5:4"， "C5:4"， "D5:4"， "E5:2"， "F5:2"， "E5:4"， <br />"D5:4", "C5:4"， "D5:4"， "G4:4"， "E5:4"， "E5:4"， "E5:4"， <br />"F5:4", "G5:4"， "G5:4"， "F5:4"， "E5:4"， "C5:4"， "C5:4"， <br />"C5:4", "D5:4"， "E5:4"， "D5:4"， "C5:2"， "C5:4"， "D5:4"， <br />"C5:2", "C5:4"， "G5:4"， "F5:4"， "E5:2"， "E5:4"， "C5:4"， <br />"B5:4", "A5:2"， "A5:4"， "F5:2"， "D5:2"， "C5:2"， "B4:2"， <br />"D5:2", "B4:2"， "A4:2"， "G4:2"， "A4:2"， "B4:2"， "C5:2"， <br />"E5:2", "D5:2"， "B4:2"， "C5:4"， "C5:2"， "C5:1"， "C5:4" ] | Create variable tune                                         |
| **while True:**                                              | This is a permanent loop that makes <br />micro:bit execute the code of it. |
| music.play(tune)                                             | Call the function play() to save the notes in variable tune  |

**References：**

music.play()：used to play music and MicroPython has abundant **music melody.** More info, please the below link:

<https://microbit-micropython.readthedocs.io/en/latest/tutorials/music.html>

### 14: RGB Experiments

![](media/eb371068cdb58006e9e422beb919bc1c.png)

**Description：**

The RGB color mode is a color standard in the industry. It obtains various colors by changing the three color channels of red (R), green (G), and blue (B) and integrating them. RGB denotes the three colors of red, green and blue. The monitors mostly adopt the RGB color standard, and all the colors on the computer screen are composed of the three colors of red, green and blue mixed in different proportions. A group of red, green and blue is the smallest display unit. Any color on the screen can be recorded and expressed by a set of RGB values.

Each of the three color channels of red, green, and blue is divided into 256 levels of brightness. At 0, the "light" is the weakest-it is turned off, and at 255, the "light" is the brightest. When the three-color gray values are the same, the gray tones with different gray values are produced, that is, when the three-color gray is 0, the darkest black is generated; when the three-color gray is 255, it is the brightest white tone .

![image-20230510153552559](media/image-20230510153552559.png)

RGB colors are called additive colors since the adding of R, G, and B together (that is, all light reflect back to the eye) produces white color. Additive colors are used for lighting, television and computer displays. For example,
displays produce color by emitting red, green, and blue rays. Most visible spectra can be expressed as a mixture of red, green and blue (RGB) light in different proportions and intensities. If these colors overlap, they produce cyan, magenta and yellow.

We will make two experiments, one is that two RGB LEDs light up red, green, blue, indigo, dark red, yellow and white color, another one is that RGB lights display color in gradient way.

**Components:**

Insert micro:bit board into slot of V2 shield.

Put batteries into battery holder

Turn on the switch at the back of micro:bit car

Link micro:bit board with computer via USB cable.

Open the offline version of Mu

**Test Code：**

**Code 1**

**RGB shows seven colors in loop way.**

Open“Code 1.py”file in Mu

| File Type   | Route                                | File Name          |
|-------------|--------------------------------------|--------------------|
| Python file | ../Python code/6.14：RGB Experiments | microbit-Code 1.py |

You can also input code in the editing window yourself.(Note:all English words and symbols must be written in English)

```python
from microbit import *
from keyes_Bit_Car_Driver import *

bitCar = Bit_Car_Driver()

while True:
    bitCar.headlights(255, 0, 0)
    sleep(1000)
    bitCar.headlights(0, 255, 0)
    sleep(1000)
    bitCar.headlights(0, 0, 255)
    sleep(1000)
    bitCar.headlights(0, 255, 255)
    sleep(1000)
    bitCar.headlights(255, 0, 255)
    sleep(1000)
    bitCar.headlights(255, 255, 0)
    sleep(1000)
    bitCar.headlights(255, 255, 255)
    sleep(1000)

```

**Import“keyes_Bit_Car_Driver.py“ File**

**Don’t click“Flash”immediately,** you need to firstly import “keyes_Bit_Car_Driver.py”file which includes the control method of micro:bit smart robot car, making Python code control robot car easily.

Files are mostly stored in the mu_code directory in your home directory. Mu’s default directory is“Mu_code”.

Refer to the link: <https://codewith.mu/en/tutorials/1.0/files>

![](media/d271a92404720dbd8cf7c858732b7767.png)

| File type    | Path                       | File name               |
|--------------|----------------------------|-------------------------|
| Python file  | .. /Python Code/ Libraries | keyes_Bit_Car_Driver.py |

Therefore, copy“keyes_Bit_Car_Driver.py“ to“mu_code”folder, as shown below:

![](media/1242fab07beb60b3d148021c4f399001.png)

Open Mu, connect micro:bit to computer, click“Files”and drag“keyes_Bit_Car_Driver.py”library file to micro:bit.

![](media/b1d9bcd05ccb6ef47f15d1f644402c39.png)

You could view it in the left column, after importing “keyes_Bit_Car_Driver”file

![](media/6e7f654ce0afc4a2e33f5b90c299acc1.png)

Tap“Check”button to confirm if the code has errors. The program proves wrong if there are underlines and cursors

![](media/f9583467210931641a54cc8d853e9f3e.png)

Besides, the prompt signs will appear. The prompt is a warning sign which doesn’t indicate wrong code.

![](media/b27eb6846ce642e80170ac3b8a26b2c5.png)

![](media/67ff667a61837491f09e864d2ca39957.png)

If the code is correct, connect micro:bit to computer and click“Flash”to download code to micro:bit board

![](media/8928a7e1287c915aa5cc7ef692083254.png)

Click“Flash”and appear errors, you need to confirm if you import “keyes_Bit_Car_Driver.py”library.

Note: You need to import“keyes_Bit_Car_Driver.py”file to micro:bit.

If you program with different micro:bit, the library file“keyes_Bit_Car_Driver.py”needs to be imported again to a new micro:bit

**Code 2：**

Display different colors

Open file“microbit- Code 2.py“ in Mu

| File Type   | Route                                | File Name           |
|-------------|--------------------------------------|---------------------|
| Python file | ../Python code/6.14：RGB Experiments | microbit- Code 2.py |

You can also input code in the editing window yourself.(note:all English words and symbols must be written in English)

```python
from microbit import *
from keyes_Bit_Car_Driver import *
bitCar = Bit_Car_Driver()
ledr = 0
ledg = 0
ledb = 0
while True:
    for index in range(51):
        bitCar.headlights(ledr, 0, 0)
        sleep(100)
        ledr += 5
    for index in range(51):
        bitCar.headlights(ledr, 0, 0)
        sleep(100)
        ledr += -5
    for index in range(51):
        bitCar.headlights(0, ledg, 0)
        sleep(100)
        ledg += 5
    for index in range(51):
        bitCar.headlights(0, ledg, 0)
        sleep(100)
        ledg += -5
    for index in range(51):
        bitCar.headlights(0, 0, ledb)
        sleep(100)
        ledb += 5
    for index in range(51):
        bitCar.headlights(0, 0, ledb)
        sleep(100)
        ledb += -5

```

Click “Files” to import “keyes_Bit_Car_Driver.py” library file to micro:bit. If micro:bit has library inside, you don’t need add one.

![](media/3ac083a25299831c6c7876d39c11e156.png)

Click “Check” to examine error in the code. The program proves wrong if underlines and cursors are shown.

![](media/69ef68f5ece6be744fee7969a8207245.png)

If the code is correct, connect micro:bit to computer and click“Flash”to download code to micro:bit board

![](media/a4da5e1f5e141669d4cdf558171b006e.png)

**Test Result：**

Download code 1 to micro:bit board and turn on the switch at the back of micro:bit car, 2 RGB lights of smart car emit red, green, blue, indigo, dark red, yellow and white color cyclically.

Download code 2 to micro:bit board and turn on the switch at the back of micro:bit car, 2 RGB lights show different color in loop way.

**Code Explanation：**

| **from** microbit **import** \*                              | import the library file of micro:bit                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| **from** keyes_Bit_Car_Driver  **import \***                 | Import the library file of keyes_Bit_Car_Driver              |
| bitCar = Bit_Car_Driver()                                    | instantiate                                                  |
| **while True:**                                              | This is a permanent loop that makes micro:bit execute the code of it. |
| bitCar.headlights(255, 0, 0) <br />sleep(1000) <br />bitCar.headlights(0, 255, 0) <br />sleep(1000) <br />bitCar.headlights(0, 0, 255) <br />sleep(1000) <br />bitCar.headlights(0, 255, 255) <br />sleep(1000) <br />bitCar.headlights(255, 0, 255) <br />sleep(1000) <br />bitCar.headlights(255, 255, 0) <br />sleep(1000) <br />bitCar.headlights(255, 255, 255) <br />sleep(1000) | 2 RGB LEDs light up red color <br />Delay 1000ms <br />2 RGB LEDs light up green color <br />Delay in 1000ms <br />2 RGB LEDs light up blue color <br />Delay in1000ms <br />2 RGB light up indigo color <br />Delay in1000ms <br />2 RGB LEDs light up dark red color <br />Delay in1000ms <br />2 RGB LEDs light up yellow color <br />Delay in1000ms <br />2 RGB LEDs light up white color <br />Delay in1000ms |
| ledr = 0                                                     | Set the initial value of ledr to 0                           |
| ledg = 0                                                     | Set the initial value of ledg to 0                           |
| ledb = 0                                                     | Set the initial value of ledb to 0                           |
| **for** index **in** range(51):                              | Repeat 51 times                                              |
| bitCar.headlights(ledr, 0, 0)                                | Set RGB lights of car: R：led-r G：0 B：0                    |
| bitCar.headlights(0, ledg, 0)                                | Set RGB lights of car: R：0 G：ledg B：0                     |
| bitCar.headlights(0, 0, ledb)                                | Set 2 RGB lights R：0 G: 0 B：ledb                           |
| ledr += 5 <br />ledr += -5 <br />ledg += 5 <br />ledg += -5 <br />ledb += 5 <br />ledb += -5 | Change the value of led-r by 5 <br />Change the value of led-r by -5 <br />Change the value of ledg by 5 <br />Change the value of ledg by -5 <br />Change the value of ledb by 5 <br />Change the value of ledb by -5 |

### 15: KEYES-2812-18R Module

![20](media/75a3a53f6230d6adc83af7caca154c03.png)

**1.Description：**

The KEYES-2812-18R module is fully compatible with micro:bit, in this lesson, we make it display different colors through P5 end(D5 of shield) on micro:bit board.

Alter tone of color to get different color:

|                                                        | Name   | RGB（R,G,B）  | Code （16） |                                                 | Name   | RGB（R,G,B）  | Code （16） |
| ------------------------------------------------------ | ------ | ------------- | ----------- | ----------------------------------------------- | ------ | ------------- | ----------- |
| ![IMG_256](media/8eb18c098e9fb43de8e4bc1d6bcbb998.png) | Red    | 255, 0, 0     | \#FF0000    | ![](media/2c9dbcc2e147f462b526807733b44e95.png) | Orange | 255, 165, 0   | \#FFA500    |
| ![](media/02cfaa9a127b2757c4d3b9a76db06fb2.png)        | Yellow | 255, 255, 0   | \#FFFF00    | ![](media/aaa72d51ab690ac5d161bb4dedcbd706.png) | Green  | 0, 255, 0     | \#00FF00    |
| ![](media/f41ff194fdcac9bc5163f19bd64be1b0.png)        | Blue   | 0, 255, 0     | \#0000FF    | ![](media/a3cdf397029f4625fffbb34c65d6e1c7.png) | indigo | 75, 0, 130    | \#4B0082    |
| ![](media/e7ceadb386175c67dea8f22bc891fdea.png)        | violet | 238, 130, 238 | \#EE82EE    | ![](media/fb86ba2b7c59633c285d0cd2fc7d31c0.png) | purple | 160, 32, 240  | \#A020F0    |
| ![](media/9383aa73e392f24384c7fecaf9b58cd4.png)        | Black  | 0, 0, 0       | \#000000    | ![](media/648da100dfbc3c36e9e8e08a36ebeada.png) | white  | 255, 255, 255 | \#FFFFFF    |
| ......                                                 | ...... | .......       | ......      | ......                                          | ...... | ......        | ......      |

**2. Components**

(1) Insert micro:bit board into slot of V2 shield.

(2) Put batteries into battery holder

(3) Turn on the switch at the back of micro:bit car

(4) Link micro:bit board with computer via USB cable.

(5) Open the offline version of Mu

**3. Test Code：**

**Code 1：**

Open“microbit-Code 1.py”file in Mu

| File Type   | Route                                      |
|-------------|--------------------------------------------|
| Python file | ../Python code/6.15：KEYES-2812-18R module |

You can also input code in the editing window yourself.(note:all English words and symbols must be written in English)

```python
from microbit import *
import neopixel

np = neopixel.NeoPixel(pin5, 18)

while True:
    for pixel_id1 in range(0, len(np)):
        np[pixel_id1] = (255, 0, 0)
        np.show()
    sleep(1000)
    for pixel_id2 in range(0, len(np)):
        np[pixel_id2] = (255, 165, 0)
        np.show()
    sleep(1000)
    for pixel_id3 in range(0, len(np)):
        np[pixel_id3] = (255, 255, 0)
        np.show()
    sleep(1000)
    for pixel_id4 in range(0, len(np)):
        np[pixel_id4] = (0, 255, 0)
        np.show()
    sleep(1000)
    for pixel_id5 in range(0, len(np)):
        np[pixel_id5] = (0, 0, 255)
        np.show()
    sleep(1000)
    for pixel_id6 in range(0, len(np)):
        np[pixel_id6] = (75, 0, 130)
        np.show()
    sleep(1000)
    for pixel_id7 in range(0, len(np)):
        np[pixel_id7] = (238, 130, 238)
        np.show()
    sleep(1000)
    for pixel_id8 in range(0, len(np)):
        np[pixel_id8] = (160, 32, 240)
        np.show()
    sleep(1000)
    for pixel_id9 in range(0, len(np)):
        np[pixel_id9] = (255, 255, 255)
    sleep(1000)

```

Click“Check”to examine error in the code. The program proves wrong if underlines and cursors are shown.

![](media/171ea579f3ee1931cb2311ad5dd0a0bb.png)

![](media/9688d8dfe8e72516da83d2ad0a72c7cc.png)

If the code is correct, connect micro:bit to computer and click“Flash”to download code to micro:bit board

![](media/1396301411cb73012a4908fbe763d1ea.png)

![](media/9688d8dfe8e72516da83d2ad0a72c7cc.png)

**Code 2：**

Open“microbit-Code 2.py”file in Mu

| File Type   | Route                                       |
|-------------|---------------------------------------------|
| Python file | ../Python code/6.15：KEYES-2812-18R module/ |

You can also input code in the editing window yourself.(note:all English words and symbols must be written in English)

```python
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

```

Click “Check” to examine error in the code. The program proves wrong if underlines and cursors are shown. 

![](media/24a6a3749f5b0c61ffc9971e753048b9.png)

If the code is correct, connect micro:bit to computer and click“Flash”to download code to micro:bit board.

![](media/ab74f45f245f10f1b5a847ff4bd32fbc.png)

**Code 3：**

Open“microbit-Code 3.py”file in Mu

| File Type   | Route                                       |
|-------------|---------------------------------------------|
| Python file | ../Python code/6.15：KEYES-2812-18R module/ |

You can also input code in the editing window yourself.(note:all English words and symbols must be written in English)

```python
from microbit import *
import neopixel
np = neopixel.NeoPixel(pin5, 18)
while True:
    for index in range(0, 18):
        np.clear()
        np[index] = (255, 0, 0)
        np.show()
        sleep(100)
    for index1 in range(0, 18):
        np.clear()
        np[index1] = (255, 165, 0)
        np.show()
        sleep(100)
    for index2 in range(0, 18):
        np.clear()
        np[index2] = (255, 255, 0)
        np.show()
        sleep(100)
    for index3 in range(0, 18):
        np.clear()
        np[index3] = (0, 255, 0)
        np.show()
        sleep(100)
    for index4 in range(0, 18):
        np.clear()
        np[index4] = (0, 0, 255)
        np.show()
        sleep(100)
    for index5 in range(0, 18):
        np.clear()
        np[index5] = (75, 0, 130)
        np.show()
        sleep(100)
    for index6 in range(0, 18):
        np.clear()
        np[index6] = (238, 130, 238)
        np.show()
        sleep(100)
    for index7 in range(0, 18):
        np.clear()
        np[index7] = (160, 32, 240)
        np.show()
        sleep(100)
    for index8 in range(0, 18):
        np.clear()
        np[index8] = (255, 255, 255)
        np.show()
        sleep(100)

```

Click “Check” to examine error in the code. The program proves wrong if underlines and cursors are shown.

![](media/08030943883aed47fbef211c03b4e89f.png)

![](media/d327029b49407544133f030683469e95.png)

If the code is correct, connect micro:bit to computer and click“Flash”to download code to micro:bit board

![](media/467a6a72746bbca016ea5fdf4a844e1b.png)

![](media/d327029b49407544133f030683469e95.png)

**Code 4：**

Open“microbit-Code 4.py” file

| File Type   | Route                                       |
|-------------|---------------------------------------------|
| Python file | ../Python code/6.15：KEYES-2812-18R module/ |

You can also input code in the editing window yourself.(note:all English words and symbols must be written in English)

```python
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


```

Click “Check” to examine error in the code. The program proves wrong if underlines and cursors are shown.

![](media/52ffd9c59aa8d200ac121be740256643.png)

If the code is correct, connect micro:bit to computer and click“Flash”to download code to micro:bit board.

![](media/f96240fa751a3b57bd53e1fb860a4cd5.png)

**4.Test Result：**

Download code 1 to micro:bit, turn on the switch on robot car and every RGB on KEYES-2812-18R module displays same color.

Download code 2 to micro:bit, turn on the switch on robot car, 18 pcs RGB on KEYES-2812-18R light up and go off one by one.

Download code 3 to micro:bit, turn on the switch on robot car, every RGB light on KEYES-2812-18R shows the same color and turns off one by one.

Download code 4 to micro:bit, turn on switch on robot car. Every RGB light on KEYES-2812-18R lights up random color and goes off one by one.

**5.Code Explanation：**

| **from** microbit **import** \*                              | import the library file of micro:bit                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| **import** neopixel                                          | Import the library file of neopixel                          |
| np = neopixel.NeoPixel(pin5, 18)                             | Initialize Neopixel  set Neopixel to initialize P5 with 18 LEDs |
| np.clear()                                                   | Turn off RGB on Neopixel strip                               |
| **while True:**                                              | This is a permanent loop that makes micro:bit execute the code of it. |
| **for** pixel_id1 **in** range(0, len(np)):                  | Set RGB to pixel_id1 in the range of （0，len（np））        |
| **for** index **in** range(0, 18):                           | Set the pixel of RGB to index in the range of（0，18）       |
| np.show()                                                    | Show the current pixel on Neopixel strip                     |
| np[pixel_id1] = (255, 0, 0) <br />np[pixel_id2] = (255, 165, 0) <br />np[pixel_id3] = (255, 255, 0) <br />np[pixel_id4] = (0, 255, 0) <br />np[pixel_id5] = (0, 0, 255) <br />np[pixel_id6] = (75, 0, 130) <br />np[pixel_id7] = (238, 130, 238) <br />np[pixel_id8] = (160, 32, 240) <br />np[pixel_id9] = (255, 255, 255) | Set pixel_id1 to display red color <br />Set pixel_id2 to display orange color <br />Set pixel_id3 to display yellow color <br />Set pixel_id4 to display green color <br />Set pixel_id5 to display blue color <br />Set pixel_id6 to display indigo color <br />Set pixel_id7 to display violet color <br />Set pixel_id8 to display purple color <br />Set pixel_id9 to display white color |
| **from** random **import** randint                           | Import randint from random variables                         |
| flag = 1                                                     | Set the initial value of flag to 1                           |
| red = 255 <br />green = 0 <br />blue = 0                     | Set the initial value of variable red to 255 <br />Set the initial value of variable green to 0 <br />Set the initial value of variable blue to 0 |
| **while** flag == 1:                                         | When flag=1                                                  |
| red = red - 35 <br />green = green + 35 <br />blue = blue + 35 | Variable red reduces 35 gradually <br />Variable green adds 35 gradually <br />Variable blue adds 35 gradually |
| **if** red \<= 0: <br />red = 0 <br />**if** green \>= 255: <br />green = 255 <br />**if** blue \>= 255: <br />blue = 255 | If variable red≤0 <br />Variable red=0 <br />If Variable green≥255 <br />Variable green=255 <br />If Variable blue≥255 <br />Variable blue=255 |
| np[pixel_id] = (red, green, blue)                            | Set pixel_id to flash colorful light on Neopixel strip       |
| **for** pixel_close **in** range(0, len(np)):                | Pixel of RGB is pixel_close in the range of（0，len（np））  |
| np[pixel_close] = (0, 0, 0)                                  | Set RGB on Neopixel strip to light off                       |
| R = 0 <br />G = 0 <br />B = 0                                | Set the initial value of R to 0 <br />Set the initial value of G to 0 <br />Set the initial value of B to 0 |
| R = randint(10, 255) <br />G = randint(10, 255) <br />B = randint(10, 255) | Set R=randint(10, 255) <br />Set G=randint(10, 255) <br />Set B=randint(10, 255) |

### 16: Photoresistor

![IMG_256](media/d886f14ac931f651ba7977c396fcb785.png)

**Description：**

The photocell sensor (photoresistor) is a resistor made by the photoelectric effect of a semiconductor. It is very sensitive to ambient light, thus its resistance value vary with different light intensity.

We use its features to design a circuit and generate a photoresistor sensor module. The signal end of the module is connected to the analog port of the microcontroller. When the light intensity increases, the resistance decreases, and the voltage of the analog port rises, that is, the analog value of the microcontroller also goes up. Otherwise, when the light intensity decreases, the resistance increases, and the voltage of the analog port declines. That is, the analog value of the microcontroller becomes smaller. Therefore, we can use the photoresistor sensor module to read the corresponding analog value and sense the light intensity in the environment.

It is commonly applied to light measurement, control and conversion, light control circuit as well.

The smart robot car comes with photoresistor. In the experiment, we control 18 RGB lights by photoresistor. The darker the ambient environment, the lighter the RGB.

**Components:**

(1) Insert micro:bit board into slot of V2 shield.

(2) Put batteries into battery holder

(3) Turn on the switch at the back of micro:bit car

(4) Link micro:bit board with computer using USB cable.

(5) Open the offline version of Mu

**Test Code：**

**Code 1：**

Detect light intensity through photoresistor

Open“microbit-Code 1.py“ in Mu

| File Type   | Route                                | File Name          |
|-------------|--------------------------------------|--------------------|
| Python file | ../Python code/6.16：Photoresistor / | microbit-Code 1.py |

You can also input code in the editing window yourself.(note:all English words and symbols must be written in English)

```python
from microbit import *

while True:
    val = pin1.read_analog()
    print("analog signal:", val)
    sleep(100)

```

Click“Check”to examine error in the code. The program proves wrong if underlines and cursors are shown.

![](media/5f7caf718a0cd0f757e072e3d6bc896c.png)

If the code is correct, connect micro:bit to computer and click“Flash”to download code to micro:bit board

![](media/d41d29e1e7c71af37a418a04b11369e9.png)

Download code 1 to micro:bit and plug micro:bit into power. Click**“REPL” button and press reset button on micro:bit board.** BBC microbit REPL shows the intensity value. The value varies with the external light intensity. The weaker the light intensity is, the smaller the value is. As shown below:

![IMG_256](media/7f624ae56921aacdc63bdf1a463d10ee.png)

**Code 2：**

Open“microbit-Code 2.py”file in Mu

| File Type   | Route                              | File Name          |
|-------------|------------------------------------|--------------------|
| Python file | ../Python code/6.16：Photoresistor | microbit-Code 2.py |

You can also input code in the editing window yourself.(note:all English words and symbols must be written in English)

```python
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

```

Click“Check”to examine error in the code. The program proves wrong if underlines and cursors are shown.

![](media/1b78f4244af3f046414db8d56d7d2a98.png)

If the code is correct, connect micro:bit to computer and click“Flash”to download code to micro:bit board

![](media/4d78508e369bfdb9bb95e1fe8dfcc27f.png)

**Test Result：**

Download code2 to micro:bit, turn on the switch on robot car, then KEYES-2812-18R module shows white color. The weaker the light intensity is, the brighter the KEYES-2812-18R gets.

**Code Explanation：**

| **from** microbit **import** \*                     | import the library file of micro:bit                                       |
|-----------------------------------------------------|----------------------------------------------------------------------------|
| **import** neopixel                                 | Import the library file of neopixel                                        |
| np = neopixel.NeoPixel(pin5, 18)                    | Initialize Neopixel                                                        |
| np.clear()                                          | RGB goes off                                                               |
| **while True:**                                     | This is a permanent loop that makes micro:bit execute the code of it.      |
| val1 = pin1.read_analog()                           | Set the light intensity value of photoresistor of P1 to val                |
| val2 = int((val1/1023)\*255)                        | Set int((val1/1023)\*255) to val2                                          |
| **for** pixel_id **in** range(0, len(np)):          | Set the pixel of RGB to pixel_id in the range of（0，len（np））           |
| np[pixel_id] = (255 - val2, 255 - val2, 255 - val2) | Set the color of pixel_id to RGB（red 255-val green 255-val blue 255-val） |
| np.show()                                           | Display the current pixel_id on Neopixel strip                             |
| sleep(100)                                          | Delay in 100ms                                                             |

**Reference：**

read_analog() : read the voltage of pin, and more details please refer to[https://microbit-micropython.readthedocs.io/en/latest/pin.html](https://microbit-micropython.readthedocs.io/en/latest/pin.html%20)

### 17: Motor Driving

![](media/596de7f13f36eaf067afacc3a842a0da.png)

**Description：**

Keyestudio Micro：bit robot car is equipped with two DC geared motors.

DC geared motor is integration of reducer and motor, which is widely applied to steel and machinery industry.

The shield of smart car is inclusive of PCA9685PW and TB6612FNG chip.

In order to save the resources of IO ports, we control the rotation speed and direction by TB6612FNG chip.

**Components**

1.  Insert micro:bit board into slot of V2 shield.

2.  Put batteries into battery holder

3.  Turn on the switch at the back of micro:bit car

4.  Link micro:bit board with computer via USB cable.

5.  Open the offline version of Mu


**Test Code：**

**Code 1：**

**CarRun**

Open“microbit-Code 1.py” file in Mu

| File Type   | Route                              | File Name          |
|-------------|------------------------------------|--------------------|
| Python file | ../Python code/6.17：Motor Driving | microbit-Code 1.py |

You can also input code in the editing window yourself.(note:all English words and symbols must be written in English)

```python
from microbit import *
from keyes_Bit_Car_Driver import *
bitCar = Bit_Car_Driver()
while True:
    display.show(Image.ARROW_S)
    bitCar.motorL(1, 200)
    bitCar.motorR(1, 200)
    sleep(1000)
    display.show(Image.ARROW_N)
    bitCar.motorL(0, 200)
    bitCar.motorR(0, 200)
    sleep(1000)
    display.show(Image.ARROW_E)
    bitCar.motorL(1, 50)
    bitCar.motorR(1, 200)
    sleep(1000)
    display.show(Image.ARROW_W)
    bitCar.motorL(1, 200)
    bitCar.motorR(1, 50)
    sleep(1000)
    display.show(Image.ARROW_E)
    bitCar.motorL(0, 200)
    bitCar.motorR(1, 200)
    sleep(1000)
    display.show(Image.ARROW_W)
    bitCar.motorL(1, 200)
    bitCar.motorR(0, 200)
    sleep(1000)
    display.show(Image("00900:""09990:""99999:""99999:""09090"))
    bitCar.motorL(0, 0)
    bitCar.motorR(0, 0)
    sleep(1000)

```

Click“Files”to import the library file of“keyes_Bit_Car_Driver.py”to micro:bit

If micro:bit has library, you don’t need to add one.

![](media/e8acb87abb40b228757a54868d1cbb03.png)

Click“Check”to examine error in the code. The program proves wrong if underlines and cursors are shown.

![](media/e89024c91a3f26c49dde6d7c60fc724d.png)

If the code is correct, connect micro:bit to computer and click“Flash”to download code to micro:bit board.

![](media/b74f50f69a9bd8e820b006584616bc75.png)

**Code 2：**

Open“microbit-Code 2.py”file in Mu

| File Type   | Route                              | File Name                   |
|-------------|------------------------------------|-----------------------------|
| Python file | ../Python code/6.17: Motor Driving | microbit-Motor Driving-2.py |

You can also input code in the editing window yourself.(note:all English words and symbols must be written in English)

**Note: Download code 2 to micro:bit, and turn on the switch of micro:bit.(Note: the control pin of right obstacle avoidance sensor and B button are P11. To prevent the obstacle avoidance sensor from interfering button B, we could screw the potentiometer RP9 clockwise to turn off the right obstacle sensor.**

```python
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

```

Click“Files”to import the library of“keyes_Bit_Car_Driver.py“ to micro:bit.

![](media/299e4e408046c09ec3d40900d6e9ba57.png)

![](media/70dc0c648e58f279a7c6b9bd120118be.png)

![](media/5439ed551ab9df747b9e44b5bc5f5004.png)

Click“Check”to examine error in the code. The program will be wrong if underlines and cursors are shown.

![](media/3610771a03e5fd21317b01e46fa7ccfa.png)

![](media/70dc0c648e58f279a7c6b9bd120118be.png)

![](media/5439ed551ab9df747b9e44b5bc5f5004.png)

If the code is correct, connect micro:bit to computer and click“Flash”to download code to micro:bit board

![](media/69c314f5eccc967e3f998326d929cf9f.png)

![](media/70dc0c648e58f279a7c6b9bd120118be.png)

![](media/5439ed551ab9df747b9e44b5bc5f5004.png)

**Test Result：**

Download code 1 to micro:bit, and turn on the switch on robot car. The robot car will go forward for 1s, back for 1s, turn left for 1s, right for 1s, turn anticlockwise for 1s, clockwise for 1 and stop 1s. Matrix also displays the patterns.

**Note: Download code 2 to micro:bit, and turn on the switch of micro:bit. (Note: the control pin of right obstacle avoidance sensor and B button are P11. To prevent the obstacle avoidance sensor from interfering button B, we could screw the potentiometer RP9 clockwise to turn off the right obstacle sensor.**

When the button A and B are firstly pressed, micro:bit will show“L”, the route of car is“L”. When they are pressed again,“口”is shown on micro:bit, and route of car is“口”.

**Code Explanation：**

| **from** microbit **import** \*                              | import the library file of micro:bit                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| **from** keyes_Bit_Car_Driver  **import \***                 | Import the library of keyes_Bit_Car_Driver                   |
| bitCar = Bit_Car_Driver()                                    | Set Bit_Car_Driver() to bitCar                               |
| **while True:**                                              | This is permanant loop, and make micro:bit excute the code.  |
| display.show(Image.ARROW_S) <br />display.show(Image.ARROW_N) <br />display.show(Image.ARROW_E) <br />display.show(Image.ARROW_W) <br />display.show(Image("00900:""09990:""99999:""99999:""09090")) | micro:bit shows arrow pointing to South <br />micro:bit shows arrow pointing to North <br />micro:bit shows arrow pointing to East <br />micro:bit shows arrow pointing to West <br />micro:bit displays“❤” |
| bitCar.motorL(1, 200) <br /><br />bitCar.motorR(1, 200)      | The left motor of car rotates clockwise at the speed of PWM200 <br />1: clockwise，0: anticlockwise；<br />PWM100 means speed（0\~255） <br />The right motor of car rotates clockwise at the speed of PWM200 |
| bitCar.motorL(0, 200) <br />bitCar.motorR(0, 200)            | The left motor of car rotates anticlockwise at the speed of PWM200 <br />The right motor of car rotates anticlockwise at the speed of PWM200 |
| sleep(1000)                                                  | Delay in 1000ms                                              |
| a = 0 <br />b = 0                                            | Set the initial value of a to 0 <br />Set the initial value of b to 0 |
| **def** run_L(): **def** run_O():                            | Define subroutine run_L()                                    |
| show_L = Image("90000:""90000:""90000:""90000:""99999")      | Set show_L=Image()                                           |
| **if** button_a.was_pressed(): <br />a = a + 1 <br />**if** a \>= 3: <br />a = 0 <br />**if** button_b.was_pressed(): <br />b = 1 <br />**if** (a == 1): <br />display.show(show_L) <br />**if** b == 1: <br />run_L() <br />**elif** a == 2: <br />display.show(show_O) <br />**if** b == 1: <br />run_O() | If button A is pressed, <br />a = a + 1 <br />If a≥3 <br />a=0 <br />If button B is pressed, <br />b=1 <br />If a=1 <br />micro:bit shows“L”pattern <br />If b=1 <br />The track of car is route L  <br />If a=2 <br />micro:bit shows “O” image <br />If b=1 <br />The track of car is route O |

### 18: Line Tracking Car

6.18.1: Line Tracking Sensor

![](media/81a769b41214847d61628921b85d74ab.png)

**Description：**

The V2 expansion board of Keyestudio Micro:bit mini smart robot car comes with two line tracking elements which adopt TCRT5000 IR tubes.

TCRT5000 IR tube has an IR emitting tube and a receiving tube.

Low level(0) is output when IR transmitting tube emits IR signals to receiving tube; high level(1) will be output when smart car runs along black line.

**Components:**

(1) Insert micro:bit board into slot of V2 shield.

(2) Put batteries into battery holder

(3) Turn on the switch at the back of micro:bit car

(4) Link micro:bit board with computer via USB cable.

(5) Open the offline version of Mu

**Test Code：**

**Code 1：**

Open the file“Code 1.py”in Mu

| File Type   | Route                                         | File Name |
|-------------|-----------------------------------------------|-----------|
| Python file | ../Python code/6.18：Line tracking car/6.18.1 | Code 1.py |

You can also input code in the editing window yourself.(Note:all English words and symbols must be written in English)

```python
from microbit import *
val_RR = 0
while True:
    val_RR = pin12.read_digital()
    print("digital signal:", val_RR)
    sleep(200)

```

Click“Check”to examine error in the code. The program proves wrong if underlines and cursors are shown. 

![](media/28c1b15a9817aefc3c4507fa900586b5.png)

If the code is correct, connect micro:bit to computer and click“Flash”to download code to micro:bit board.

![](media/dbe7aa7faf39bd4c544f682d15b1be3e.png)

Download code 1 onto micro:bit board, don’t plug off USB cable. Click“REPL”and press the reset buttons, the readings detected by right line tracking sensor are displayed on monitor.

When the right line tracking sensor detects white object, 0 will be shown and D6 will be on; when no white objects and only black object are detected, 1 will be displayed and D6 will be off, as shown below.

![IMG_256](media/6edb098a643366affa12f153ab4242ef.png)

**Code 2：**

Open file“Code 2.py in Mu

| File Type   | Route                                          | File Name           |
|-------------|------------------------------------------------|---------------------|
| Python file | ../Python code/ 6.18：Line tracking car/6.18.2 | microbit-Code 2 .py |

You can also input code in the editing window yourself.(note:all English words and symbols must be written in English)

```python
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

```

Click“Check”to examine error in the code. The program proves wrong if underlines and cursors are shown.

![](media/94e8aaac9df2a27dec6fbc67649f7e91.png)

If the code is correct, connect micro:bit to computer and click“Flash”to download code to micro:bit board.

![](media/429a0a564d3e198bf192fc15f0c4d463.png)

**Test Result：**

Download code 2 to micro:bit, turn on the switch on robot car. When white object is detected by left sensor, micro bit shows“I”pattern at its left and D2 is on.

When only right sensor detects the white object, micro bit shows“I”pattern at its right and D6 is on.

If both of line tracking sensors detect black object or no object is detected, “![](media/aaa1b518e463aef56f86c35ab6f0d1df.png)”will be shown on micro:bit.

If both detect white object,“❤”will be shown and D2 and D6 will be on.

**Code Explanation：**

| **from** microbit **import** \*                              | import the library file of micro:bit                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| val_RR = 0                                                   | Set the initial value of val_RR to 0                         |
| val_LL = 0                                                   | Set the initial value of val_LL to 0                         |
| **while True:**                                              | This is a permanent loop that makes micro:bit execute the code of it. |
| val_RR = pin12.read_digital()                                | Set the digital signal read by tracking sensor connected to pin12, to val_RR |
| val_LL = pin13.read_digital()                                | Set the digital signal read by tracking sensor connected to pin13, to val_LL |
| print("Light intensity:", Lightintensity)                    | BBC microbit REPL prints the digital signals read by line tracking sensor |
| sleep(100)                                                   | Delay in 100ms                                               |
| **if** val_LL == 0 **and** val_RR == 1: <br />display.show(Image("00009:""00009:""00009:""00009:""00009")) <br />**elif** val_LL == 1 **and** val_RR == 0: <br />display.show(Image("90000:""90000:""90000:""90000:""90000")) <br />**elif** val_LL == 1 **and** val_RR == 1: <br />display.show(Image.HEART_SMALL) <br />**else:** <br />display.show(Image.HEART) | When val_LL = 0 and val_RR = 1 <br />micro:bit shows“1”on the left <br />When val_LL = 1 and val_RR = 0 <br />micro:bit shows “1”on the right <br />When val_LL =1 and val_RR = 1<br />micro:bit displays“![](media/aaa1b518e463aef56f86c35ab6f0d1df.png)”. <br />If the above conditions are not met<br />micro:bit displays“❤”. |

6.18.2: Line Tracking Car

![功能图1](media/793e7e798d3b66314dcef86823b0ae33.jpeg)

**1. Description：**

In this lesson we will combine line tacking sensors with motor to make a line tracking smart car.

The micro:bit board will analyze the signals and control smart car to show line tracking function.

If two line tracking sensors detect black line, the smart car will go forward；if only left sensor detects black line, robot car will turn left; if only right sensor detects black line，smart car will turn right；if black line is not detected, car will stop.

![](media/a16a844427530b0bb8b40e74e08bdf4e.png)

**2. What you need to get started**

1.  Insert micro:bit board into slot of V2 shield.

2.  Put batteries into battery holder

3.  Turn on the switch at the back of micro:bit car

4.  Link micro:bit board with computer via USB cable.

5.  Open the offline version of Mu

| Left/Right line tracking sensor（Level） | Line tracking Smart Car |            |
|------------------------------------------|-------------------------|------------|
| Low（0）                                 | High（1）               | Turn right |
| High（1）                                | Low（0）                | Go back    |
| High（1）                                | High（1）               | Go forward |
| Low（0）                                 | Low（0）                | Stop       |

**3. Flow Chart**

![](media/401323665b7bd44b7160e7953eee09f2.png)

**4. Test Code：**

Open“microbit- Line Tracking Car.py“ in Mu：

| File Type   | Route                                         | File Name                      |
|-------------|-----------------------------------------------|--------------------------------|
| Python file | ../Python Code/6.18：Line tracking car/6.18.2 | microbit- Line Tracking Car.py |

You can also input code in the editing window yourself.(note: all English words and symbols must be written in English)

```python
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

```

Click“Files”to import the library file of“keyes_Bit_Car_Driver.py to micro:bit If micro:bit has library, you don’t need to add one.

![IMG_256](media/ffc1f41c78651205396e8d616ab89fb1.png)

Click“Check”to examine error in the code. The program proves wrong if underlines and cursors are shown.

![](media/35c79e21327aaa8c69b101bd65f5c728.png)

If the code is correct, connect micro:bit to computer and click“Flash”to download code to micro:bit board

![](media/6661a7edf800a3e93a9bb59e4e222e7c.png)

**5. Test Result：**

Download code to micro:bit and turn on the switch at the back of micro:bit car.
The car can follow black traces and KEYES-2812-18R module lights up.

**Note: (1) the width of black trace should be wider than the distance between two line tracking sensors.**

**Avoid to test smart car under the strong light.**

**6. Code Explanation：**

| **from** keyes_Bit_Car_Driver  **import \***                                                                                                                                                                                                                                                          | Import the library file of keyes_Bit_Car_Driver                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **import** neopixel                                                                                                                                                                                                                                                                                   | Import the library file of neopixel                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| bitCar = Bit_Car_Driver()                                                                                                                                                                                                                                                                             | Set Bit_Car_Driver() to bitCar                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| np = neopixel.NeoPixel(pin5, 18)                                                                                                                                                                                                                                                                      | Initialize Neopixel                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| display.show(Image.HAPPY)                                                                                                                                                                                                                                                                             | micro:bit shows the smile pattern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **while True:**                                                                                                                                                                                                                                                                                       | This is a permanent loop that makes micro:bit execute the code of it.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| val_RR = pin12.read_digital()                                                                                                                                                                                                                                                                         | Set the digital signal read by line tracking sensor connected to P12, to val_RR                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| val_LL = pin13.read_digital()                                                                                                                                                                                                                                                                         | Set the digital signal read by line tracking sensor connected P13, to val_LL                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **for** pixel_id1 in range(0, len(np)): np[pixel_id1] = (255, 100, 100) np.show()                                                                                                                                                                                                                     | Set the pixel of RGB to pixel_id1 in the range of （0，len（np））  Set the pixel of RGB on Neopixel strip to pixel_id1 on (255, 100, 100)  Display pixel on Neopixel strip                                                                                                                                                                                                                                                                                                                                                                                                      |
| **if** val_LL == 0 **and** val_RR == 1:  bitCar.motorL(1, 80) bitCar.motorR(0, 30) **elif** val_LL == 1 and val_RR == 0:  bitCar.motorL(0, 30) bitCar.motorR(1, 80) **elif** val_LL == 1 and val_RR == 1: bitCar.motorL(1, 60) bitCar.motorR(1, 60) **else:** bitCar.motorL(0, 0) bitCar.motorR(0, 0) | If val_LL = 0 and val_RR = 1 Left motor rotates clockwise at thes peed of PWM 80（1: clockwise，0: anticlockwise；speed: PWM 80（0\~255）） Right motor rotates anticlockwise at the speed of PWM 30 When val_LL =1 and val_RR = 0 Left motor rotates anticlockwise at the speed of PWM 30 Right motor rotates clockwise at the speed of PWM 80 When val_LL = 1 and val_RR = 1 Left motor rotates clockwise at the speed of PWM 60 Right motor rotates clockwise at the speed of PWM 60 If the above conditions are not met Left motor doesn’t rotate Right motor doesn’t rotate |

### 19: Ultrasonic Follow Smart Car

6.19.1: Ultrasonic Ranging

![5](media/7d1365ccda9dfeff4ba6624f9413877c.png)

**1. Description：**

The HC-SR04 ultrasonic sensor uses sonar to determine distance to an object like bats do. It offers excellent non-contact range detection with high accuracy and stable readings in an easy-to-use package. It comes complete with ultrasonic transmitter and receiver modules.

The HC-SR04 or the ultrasonic sensor is being used in a wide range of electronics projects for creating obstacle detection and distance measuring application as well as various other applications.

As the above picture shown, it is like two eyes. One is transmitting end, the other is receiving end.

The ultrasonic module will emit the ultrasonic waves after trigger signal. When the ultrasonic waves encounter the object and are reflected back, the module outputs an echo signal, so it can determine the distance of object from the time difference between trigger signal and echo signal.

**2. Working principle ：**

![](media/8ff02741199a0f03d8d814a4b72f27d7.png)

1.  Pull down TRIG then trigger high level signals with least 10us.

2.  After triggering, the module will automatically send eight 40KHz ultrasonic pulses and detect whether there is a signal return.
    
3.  The propagation speed of sound in the air is about 343m/s, therefore, distance = speed \* time, because the ultrasonic wave emits and comes back, which is 2 times of distance, so it needs to be divided by 2, the distance measured by ultrasonic wave = (speed \* time)/2

**3. Specification：**

-   Working voltage：3-5.5V（DC）

-   Power Supply :+5V DC

-   Working Current: 15mA

-   Working frequency: 40khz

-   Maximum Ranging Distance : around 3m

-   Minimum Ranging Distance: 2-3cm

-   Resolution : 0.3 cm

-   Measuring Angle: ≤15 degree

-   Trigger Input Pulse width: 10uS

-   Accuracy: up to 0.2cm

-   Output echo signal : output TTL level signal(high), which is proportion to range.

**4. Components**

1.  Insert micro:bit board into slot of V2 shield.

2.  Put batteries into battery holder

3.  Turn on the switch at the back of micro:bit car

4.  Link micro:bit board with computer via USB cable.

5.  Open the offline version of Mu


**5. Test Code：**

Open “6.19.1- Ultrasonic Ranging.py”file in Mu software

| File Type   | Route                                            | File Name                     |
|-------------|--------------------------------------------------|-------------------------------|
| Python file | ../Python code/6.19：Ultrasonic Follow Smart car | 6.19.1- Ultrasonic Ranging.py |

You can also input code in the editing window yourself.(note:all English words and symbols must be written in English)

```python
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
```

Click “Files” to import the library file of“keyes_Bit_Car_Driver.py to micro:bit. If micro:bit has library, you don’t need to add one.

![](media/b0ab34e8a787318e04641b92766def61.png)

Click “Check” to examine error in the code. The program proves wrong if underlines and cursors are shown.

![](media/781e95ec55c64513142b23b313835957.png)

**Make sure code correct, connect micro:bit to computer via USB cable, turn on the switch of keyestudio Micro:bit robot car and click“Flash”to download code to micro:bit.**

![](media/a6d00cf3ccd9fe6a4a3207a310174571.png)

**6. Test Result：**

After downloading code, keep USB cable connected, click**“REPL”button and press the reset button.** REPL window shows the distance value between the ultrasonic sensor and the obstacle(as shown below), when the distance between obstacle and ultrasonic sensor is less than 10cm, the passive buzzer emits sound.

![IMG_256](media/95be52a8f0408d765391bdfa6040808c.png)

**7. Code Explanation：**

| **from** microbit **import \***                              | import the library file of microbit                          |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| **from** keyes_Bit_Car_Driver **import \***                  | import the library file of keyes_Bit_Car_Driver              |
| bitCar = Bit_Car_Driver()                                    | instantiate                                                  |
| **import** music                                             | import the library file of music                             |
| tune = ["C4:4"]                                              | Create variable tune to save notes                           |
| **while True:**                                              | This is a permanent loop that makes micro:bit execute the code of it. |
| i = 0                                                        | Set variable i=0                                             |
| distance = bitCar.get_distance()                             | Set bitCar.get_distance() to distance                        |
| print("distance:", distance)                                 | BBC microbit REPL window shows the distance value <br />between the ultrasonic sensor and the obstacle |
| **if** distance \< 10:                                       | **if** distance \< 10                                        |
| **while** i \< 1:                                            | When i＜1                                                    |
| music.play(tune) sleep(200) <br />music.play(tune) sleep(200) | Passive buzzer emits “tick,tick”                             |
| i += 1                                                       | Variable i plus 1                                            |

6.19.2: Ultrasonic Follow Smart Car

![跟随](media/fd2f5e910e2ea77331bc82142fd08659.jpeg)

**1. Description：**

In previous lesson, we’ve learned the basic principle of line tracking sensor. Next, we will combine ultrasonic sensor with car shield to make an ultrasonic follow car.

**2. Components:**

1.  Insert micro:bit board into slot of V2 shield.

2.  Put batteries into battery holder

3.  Dial POWER switch to ON end on shield.

4.  Link micro:bit board with computer via USB cable.

5.  Open the offline version of Mu

**3. Flow Chart:**

![makecode-超声波跟随小车](media/f6fcf149f81ad386e0f9bdbe69b5ba52.png)

**4.Test Code：**

Open“6.19.2-Ultrasonic Follow Smart Car.py”file in Mu

| File Type   | Route                                         | File Name                             |
|-------------|-----------------------------------------------|---------------------------------------|
| Python file | ../Python code/6.19：Ultrasonic following car | 6.19.2-Ultrasonic Follow Smart Car.py |

You can also input code in the editing window yourself.(note:all English words and symbols must be written in English)

```python
from keyes_Bit_Car_Driver import *
import neopixel
np = neopixel.NeoPixel(pin5, 18)
from random import randint
bitCar = Bit_Car_Driver()
while True:
    distance = 0
    distance = bitCar.get_distance()
    if distance >= 10 and distance <= 30:
        bitCar.motorL(1, 100)
        bitCar.motorR(1, 100)
        for pixel_id1 in range(0, len(np)):
            np[pixel_id1] = (255, 0, 0)
            np.show()
    if distance <= 6:
        bitCar.motorL(0, 100)
        bitCar.motorR(0, 100)
        for pixel_id1 in range(0, len(np)):
            np[pixel_id1] = (255, 255, 0)
            np.show()
    if distance > 6 and distance < 10 or distance > 30:
        bitCar.motorL(0, 0)
        bitCar.motorR(0, 0)
        for pixel_id1 in range(0, len(np)):
            np[pixel_id1] = (255, 255, 255)
            np.show()

```

Click“Files”to import the library file of“keyes_Bit_Car_Driver.py”to micro:bit. If micro:bit has library, you don’t need to add one.

![](media/a2291a65c524acf8111415dd8fb6ceb8.png)

Click“Check”to examine error in the code. The program proves wrong if underlines and cursors are shown.

![](media/4ba20b2b89d7c062cffb01347de23b26.png)

**Make sure code correct, connect micro:bit to computer via USB cable, turn on the switch of keyestudio Micro:bit robot car and click“Flash”to download code to micro:bit board.**

![](media/d8f549b429857e2e5fa778271d865a12.png)

**5.Test Result：**

After downloading code, turn on the switch of robot car, as a result, the car will follow the obstacle to move and KEYES-2812-18R module will display different colors.

**6.Code Explanation：**

| **from** keyes_Bit_Car_Driver **import \***                  | Import the library file of keyes_Bit_Car_Driver              |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| bitCar = Bit_Car_Driver()                                    | instantiate                                                  |
| **import** neopixel                                          | Import the library file of neopixel                          |
| np = neopixel.NeoPixel(pin5, 18)                             | Initialize Neopixel                                          |
| **from** random **import** randint                           | Import randint from random variables                         |
| **while True:**                                              | This is a permanent loop that makes micro:bit execute the code of it. |
| distance = 0                                                 | Set the initial value of distance to 0                       |
| distance = bitCar.get_distance()                             | Set distance = bitCar.get_distance()                         |
| **if** distance \>= 10 **and** distance \<= 30: <br />bitCar.motorL(1, 100) <br />bitCar.motorR(1, 100) <br />**for** pixel_id1 **in** range(0, len(np)): <br />np[pixel_id1] = (255, 0, 0) <br />np.show() <br />**if** distance \<= 6: <br />bitCar.motorL(0, 100) <br />bitCar.motorR(0, 100) <br />**for** pixel_id1 **in** range(0, len(np)): <br />np[pixel_id1] = (255, 255, 0) <br />np.show() <br />**if** distance \> 6 **and** distance \< 10 **or** distance \> 30: <br />bitCar.motorL(0, 0) <br />bitCar.motorR(0, 0) <br />**for** pixel_id1 **in** range(0, len(np)): <br />np[pixel_id1] = (255, 255, 255) <br />np.show() | If distance ≥10 and distance ≤ 30 <br />Left motor rotates clockwise at the speed of PWM100 <br />Right motor rotates clockwise at the speed of PWM100 <br />RGB pixel is pixel_id1 in the range of （0，len（np）） <br />Set pixel_id1 to light up red color <br />Display pixel on Neopixel strip <br />If distance ≤6 <br />Left motor rotates anticlockwise at the speed of PWM100 <br />Right motor rotates anticlockwise at the speed of PWM100 <br />RGB pixel is pixel_id1 in the range of （0，len（np）） <br />Set pixel_id1to light up yellow color <br />Display pixel on Neopixel strip <br />If distance＞6, distance＜10 or distance＞30 <br />left motor doesn’t rotate right motor doesn’t rotate <br />RGB pixel is pixel_id1 in the range of （0，len（np）） <br />Set pixel_id1 to light up white color <br />Display pixel on Neopixel strip |

### 20: Obstacle Avoidance and Follow Smart Car

6.20.1: Obstacle Avoidance Function

![](media/cdd665626233e3f8e9db635fd8fd093d.png)

**Description：**

The shield of smart car comes with two IR obstacle avoidance sensors which adopt transmitting tube and receiving tube.

The IR rays will reflect back to receiving tube if there is an obstacle. Next, sensor will determine the obstacle and send test result to microcontroller.

After a series of processing analysis, the smart car will avoid the obstacle.

The low level (0) will be output when the obstacle is detected, otherwise, the high level(1) will be output

IR obstacle avoidance sensor is generally applied to obstacle avoiding, line tracking, anti-falling, counter and production line cutting and liquid level detection, etc

**Components:**

1.  Insert micro:bit board into slot of V2 shield.

2.  Put batteries into battery holder

3.  Turn on the switch at the back of micro:bit car

4.  Link micro:bit board with computer via USB cable.

5.  Open the offline version of Mu

**Test Code：**

**Code 1：**

Open file“Code 1.py“ in Mu

| File Type   | Route                                                           | File Name |
|-------------|-----------------------------------------------------------------|-----------|
| Python file | ../Python code/6.20：Obstacle Avoidance&Follow Smart Car/6.20.1 | Code 1.py |

You can also input code in the editing window yourself.(note:all English words and symbols must be written in English)

```python
from microbit import *
from keyes_Bit_Car_Driver import *
bitCar = Bit_Car_Driver()
val_LL = 0
while True:
    bitCar.headlights(0, 0, 0)
    val_LL = pin2.is_touched()
    print("digital signal:", val_LL)
    sleep(200)

```

Click“Files”to import the library file of“keyes_Bit_Car_Driver.py to micro:bit. If micro:bit has library, you don’t need to add one.

![](media/fbf54693c3b0f8a08fe307d60272a084.png)

Click“Check”to examine error in the code. The program proves wrong if underlines and cursors are shown. 

![](media/a383e5fdebecc8834bb9e492bedb1bc7.png)

If the code is correct, connect micro:bit to computer and click“Flash”to download code to micro:bit board

![](media/082fe84eda129591becc608916f2cb0f.png)

After downloading code, keep USB cable connected, click**“REPL”button and press the reset button.**

BBC microbit REPL window prints“True”and“False”.

Signal end will output“True”when the obstacle is detected, and SIG1 indicator will light up; otherwise, the signal end will output“False”and SIG1 indicator will go off.

(official website:<https://microbit-micropython.readthedocs.io/en/v1.0.1/pin.html> the micro:bit has external weak (10M) pull-ups fitted on pins 0, 1 and 2 only，in order for the touch sensing to work. Return True if the pin is being
touched with a finger, otherwise return False）

![](media/b9488318f79cf14a4d43aae69c225a95.png)

![IMG_256](media/c7d4d87cf4e248e6f0a87571ae34f1a2.png)

**Code 2：**

Open“Code 2.py” in Mu

| File Type   | Route                                                           | File Name |
|-------------|-----------------------------------------------------------------|-----------|
| Python file | ../Python code/6.20：Obstacle Avoidance&Follow Smart Car/6.20.1 | Code 2.py |

You can also input code in the editing window yourself.(note:all English words and symbols must be written in English)

```python
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

```

Click“Check”to examine error in the code. The program proves wrong if underlines and cursors are shown.

![](media/6e96b3c83435efc51c18dc4d31789015.png)

If the code is correct, connect micro:bit to computer and click“Flash”to download code to micro:bit board.

![](media/68364ad55dbd2f5879be13b16b41a7f6.png)

**Test Result：**

Download code 2 to micro:bit, plug in power using USB cable and turn on the switch of robot car.

(1) When both obstacle avoidance sensors detect the obstacle, micro:bit show will smile face.

(2) When only left obstacle avoidance sensor detects the obstacle, micro:bit will display the leftward arrow.

(3) When only right obstacle avoidance sensor detects the obstacle, micro:bit will display the rightward arrow.

(4) When neither of them detects the obstacle, micro:bit will display the upward arrow.

**Code Explanation：**

| **from** microbit **import \***                              | Import the library file of micro;bit                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| **from** keyes_Bit_Car_Driver **import \***                  | Import the library file of keyes_Bit_Car_Driver              |
| bitCar = Bit_Car_Driver()                                    | instantiate                                                  |
| val_LL = 0                                                   | Set the initial value of val_LL to 0                         |
| val_RR = 0                                                   | Set the initial value of val_RR to 0                         |
| **while True:**                                              | This is a permanent loop that makes micro:bit execute the code of it. |
| bitCar.headlights(0, 0, 0)                                   | Turn off 2 pcs RGB lights                                    |
| val_LL = pin2.is_touched()                                   | Set the value of P2 read by pin2.is_touched() command , to val_LL |
| val_RR = pin11.read_digital()                                | Set the digital signal read by P11 to val_RR                 |
| print("digital signal:", val_LL)                             | BBC microbit REPL prints the signals read by IR obstacle avoidance sensor |
| sleep(200)                                                   | Delay in 200ms                                               |
| **if** val_LL is True **and** val_RR == 0: <br />display.show(Image.HAPPY) <br />**elif** val_LL is True **and** val_RR == 1: <br />display.show(Image("00900:""00090:""99999:""00090:""00900") <br />**elif** val_LL is False **and** val_RR == 0: <br />display.show(Image("00900:""09000:""99999:""09000:""00900")) <br />**else**: <br />display.show(Image("00900:""09990:""90909:""00900:""00900")) | If val_LL is True and val_RR == 0; <br />micro:bit displays the smile pattern, <br />If val_LL is True **and** val_RR == 1 micro:bit <br />displays“←”pattern <br />If val_LL is False and val_RR == 0; <br />micro:bit shows“→”pattern <br />If the above conditions are not met <br />micro:bit displays“↑”pattern |

6.20.2: Obstacle Avoidance Smart Car

![1(3)](media/50bb9fec75b30364412930f055365e9d.jpeg)

**Description：**

We’ve learned the knowledge of obstacle avoidance sensor. In this project, we will integrate ultrasonic sensor, IR obstacle avoidance sensor and car expansion board to make an obstacle avoidance smart car.

Its principle is to detect the distance between the car and obstacle by ultrasonic sensor and IR obstacle avoidance sensors and control the motion of smart car.

Left obstacle avoidance sensor is controlled by P2 and right one is decided by P11

**Components:**

1.  Insert micro:bit board into slot of V2 shield.

2.  Put batteries into battery holder

3.  Turn on the switch at the back of micro:bit car

4.  Link micro:bit board with computer via USB cable.

5.  Open the offline version of Mu

Warning: the obstacle avoidance sensor can't work normally under strong light which contains a mountain of invisible light including IR and ultraviolet rays.

**Flow Chart**

![makecode-避障小车(1)](media/1dfe33af8eb002ec9246a529161aec88.png)

**Test Code：**

Open“6.20.2.py”in Mu software

| File Type   | Route                                                       | File Name |
|-------------|-------------------------------------------------------------|-----------|
| Python file | ../Python code/6.20：Obstacle avoidance&following robot car | 6.20.2.py |

You can also input code in the editing window yourself.(note:all English words and symbols must be written in English)

```python
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
    if val_L is True and val_R == 0:
        bitCar.motorL(0, 100)
        bitCar.motorR(0, 100)
        for pixel_id1 in range(0, len(np)):
            np[pixel_id1] = (250, 0, 0)
            np.show()
        sleep(1000)
        bitCar.motorL(0, 80)
        bitCar.motorR(1, 80)
        sleep(200)
    elif val_L is False and val_R == 0:
        bitCar.motorL(0, 80)
        bitCar.motorR(1, 80)
        for pixel_id1 in range(0, len(np)):
            np[pixel_id1] = (160, 32, 240)
            np.show()
    elif val_L is True and val_R == 1:
        bitCar.motorL(1, 80)
        bitCar.motorR(0, 80)
        for pixel_id1 in range(0, len(np)):
            np[pixel_id1] = (255, 255, 0)
            np.show()
    elif distance <= 10 and val_L is False and val_R == 1:
        bitCar.motorL(1, 80)
        bitCar.motorR(0, 80)
        for pixel_id1 in range(0, len(np)):
            np[pixel_id1] = (0, 0, 255)
            np.show()
    elif distance > 10 and val_L is False and val_R == 1:
        bitCar.motorL(1, 100)
        bitCar.motorR(1, 100)
        for pixel_id1 in range(0, len(np)):
            np[pixel_id1] = (0, 255, 0)
            np.show()
```

Click“Files”to import the library file of“keyes_Bit_Car_Driver.py”to micro:bit. If micro:bit has library, you don’t need to add one.

![](media/3bab71858747275c2eb93fa102368e5c.png)

![](media/3f117da0b89bd23901b0f670ab95c1de.png)

Click “Check” to examine error in the code. The program proves wrong if underlines and cursors are shown.

![](media/5dace015755353b4387957fe10c6a81c.png)

![](media/3f117da0b89bd23901b0f670ab95c1de.png)

After downloading code, keep USB cable connected, turn on the switch of robot car. And tap“Flash”to download code to micro:bit board.

![](media/9a60f611ccd53af93737cab722c7a0fe.png)

![](media/3f117da0b89bd23901b0f670ab95c1de.png)

**Test Result：**

After downloading code, turn on the switch of robot car. As a result, the car will avoid the obstacle automatically

**Code Explanation：**

| **from** keyes_Bit_Car_Driver **import \***                  | Import the library file of keyes_Bit_Car_Driver              |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| bitCar = Bit_Car_Driver()                                    | instantiate                                                  |
| **import** neopixel                                          | Import the library file of neopixel                          |
| np = neopixel.NeoPixel(pin5, 18)                             | Initialize Neopixel                                          |
| distance = 0                                                 | Set the initial value of distance to 0                       |
| val_L = 0                                                    | Set the initial value of val_L to 0                          |
| val_R = 0                                                    | Set the initial value of val_R to 0                          |
| **while True:**                                              | This is a permanent loop that makes micro:bit execute the code of it. |
| distance = bitCar.get_distance()                             | Set bitCar.get_distance() to variable distance               |
| val_L = pin2.is_touched()                                    | Set the value of P2 read by pin2.is_touched() command, to val_LL |
| val_R = pin11.read_digital()                                 | Set the digital signal read by P11 to val_RR                 |
| **if** val_L is True **and** val_R == 0: <br />bitCar.motorL(0, 100) <br />bitCar.motorR(0, 100) <br />**for** pixel_id1 **in** range(0, len(np)): <br />np[pixel_id1] = (250, 0, 0) <br />np.show() <br />sleep(1000) <br />bitCar.motorL(0, 80) <br />bitCar.motorR(1, 80) <br />sleep(200) <br />**elif** val_L is False **and** val_R == 0: <br />bitCar.motorL(0, 80) <br />bitCar.motorR(1, 80) <br />**for** pixel_id1 **in** range(0, len(np)): <br />np[pixel_id1] = (160, 32, 240) <br />np.show() <br />**elif** val_L is True **and** val_R == 1: <br />bitCar.motorL(1, 80) <br />bitCar.motorR(0, 80) <br />**for** pixel_id1 **in** range(0, len(np)): <br />np[pixel_id1] = (255, 255, 0) <br />np.show() <br />**elif** distance \<= 10 **and** val_L is False **and** val_R == 1: <br />bitCar.motorL(1, 80) <br />bitCar.motorR(0, 80) <br />**for** pixel_id1 **in** range(0, len(np)): <br />np[pixel_id1] = (0, 0, 255) <br />np.show() <br />**elif** distance \> 10 **and** val_L is False **and** val_R == 1: <br />bitCar.motorL(1, 100) <br />bitCar.motorR(1, 100) **for** pixel_id1 **in** range(0, len(np)): <br />np[pixel_id1] = (0, 255, 0) <br />np.show() | If val_L is True and val_R = 0 <br />The left motor rotates clockwise at the speed of PWM100  <br />The right motor rotates clockwise at the speed of PWM100 <br />Set pixel of RGB to pixel_id1 <br />Set pixel_id1 to show red color <br />Set pixel on Neopixel strip <br />Delay in 1000ms <br />The left motor rotates anticlockwise at the speed of PWM80  <br />The right motor rotates clockwise at the speed of PWM80 <br />Delay in 200ms <br />If val_L is False and val_R =0 <br />The left motor rotates anticlockwise at the speed of PWM80  <br />The right motor rotates clockwise at the speed of PWM80 <br />Set pixel of RGB to pixel_id1 <br />Set pixel_id1 to display purple color <br />Set pixel on Neopixel strip <br />If val_L is True and val_R = 1 <br />The left motor rotates clockwise at the speed of PWM80   <br />The right motor rotates anticlockwise at the speed of PWM80 <br />Set pixel of RGB to pixel_id1 <br />Set pixel_id1 to show yellow color <br />Set pixel on Neopixel strip <br />If distance ≤10 and val_L is False and val_R = 1 <br />The left motor rotates clockwise at the speed of PWM80  <br />The right motor rotates anticlockwise at the speed of PWM80 <br />Set pixel of RGB to pixel_id1 <br />Set pixel_id1 to display blue color <br />Set pixel on Neopixel strip <br />If distance \> 10 and val_L is False and val_R = 1 <br />The left motor rotates clockwise at the speed of PWM100 <br />The right motor rotates anticlockwise at the speed of PWM100 <br />Set pixel of RGB to pixel_id1 <br />Set pixel_id1 to show green color <br />Set pixel on Neopixel strip |

6.20.3: Following Smart Car

![新作跟随2](media/fa31aba3ce37dc5786dedac6cdd16ade.jpeg)

**1.Description：**

In this chapter, we will integrate ultrasonic sensor, IR obstacle avoidance sensor and car expansion board to make a multi-directional follow smart car. Its principle is to detect the distance between the car and obstacle by ultrasonic sensor and IR obstacle avoidance sensors and control the motion of smart car.

**2.Components:**

1.  Insert micro:bit board into slot of V2 shield.

2.  Put batteries into battery holder

3.  Turn on the switch at the back of micro:bit car

4.  Link micro:bit board with computer via USB cable.

5.  Open the offline version of Mu

Warning: the obstacle avoidance sensor can't work normally under strong light full of invisible light like IR and ultraviolet rays.

**3.Flow Chart:**

![makecode-多方向跟随小车(1)](media/50eb6365f838219cddd3a5948cc10995.png)

**4.Test Code：**

Open“6.20.3.py”in Mu

| File Type   | Route                                                       | File Name |
|-------------|-------------------------------------------------------------|-----------|
| Python file | ../Python code/6.20：Obstacle avoidance&following robot car | 6.20.3.py |

You can also input code in the editing window yourself.(note:all English words and symbols must be written in English)

```python
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
```

Click “Files” to import the library file of “keyes_Bit_Car_Driver.py to micro:bit. If micro:bit has library, you don’t need to add one.

![](media/fc02e5d51e9add20530b48768a4dc8c5.png)

![](media/fc7f55391ba6dfe6befe433341f1a1e4.png)

Click “Check” to examine error in the code. The program proves wrong if underlines and cursors are shown.

![](media/406eda5995d61f3ec313f6db2dbf26d4.png)

![](media/fc7f55391ba6dfe6befe433341f1a1e4.png)

**Make sure code correct, connect micro:bit to computer via USB cable, turn on the switch of keyestudio micro:bit robot car and click“Flash”to download code to micro:bit.**

![](media/3a11414a92d5930f83071d211b8ccd5a.png)

![](media/fc7f55391ba6dfe6befe433341f1a1e4.png)

**5.Test Result：**

After downloading code, turn on the switch of robot car, the car will follow the obstacle to move.

**6.Code Explanation：**

| **from** keyes_Bit_Car_Driver **import \***                  | Import the library file of keyes_Bit_Car_Driver              |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| bitCar = Bit_Car_Driver()                                    | instantiate                                                  |
| **import** neopixel                                          | Import the library file of neopixel                          |
| np = neopixel.NeoPixel(pin5, 18)                             | Initialize Neopixel                                          |
| distance = 0                                                 | Set the initial value of distance to 0                       |
| val_L = 0                                                    | Set the initial value of val_L to 0                          |
| val_R = 0                                                    | Set the initial value of val_R to 0                          |
| **while True:**                                              | This is a permanent loop that makes micro:bit execute the code of it. |
| distance = bitCar.get_distance()                             | Set bitCar.get_distance() to distance                        |
| val_L = pin2.is_touched()                                    | Set the value of P2 read by pin2.is_touched()z command, to val_LL |
| val_R = pin11.read_digital()                                 | Set the digital signal read by P11 to val_RR                 |
| **if** distance \> 3 **and** distance \<= 6 **and** val_L is False **and** val_R == 1: <br />bitCar.motorL(0, 0) <br />bitCar.motorR(0, 0) <br />**for** pixel_id1 **in** range(0, len(np)): <br />np[pixel_id1] = (250, 0, 0) <br />np.show() <br />**elif** distance \<= 3 **or** val_L is True **and** val_R == 0: <br />bitCar.motorL(0, 80) <br />bitCar.motorR(0, 80) <br />**for** pixel_id1 **in** range(0, len(np)): <br />np[pixel_id1] = (160, 32, 240) <br />np.show() <br />**elif** distance \> 6 **and** val_L is False **and** val_R == 1: <br />bitCar.motorL(1, 80) <br />bitCar.motorR(1, 80) <br />**for** pixel_id1 **in** range(0, len(np)): <br />np[pixel_id1] = (0, 0, 255)<br />np.show() <br />**elif** val_L is True **and** val_R == 1: <br />bitCar.motorL(0, 80) <br />bitCar.motorR(1, 80) <br />**for** pixel_id1 **in** range(0, len(np)): <br />np[pixel_id1] = (0, 255, 0) <br />np.show() <br />**elif** val_L is False **and** val_R == 0: <br />bitCar.motorL(1, 80) <br />bitCar.motorR(0, 80) <br />**for** pixel_id1 **in** range(0, len(np)): <br />np[pixel_id1] = (255, 255, 0) <br />np.show() <br />**else**: <br />bitCar.motorL(0, 0) <br />bitCar.motorR(0, 0) <br />**for** pixel_id1 **in** range(0, len(np)): <br />np[pixel_id1] = (255, 0, 0) <br />np.show() | If distance \> 3 and distance ≤ 6 val_L is False, val_R =1 <br />left motor doesn’t rotate <br />right motor doesn’t rotate <br />Set the pixel of RGB to pixel_id1 in the range of 0-len（np） <br />Set pixel_id1to show red color <br />Set pixel of RGB to pixel_id1 <br />If distance ≤ 3 or val_L is True and val_R = 0 <br />The left motor rotates anticlockwise at the speed of PWM80 <br />The right motor rotates anticlockwise at the speed of PWM80 <br />Set pixel of RGB to pixel_id1 <br />Set pixel_id1 to display purple color <br />Display pixel on Neopixel strip <br />Otherwise, if distance \> 6 and val_L is False and val_R =1 <br />The left motor rotates clockwise at the speed of PWM80 <br />The right motor rotates clockwise at the speed of PWM80 <br />Set pixel of RGB to pixel_id1 <br />Set pixel_id1to show blue color <br />Display pixel on Neopixel strip <br />If val_L is True and val_R = 1 <br />The left motor rotates anticlockwise at the speed of PWM80 <br />The right motor rotates clockwise at the speed of PWM80 <br />Set pixel of RGB to pixel_id1 <br />Set pixel_id1 to show green color <br />Display pixel on Neopixel strip If val_L is False and val_R = 1 <br />The left motor rotates clockwise at the speed of PWM80 <br />The right motor rotates anticlockwise at the speed of PWM80 <br />Set pixel of RGB to pixel_id1 <br />Set pixel_id1 to display yellow color <br />Display pixel on Neopixel strip <br />If the above conditions are not met <br />left motor doesn’t rotate <br />right motor doesn’t rotate <br />Set pixel of RGB to pixel_id1 <br />Set pixel_id1 to show red color <br />Display pixel on Neopixel strip |

### 21: Multi-purpose Smart Car

With 16k RAM, micro:bit owns a low-consumption Bluetooth module and support Bluetooth communication. However, BLE heap stack occupies 12K RAM, which implies that there is no enough space to run microPython.

At present, microPython doesn’t support Bluetooth, thereby, we can’t make a multi-purpose smart car.

<https://microbit-micropython.readthedocs.io/en/latest/ble.html>

## Resources

BBC Micro：bit Micro Python：

<https://microbit-micropython.readthedocs.io/en/latest/tutorials/introduction.html>

The Micro Python language

[https://docs.openmv.io/reference/index.html -the-micropython-language](https://docs.openmv.io/reference/index.html#the-micropython-language)

<https://docs.openmv.io/reference/index.html>

Ustruct Library：

<https://docs.openmv.io/library/ustruct.html>

Math Library：

<https://docs.openmv.io/library/math.html>

