import math

import cv2
import cvzone
from ultralytics import YOLO

# import serial

# Running real time from webcam
cap = cv2.VideoCapture(0)
# ArduinoSerial = serial.Serial('com8', 9600, timeout=0.1)
# out= cv2.VideoWriter('FaceByLight detection4.avi',fourcc,20.0,(640,480))
model = YOLO('Data/FireModel.pt')
print("loaded the model")

# Reading the classes
classnames = ['fire']

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))
    result = model(frame, stream=True)
    lX, lY = -1, -1
    # Getting  ,confidence and class names information to work with
    for info in result:
        faces = info.boxes
        for face in faces:
            confidence = face.conf[0]
            confidence = math.ceil(confidence * 100)
            Class = int(face.cls[0])
            if confidence > 80:
                x, y, w, h = face.xyxy[0]
                xm = (x + w) / 2
                ym = (y + h) / 2
                x, y, w, h = int(x), int(y), int(w), int(h)
                if (lX == -1 and lY == -1) or (xm - 20 < lX < xm + 20) and (ym - 20 < lY < ym + 20):
                    lX = xm
                    lY = ym
                    string = 'X{0:d}Y{1:d}'.format((x + w // 2), (y + h // 2))
                    print("position =", string)
                    # ArduinoSerial.write(string.encode('utf-8'))
                    cv2.rectangle(frame, (x, y), (w, h), (0, 0, 255), 3)
                    cvzone.putTextRect(frame, f'{classnames[Class]} {confidence}%', [x + 8, y + 100],
                                       scale=1.5, thickness=2)
                else:
                    cv2.rectangle(frame, (x, y), (w, h), (47, 254, 0), 2)
                    cvzone.putTextRect(frame, f'{classnames[Class]} {confidence}%', [x + 8, y + 100],
                                       scale=1.5, thickness=2)
    cv2.imshow('fire detection', frame)
    cv2.waitKey(10)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
