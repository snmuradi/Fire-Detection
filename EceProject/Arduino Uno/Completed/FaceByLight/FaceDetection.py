import threading
from builtins import print

import cv2

import communiction as comm

cascPath = r"D:\Downloads\haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)
forFirst = True
move = 0
Motor1 = 0
Motor2 = 0

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    frame_height, frame_width, channels = frame.shape
    if forFirst:
        print("Frame : ", frame_height, frame_width)
        forFirst = False
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=1,
        minSize=(40, 40),
        # flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        xx = (x + x + w) / 2
        yy = (y + y + y) / 2
        if yy - frame_height / 2 == 0:
            move += 0
            Motor2 = 0
        elif yy - frame_height / 2 > 0:
            move = 2
            Motor2 = -1
        else:
            move = 4
            Motor2 = 1

        if xx - frame_width / 2 == 0:
            move += 0
            Motor1 = 0
        elif xx - frame_width / 2 > 0:
            move = move * 10 + 1
            Motor1 = -1
        else:
            move = move * 10 + 3
            Motor1 = 1

        print(move, (x + x + w) / 2, (y + y + y) / 2)
        thread = threading.Thread(target=comm.sendCommend(move))
        thread.start()
    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
