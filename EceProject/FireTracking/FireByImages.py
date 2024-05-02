import math

import cv2
import cvzone
from ultralytics import YOLO

# import serial

model = YOLO('Data/FireModel.pt')
print("loaded the model")

limit = 40
# Running real time from webcam
# Load the image
i = 3
lX, lY = -1, -1
BX, XY = -1, -1
while i <= 8:
    image_path = '../Images/fireImages' + str(i) + '.png'  # Specify the path to your image
    frame = cv2.imread(image_path)
    # ArduinoSerial = serial.Serial('com8', 9600, timeout=0.1)
    # out= cv2.VideoWriter('FaceByLight detection4.avi',fourcc,20.0,(640,480))

    # Reading the classes
    classnames = ['fire']
    frame = cv2.resize(frame, (640, 480))
    result = model(frame, stream=True)

    # Getting  ,confidence and class names information to work with
    for info in result:
        faces = info.boxes
        if len(faces) == 0:
            lX, lY = -1, -1
        for face in faces:
            confidence = face.conf[0]
            confidence = math.ceil(confidence * 100)
            Class = int(face.cls[0])
            if confidence > 80:
                x, y, w, h = face.xyxy[0]
                xm = (x + w) / 2
                ym = (y + h) / 2
                x, y, w, h = int(x), int(y), int(w), int(h)
                if (lX == -1 and lY == -1) or (xm - limit < lX < xm + limit) and (ym - limit < lY < ym + limit):
                    lX = int(xm)
                    lY = int(ym)
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
            else:
                break

    cv2.imshow('Fire Detection' + str(i), frame)
    i += 1
    cv2.waitKey(0)
    cv2.destroyAllWindows()
