import cv2
import numpy as np
# import communiction as comm

move = 0
Motor1 = 0
Motor2 = 0


def detect_fire(frame):
    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define lower and upper bounds for the color of flames
    lower_bound = np.array([0, 100, 100])
    upper_bound = np.array([20, 255, 255])

    # Create a binary mask for flame color
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Apply morphological operations to reduce noise
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # Find contours in the binary mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    frame_height, frame_width, channels = frame.shape
    # Check if any contours (potential flames) are found
    if contours:
        # Draw bounding boxes around detected flames
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            xx = (x + x + w) / 2
            yy = (y + y + y) / 2
            move = 0
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
            # thread = threading.Thread(target=comm.sendCommend(move))
            # thread.start()

    return frame


# Open the webcam
cap = cv2.VideoCapture(1)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()
    if not ret:
        break

    # Apply fire detection
    result_frame = detect_fire(frame)

    # Display the original and result frames
    cv2.imshow('Original', frame)
    cv2.imshow('Fire Detection', result_frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()
