from gpiozero import LED
from gpiozero import MotionSensor
from gpiozero import Buzzer
import time,sys
import RPi.GPIO as GPIO
import serial
import numpy as np
import cv2
from picamera import PiCamera
from email.mime.multipart import MIMEMultipart
from subprocess import call 
import os
from datetime import datetime
import email.mime.application
import datetime
import smtplib
from time import sleep
import mysql.connector


red_led = LED(17)
pir = MotionSensor(21)
buzzer = Buzzer(23)

#phpdatabase
db=mysql.connector.connect(
    host="192.168.0.128",
    user="amir",
    password="IntruderAlarmiot",
    database="Alarm_Activity"

)
mycursor = db.cursor()

#PI_ACTIVITY
pi_name = 'pi_one'

#Email details
from_email_addr = 'IntruderAlarm34'
from_email_password = 'IntruderAlarmiot'
to_email_addr = 'ashrafwzakaria@gmail.com'

#GSM SERIALPORT/BAUDRATE(speed of communication over data channel)/timeout(exception alarm signal received)
SERIAL_PORT = "/dev/ttyS0"
ser = serial.Serial(SERIAL_PORT, baudrate = 9600, timeout=5)


while True:
    #Initiate Alarm
    pir.wait_for_motion()
    print("Motion Detected")
    red_led.on()
    buzzer.on()
    os.system('fswebcam -r 1280x720 -S 3 --jpeg 90 --save /home/pi/Desktop/Run/alert_picture.jpg')    


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
    
    #Initiate SMS
    ser.write("AT+CMGF=1\r".encode())
    time.sleep(2)
    ser.write('AT+CMGS="+60176984760"\r'.encode())
    msg=("HOME ALARM! - Intruder Alert! Check your email for photo.".encode())
    print("Sending SMS ...")
    time.sleep(2)
    ser.write(msg+chr(26).encode())
    time.sleep(2)
    print("SMS sent!")
    
    #phpexecute
    mycursor.execute ("INSERT INTO History (PI_ACTIVITY) VALUES ('%s')"%(pi_name))
    db.commit()

    #STOP Alarm
    pir.wait_for_no_motion()
    print("Motion Stopped")
    red_led.off()
    buzzer.off()

