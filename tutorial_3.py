import cv2
import numpy as np

cap = cv2.VideoCapture(0)  # Webcam enumeration
delay = 1  # delay between frames

# cap = cv2.VideoCapture('assets/PowerTel 701.mp4')  # Video file
# delay = 25  # delay between frames

# cap = cv2.VideoCapture('rtsp://192.168.0.30:10001/1/stream1')  # Video stream
# delay = 1  # delay between frames


if not cap.isOpened():
    print('Cannot open video stream')
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print('Camera disconnected')
        break

    # Get the frame dimensions
    # VideoCaptureProperties enumeration:
    #   https://docs.opencv.org/4.5.3/d4/d15/group__videoio__flags__base.html
    #       cv::CAP_PROP_FRAME_WIDTH =3,
    #       cv::CAP_PROP_FRAME_HEIGHT =4,
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    image = np.zeros(frame.shape, dtype=np.uint8)

    # Rotate frame
    #   https://docs.opencv.org/4.5.3/d2/de8/group__core__array.html
    #   cv::ROTATE_90_CLOCKWISE = 0,
    #   cv::ROTATE_180 = 1,
    #   cv::ROTATE_90_COUNTERCLOCKWISE = 2

    # TOP LEFT
    # image[:height // 2, :width // 2] = cv2.rotate(small_frame, 2)
    # Causes ValueError: could not broadcast input array from shape (320,240,3) into shape (240,320,3)
    img_ccw = cv2.resize(
        cv2.rotate(
            small_frame,
            cv2.ROTATE_90_COUNTERCLOCKWISE
        ),
        (320, 240)
    )
    image[:height // 2, :width // 2] = img_ccw

    # BOTTOM LEFT
    image[height // 2:, :width // 2] = cv2.rotate(small_frame, cv2.ROTATE_180)

    # TOP RIGHT
    img_cw = cv2.resize(
        cv2.rotate(
            small_frame,
            cv2.ROTATE_90_CLOCKWISE
        ),
        (320, 240)
    )
    image[:height // 2, width // 2:] = img_cw

    # BOTTOM RIGHT
    image[height // 2:, width // 2:] = small_frame


    cv2.imshow('Camera 0', image)
    if cv2.waitKey(delay) == ord('q'):  # Hit q to exit
        break

cap.release()  # Release the camera
cv2.destroyAllWindows()
