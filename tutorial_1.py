# OpenCV
# Open Source Computer Vision

# Tech With Tim: OpenCV Python Tutorial #1 - Introduction & Images
# https://www.youtube.com/watch?v=qCR2Weh64h4&list=PLzMcBGfZo4-lUA8uGjeXhBUUzPYc6vZRn&index=1

import cv2


# ImreadModes
# https://docs.opencv.org/4.5.3/d8/d6a/group__imgcodecs__flags.html#ga61d9b0126a3e57d9277ac48327799c80
# Enumerations
# cv::ImreadModes {
#   cv::IMREAD_UNCHANGED = -1,
#   cv::IMREAD_GRAYSCALE = 0,
#   cv::IMREAD_COLOR = 1,
#   cv::IMREAD_ANYDEPTH = 2,
#   cv::IMREAD_ANYCOLOR = 4,
#   cv::IMREAD_LOAD_GDAL = 8,
#   cv::IMREAD_REDUCED_GRAYSCALE_2 = 16,
#   cv::IMREAD_REDUCED_COLOR_2 = 17,
#   cv::IMREAD_REDUCED_GRAYSCALE_4 = 32,
#   cv::IMREAD_REDUCED_COLOR_4 = 33,
#   cv::IMREAD_REDUCED_GRAYSCALE_8 = 64,
#   cv::IMREAD_REDUCED_COLOR_8 = 65,
#   cv::IMREAD_IGNORE_ORIENTATION = 128
# }
#
# IMREAD_UNCHANGED
#   If set, return the loaded image as is (with alpha channel, otherwise it gets cropped). Ignore EXIF orientation.
# IMREAD_GRAYSCALE
#   If set, always convert image to the single channel grayscale image (codec internal conversion).
# IMREAD_COLOR (Default)
#   If set, always convert image to the 3 channel BGR color image.
# img = cv2.imread("assets/Fun Ride.jpg", cv2.IMREAD_COLOR)
img = cv2.imread("assets/Fun Ride.jpg", cv2.IMREAD_GRAYSCALE)
# img = cv2.imread("assets/Fun Ride.jpg", cv2.IMREAD_UNCHANGED)
cv2.imshow('Image', img)  # Display the image in a window titled Image

img_resized = cv2.resize(img, (400, 400))  # 400x400 pixels
cv2.imshow('Image Resized', img_resized)

img_resized_2 = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)  # half scale
cv2.imshow('Image Resized 2', img_resized_2)

img_rotated_cw = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)  # or cv2.cv2.ROTATE_90_CLOCKWISE
cv2.imshow('Image Rotate CW', img_rotated_cw)

cv2.imwrite("assets/Fun Ride Grayscale Rotated.jpg", img_rotated_cw)

cv2.waitKey(0)  # Wait for any key press (milliseconds: 0 = infinite)
cv2.destroyAllWindows()
