# FireTracking tracker using OpenCV and Arduino
import time

import cv2
import serial

face_cascade = cv2.CascadeClassifier(r'Data/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(1)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
ArduinoSerial = serial.Serial('com3', 9600, timeout=0.1)
out = cv2.VideoWriter('Data/face detection1.avi', fourcc, 20.0, (640, 480))
time.sleep(0.5)

while cap.isOpened():
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)  # mirror the image
    # frame=cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    # print(frame.shape)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 6)  # detect the FaceByLight
    for x, y, w, h in faces:
        # sending coordinates to Arduino
        string = 'X{0:d}Y{1:d}'.format((x + w // 2), (y + h // 2))
        print(string)
        ArduinoSerial.write(string.encode('utf-8'))
        # plot the center of the FaceByLight
        cv2.circle(frame, (x + w // 2, y + h // 2), 2, (0, 255, 0), 2)
        # plot the roi
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
    # plot the squared region in the center of the screen
    cv2.rectangle(frame, (640 // 2 - 30, 480 // 2 - 30),
                  (640 // 2 + 30, 480 // 2 + 30),
                  (255, 255, 255), 3)
    # Save the frame to the video file
    out.write(frame)

    # out.write(frame)
    cv2.imshow('img', frame)
    # cv2.imwrite('output_img.jpg',frame)
    '''for testing purpose
    read= str(ArduinoSerial.readline(ArduinoSerial.inWaiting()))
    time.sleep(0.05)
    print('data from arduino:'+read)
    '''
    # press q to Quit
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
cap.release()
out.release()

cv2.destroyAllWindows()
