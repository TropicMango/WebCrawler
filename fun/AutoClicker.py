from pynput import keyboard
from pynput.mouse import Button, Controller
import time

pressed = 1
mouse = Controller()


def on_press(key):
    mouse.click(Button.left, 1)
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))
        global pressed
        pressed = 0


def on_release(key):
    mouse.click(Button.left, 1)
    print('{0} released'.format(
        key))
    global pressed
    pressed = 1
    if key == keyboard.Key.esc:
        # Stop listener
        global pressed
        pressed = 3
        return False


# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

