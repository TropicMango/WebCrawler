from pynput import keyboard, mouse
from pynput.keyboard import Key
from pynput.mouse import Button
import time
import math


keyboardC = keyboard.Controller()
mouseC = mouse.Controller()


def test():
    return


def on_release(key):
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
        if key.char == 'Q':
            print(keyboardC.ctrl_pressed)
            print(str(mouseC.position[0]) + ", " + str(mouseC.position[1]))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))
        if key == Key.esc:
            print("kk")
            exit()


# Collect events until released
with keyboard.Listener(on_release=on_release) as listener:
    listener.join()
