import cv2
import numpy as np


def convert_bgr_to_hsv(blue, green, red):
    # Create a single pixel BGR image as a numpy array
    bgr_color = np.array([[[blue, green, red]]], dtype=np.uint8)  # create a 1 pixel image
    """
    MUST specify dtype=np.uint8, otherwise:
        > Unsupported depth of input image:
        >     'VDepth::contains(depth)'
        > where
        >     'depth' is 4 (CV_32S)
    """
    x = cv2.cvtColor(bgr_color, cv2.COLOR_BGR2HSV)
    return x[0][0]


# Convert BGR blue to HSV
print(convert_bgr_to_hsv(255, 0, 0))  # -> [120 255 255]


cap = cv2.VideoCapture(0)  # Webcam enumeration
delay = 1  # delay between frames

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

    cv2.imshow('Raw Frame', frame)

    # Convert colour space from BGR to HSV
    # See RGB <-> HLS ( CV_BGR2HLS, CV_RGB2HLS, CV_HLS2BGR, CV_HLS2RGB )
    # https://docs.opencv.org/2.4/modules/imgproc/doc/miscellaneous_transformations.html#cvtcolor
    # HSL values are normally
    #   H = 0-360 degrees,
    #   S = 0-1 or 0-100 %
    #   V = 0-1 or 0-100 %
    # But CV_BGR2HLS, CV_RGB2HLS, CV_HLS2BGR, CV_HLS2RGB convert 8 bit images:
    #   H = H / 2,
    #   S = S * 255
    #   V = V * 255
    # This affects the way we generate our mask
    hsv = cv2.cvtColor(frame, code=cv2.COLOR_BGR2HSV)
    cv2.imshow('HSV', hsv)

    # Generate a blue mask
    # upper and lower bounds for colours to display
    # https://alloyui.com/examples/color-picker/hsv.html
    # Because we are using 8-bit image, we have to convert
    # Dark green  HSL = 180, 28, 12 -> 90, 71, 30
    # Light green HSL = 260, 100, 100 -> 130, 255, 255
    lower_bound = np.array([90, 70, 30])
    upper_bound = np.array([130, 255, 255])
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    cv2.imshow('Blue Mask', mask)

    result = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('Masked Frame', result)

    if cv2.waitKey(delay) == ord('q'):  # Hit q to exit
        break

cap.release()  # Release the camera
cv2.destroyAllWindows()
