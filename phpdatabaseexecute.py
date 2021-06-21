#phpdatabase
db=mysql.connector.connect(
    host="192.168.0.128",
    user="amir",
    password="IntruderAlarmiot",
    database="Alarm_Activity"

)
mycursor = db.cursor()

    #phpexecute
    mycursor.execute ("INSERT INTO History (PI_ACTIVITY) VALUES ('%s')"%(pi_name))
    db.commit()