import cv2

# import random
#
# img = cv2.imread("assets/Fun Ride.jpg", cv2.IMREAD_COLOR)
# for row in range(100):
#     for col in range(img.shape[1]):
#         img[row][col] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
# cv2.imshow('Fun Ride Modified', img)

img = cv2.imread("assets/Fun Ride.jpg", cv2.IMREAD_COLOR)
tag = img[30:130, 110:210]  # Copy a slice of the image
img[200:300, 300:400] = tag  # Paste it somewhere else

cv2.imshow('Fun Ride Modified', img)

cv2.waitKey(0)  # Wait for any key press (milliseconds: 0 = infinite)
cv2.destroyAllWindows()
