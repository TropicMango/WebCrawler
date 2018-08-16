from pynput import keyboard, mouse
from pynput.keyboard import Key

import time

keyboard = keyboard.Controller()
mouse = mouse.Controller()
wait = 0.1

keyboard.press(Key.cmd)
keyboard.press(Key.space)

keyboard.release(Key.cmd)
keyboard.release(Key.space)

time.sleep(wait)
keyboard.type("terminal")
time.sleep(wait)
keyboard.press(Key.enter)
time.sleep(wait)
keyboard.type("cd ~/Desktop/Python\ for\ fun~/fun/")
time.sleep(wait)
keyboard.press(Key.enter)
time.sleep(wait)
keyboard.type("Python MouseTesting.py")
time.sleep(wait)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
