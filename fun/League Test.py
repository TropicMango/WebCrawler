from pynput import keyboard, mouse
from pynput.keyboard import Key
import time
import math


keyboardC = keyboard.Controller()
mouseC = mouse.Controller()


def kick_flash():
    pos = mouseC.position
    # keyboardC.type('q')
    time.sleep(0.5)
    mouseC.position = (640, 390)
    keyboardC.type('s')
    keyboardC.type('r')
    time.sleep(0.05)
    keyboardC.type('r')
    time.sleep(0.1)
    angle = math.atan2(-(pos[1]-390), pos[0]-640) + math.pi/2
    mouseC.move(100*math.sin(angle), 100*math.cos(angle))
    keyboardC.type('f')


def ward_hop():
    pos = mouseC.position
    new_pos = (pos[0]-640, pos[1]-390)
    keyboardC.type('w')
    print(new_pos[0], new_pos[1])
    if (new_pos[0]*new_pos[0])/(314*314)+(new_pos[1]*new_pos[1])/(230*230) < 1:  # up 232, left 303
        keyboardC.type('w')
    else:
        time.sleep(0.05)
        # mouseC.click(Button.right)


def dance():
    pos = mouseC.position
    angle = math.atan2(-(pos[1] - 390), pos[0] - 640) + math.pi/2 + math.pi/4
    mouseC.position = (640, 390)
    mouseC.move(200 * math.sin(angle), 200 * math.cos(angle))
    keyboardC.type('`')
    ward_hop()
    time.sleep(0.5)
    mouseC.position = (640, 390)
    angle = math.atan2(-(pos[1] - 390), pos[0] - 640) + math.pi / 2 - math.pi/4
    mouseC.move(220 * math.sin(angle), 220 * math.cos(angle))
    keyboardC.type('s')
    keyboardC.type('q')
    # ward_hop()
    # mouseC.click(Button.right)


def test():
    pos = mouseC.position
    print(pos[0] - 640, pos[1] - 390)
    angle = math.degrees(math.atan2(pos[1]-390, pos[0]-640))
    print(angle)


def on_release(key):
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
        if key.char == 'Q':
            print(keyboardC.ctrl_pressed)
            kick_flash()
        elif key.char == '`':
            ward_hop()
        elif key.char == 'c':
            dance()
        # elif key.char == 't':
        #     test()
    except AttributeError:
        print('special key {0} pressed'.format(
            key))
        if key == Key.esc:
            print("kk")
            exit()


# Collect events until released
with keyboard.Listener(on_release=on_release) as listener:
    listener.join()
