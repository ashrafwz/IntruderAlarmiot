#GSM SERIALPORT/BAUDRATE(speed of communication over data channel)/timeout(exception alarm signal received)
SERIAL_PORT = "/dev/ttyS0"
ser = serial.Serial(SERIAL_PORT, baudrate = 9600, timeout=5)

 
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