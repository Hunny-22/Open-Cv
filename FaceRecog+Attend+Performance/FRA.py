import cv2
import datetime
import time

flag,secs1,secs2=0,0,0
name=input("Enter student name: ")
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
timer1=datetime.timedelta()
timer2=datetime.timedelta()
def convert(secs):
    secs = secs % (24 * 3600)
    hr = secs // 3600
    secs %= 3600
    mins = secs // 60
    secs %= 60
    return datetime.timedelta(hours=int(hr),minutes=int(mins),seconds=int(secs))
frame_rate=1
prev = 0
while True:
    time_elapsed = time.time() - prev
    _, img = cap.read()
    if time_elapsed > 1. / frame_rate:
        prev = time.time()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,1.1,1)
        cv2.imshow('img', img)
        if len(faces)>0:
            if flag==0:
                t = time.localtime()
                st = time.strftime("%H:%M:%S", t)
                flag=1
            timer1=convert(secs1)
            secs1+= 1
            time.sleep(1)
        else:
            timer2=convert(secs2)
            secs2+= 1
            time.sleep(1)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 300, 400), 2)
        cv2.imshow('img', img)
        k = cv2.waitKey(30) & 0xff
        if k==27:
            t1 = time.localtime()
            et = time.strftime("%H:%M:%S", t1)
            break
print("Name:",name)
print("Class started at:",st)
print("Class ended at:",et)
ft=datetime.timedelta()
if(timer2.total_seconds()<30):
    ft=timer1+timer2
else:
    ft=timer1
print("Face detected for:",timer1)
print("Face not detected for:",timer2)

total_time=timer1+timer2
attendance=float((ft.total_seconds()*100)/total_time.total_seconds())
print(attendance,"%")
if(attendance>=75):
    print("Attendance is Marked")
else:
    print("Attendance is not Marked")
cap.release()
