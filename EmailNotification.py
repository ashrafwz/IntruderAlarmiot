import smtplib
from email.mime.multipart import MIMEMultipart
import email.mime.application

#Email details
from_email_addr = 'IntruderAlarm34'
from_email_password = 'MYPASSWORD'
to_email_addr = 'ashrafwzakaria@gmail.com'

 #Subject & Email sender/receiver
    msg = MIMEMultipart()
    msg[ 'Subject'] = 'INTRUDER ALERT..!! Motion has been DETECTED!'
    msg['From'] = from_email_addr
    msg['To'] = to_email_addr

  # Picture attachment
    Captured = '/home/pi/Desktop/Run/alert_picture.jpg'
    fp=open(Captured,'rb')
    att = email.mime.application.MIMEApplication(fp.read(),_subtype=".jpg")
    fp.close()
    att.add_header('Content-Disposition','attachment',filename='picture' + datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S') + '.jpg')
    msg.attach(att)
    print("attach successful")

 #send Mail
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email_addr, from_email_password)
    server.sendmail(from_email_addr, to_email_addr, msg.as_string())
    server.quit()
    print('Email sent')