# OpenCV Python Tutorial #8 - Face and Eye Detection

# Hard Cascade - Pre-trained Classifier
# We are using the Haar Cascade


import cv2
import numpy as np


cap = cv2.VideoCapture(0)  # Webcam enumeration
delay = 1  # delay between frames

# Load a classifier from a file in venv/Lib/site-packages/cv2/data:
#   haarcascade_eye.xml
#   haarcascade_eye_tree_eyeglasses.xml
#   haarcascade_frontalcatface.xml
#   haarcascade_frontalcatface_extended.xml
#   haarcascade_frontalface_alt.xml
#   haarcascade_frontalface_alt2.xml
#   haarcascade_frontalface_alt_tree.xml
#   haarcascade_frontalface_default.xml
#   haarcascade_fullbody.xml
#   haarcascade_lefteye_2splits.xml
#   haarcascade_licence_plate_rus_16stages.xml
#   haarcascade_lowerbody.xml
#   haarcascade_profileface.xml
#   haarcascade_righteye_2splits.xml
#   haarcascade_russian_plate_number.xml
#   haarcascade_smile.xml
#   haarcascade_upperbody.xml
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')


if not cap.isOpened():
    print('Cannot open video stream')
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print('Camera disconnected')
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Camera 0', gray)

    # Detect faces and return a list of rectangle coordinates
    # Recommended values for OpenCV detectMultiScale() parameters
    #   https://stackoverflow.com/questions/20801015/recommended-values-for-opencv-detectmultiscale-parameters
    #   https://sites.google.com/site/5kk73gpu2012/assignment/viola-jones-face-detection#TOC-Image-Pyramid
    #   https://answers.opencv.org/question/10654/how-does-the-parameter-scalefactor-in-detectmultiscale-affect-face-detection/
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for x, y, w, h in faces:
        # Draw rectangles around detected faces
        cv2.rectangle(frame, (x, y), (x + w, y + h), color=(0, 255, 0), thickness=2)

        # Get the "Region of Interest"
        #   y before x -> (row, col) in this array
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # Find the eyes on the greyscale face
        eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.3, minNeighbors=5)
        # Draw the eyes on the coloured face - which has the same coordinate system as the greyscale face
        for ex, ey, ew, eh in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), color=(255, 0, 0), thickness=2)

    cv2.imshow('Camera 0', frame)
    if cv2.waitKey(delay) == ord('q'):  # Hit q to exit
        break

cap.release()  # Release the camera
cv2.destroyAllWindows()
