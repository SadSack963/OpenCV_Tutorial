import cv2
import numpy as np

cap = cv2.VideoCapture(0)  # Webcam enumeration
delay = 1  # delay between frames

# cap = cv2.VideoCapture('assets/PowerTel 701.mp4')  # Video file
# delay = 25  # delay between frames

# cap = cv2.VideoCapture('rtsp://192.168.0.30:10001/1/stream1')  # Video stream
# delay = 1  # delay between frames

green = (0, 255, 0)
if not cap.isOpened():
    print('Cannot open video stream')
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print('Camera disconnected')
        break
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    img = cv2.line(frame, (100, 100), (200, 200), color=green)
    img = cv2.rectangle(img, (200, 200), (400, 300), color=(255, 255, 0), thickness=2)
    img = cv2.circle(img, center=(300, 300), radius=30, color=(0, 0, 255), thickness=-1)

    # https://docs.opencv.org/4.5.3/d6/d6e/group__imgproc__draw.html
    # HersheyFonts
    #   cv::FONT_HERSHEY_SIMPLEX = 0, normal size sans-serif font
    #   cv::FONT_HERSHEY_PLAIN = 1, small size sans-serif font
    #   cv::FONT_HERSHEY_DUPLEX = 2, normal size sans-serif font (more complex than FONT_HERSHEY_SIMPLEX)
    #   cv::FONT_HERSHEY_COMPLEX = 3, normal size serif font
    #   cv::FONT_HERSHEY_TRIPLEX = 4, normal size serif font (more complex than FONT_HERSHEY_COMPLEX)
    #   cv::FONT_HERSHEY_COMPLEX_SMALL = 5, smaller version of FONT_HERSHEY_COMPLEX
    #   cv::FONT_HERSHEY_SCRIPT_SIMPLEX = 6, hand-writing style font
    #   cv::FONT_HERSHEY_SCRIPT_COMPLEX = 7, more complex variant of FONT_HERSHEY_SCRIPT_SIMPLEX
    #   cv::FONT_ITALIC = 16, flag for italic font
    # LineTypes
    #   cv::FILLED = -1,
    #   cv::LINE_4 = 4,
    #   cv::LINE_8 = 8,
    #   cv::LINE_AA = 16
    img = cv2.putText(img, 'John', (100, 400), fontFace=17, fontScale=3, color=(0, 255, 255), thickness=3, lineType=15)

    cv2.imshow('Camera 0', img)
    if cv2.waitKey(delay) == ord('q'):  # Hit q to exit
        break

cap.release()  # Release the camera
cv2.destroyAllWindows()
