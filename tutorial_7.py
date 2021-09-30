# #OpenCV #Python #TemplateMatching
# OpenCV Python Tutorial #7 - Template Matching (Object Detection)

# matchTemplate()
#   https://docs.opencv.org/master/df/dfb/group__imgproc__object.html#ga586ebfb0a7fb604b35a23d85391329be
# TemplateMatchModes
#   https://docs.opencv.org/master/df/dfb/group__imgproc__object.html#ga3a7850640f1fe1f58fe91a2d7583695d
# cv::TemplateMatchModes {
#   cv::TM_SQDIFF = 0,
#   cv::TM_SQDIFF_NORMED = 1,
#   cv::TM_CCORR = 2,
#   cv::TM_CCORR_NORMED = 3,
#   cv::TM_CCOEFF = 4,
#   cv::TM_CCOEFF_NORMED = 5
# }


import numpy as np
import cv2


img = cv2.imread('assets/soccer_practice.jpg', cv2.IMREAD_GRAYSCALE)

# template = cv2.imread('assets/ball.PNG', cv2.IMREAD_GRAYSCALE)  # cv2.TM_CCORR failed to find the ball
template = cv2.imread('assets/shoe.PNG', cv2.IMREAD_GRAYSCALE)  # cv2.TM_CCORR and cv2.TM_CCOEFF failed to find the shoe
height, width = template.shape

# All six methods for comparison
methods = [
    cv2.TM_SQDIFF,
    cv2.TM_SQDIFF_NORMED,
    cv2.TM_CCORR,
    cv2.TM_CCORR_NORMED,
    cv2.TM_CCOEFF,
    cv2.TM_CCOEFF_NORMED,
]

for method in methods:
    # Create a copy of the image because we are going to draw on it
    img_copy = img.copy()
    result = cv2.matchTemplate(img_copy, template, method)  # Perform convolution
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Get the correct location
    # These two methods return a match location at the minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc

    # Draw a rectangle around the location
    bottom_right = (top_left[0] + width, top_left[1] + height)
    cv2.rectangle(img_copy, top_left, bottom_right, color=255, thickness=2)
    cv2.imshow(str(method), img_copy)

cv2.waitKey(0)
cv2.destroyAllWindows()
