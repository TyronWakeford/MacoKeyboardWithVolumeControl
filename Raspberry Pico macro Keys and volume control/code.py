import digitalio
import board
import usb_hid
import time
from digitalio import DigitalInOut, Direction
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.mouse import Mouse
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

print("== Pi Pico multifunction knob 1.0 =="), print("---Pico Pad Keyboard---")

led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT
led.value = True

kbd = Keyboard(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)

btn1_pin = board.GP9
btn2_pin = board.GP8
btn3_pin = board.GP7
btn4_pin = board.GP19
btn5_pin = board.GP20
btn6_pin = board.GP21

CLK_PIN = board.GP4
DT_PIN = board.GP3
SW_PIN = board.GP2
clk_last = None
totalMode = 3
currentMode = 2

cc = ConsumerControl(usb_hid.devices)
mouse = Mouse(usb_hid.devices)
keyboard = Keyboard(usb_hid.devices)


clk = digitalio.DigitalInOut(CLK_PIN)
clk.direction = digitalio.Direction.INPUT

dt = digitalio.DigitalInOut(DT_PIN)
dt.direction = digitalio.Direction.INPUT

sw = digitalio.DigitalInOut(SW_PIN)
sw.direction = digitalio.Direction.INPUT
sw.pull = digitalio.Pull.UP

btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN

btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.DOWN

btn4 = digitalio.DigitalInOut(btn4_pin)
btn4.direction = digitalio.Direction.INPUT
btn4.pull = digitalio.Pull.DOWN

btn5 = digitalio.DigitalInOut(btn5_pin)
btn5.direction = digitalio.Direction.INPUT
btn5.pull = digitalio.Pull.DOWN

btn6 = digitalio.DigitalInOut(btn6_pin)
btn6.direction = digitalio.Direction.INPUT
btn6.pull = digitalio.Pull.DOWN

def millis():
    return time.monotonic() * 1000

def ccw():
    print("CCW")

    if(currentMode == 2):   # Volume decrement
        cc.send(ConsumerControlCode.VOLUME_DECREMENT)

def cw():
    print("CW")
    if(currentMode == 2):     # Volume increment
        cc.send(ConsumerControlCode.VOLUME_INCREMENT)

while True:
    clkState = clk.value
    if(clk_last != clkState):
        if(dt.value != clkState):
            cw()
        else:
            ccw()
    if btn1.value:
        keyboard.send(Keycode.CONTROL, Keycode.F7)
        time.sleep(0.1)
    if btn2.value:
        keyboard.send(Keycode.CONTROL, Keycode.F8)
        time.sleep(0.1)
    if btn3.value:
        keyboard.send(Keycode.CONTROL, Keycode.F9)
        time.sleep(0.1)
    if btn4.value:
        keyboard.send(Keycode.CONTROL, Keycode.F10)
        time.sleep(0.1)
    if btn5.value:
        keyboard.send(Keycode.CONTROL, Keycode.F11)
        time.sleep(0.1)
    if btn6.value:
        keyboard.send(Keycode.CONTROL, Keycode.F12)
        time.sleep(0.1)
    clk_last = clkState
