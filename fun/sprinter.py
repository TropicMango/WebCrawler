from pynput import keyboard
from pynput.keyboard import Key
from pynput.mouse import Button, Controller
import time

mouse = Controller()
pressed = 0

def on_press(key):
    mouse.click(Button.left, 1)
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
        if key == keyboard.Key.ctrl:
            global pressed
            pressed = 1
    except AttributeError:
        print('special key {0} pressed'.format(
            key))


def on_release(key):
    if key == keyboard.Key.ctrl:
        global pressed
        pressed = 0
    if key == keyboard.Key.cmd:
        # Stop listener
        return False


# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
