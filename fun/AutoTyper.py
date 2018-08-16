from pynput import keyboard, mouse
from pynput.keyboard import Key

import time

keyboard = keyboard.Controller()
mouseC = mouse.Controller()
wait = 0.1

mouseC.click(mouse.Button.left)

for i in range(100):
    keyboard.type(str(i))

    time.sleep(0.01)
    keyboard.press(Key.enter)

