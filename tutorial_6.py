import numpy as np
import cv2
from random import randint


img = cv2.imread('assets/chess_board.jpg')
# img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Corner Detection
corners = cv2.goodFeaturesToTrack(grey, 100, 0.03, 40)
corners = np.int0(corners)  # Convert float coordinates to integer

for corner in corners:
    # x = corner[0][0]
    # y = corner[0][1]
    x, y = np.ravel(corner)
    # print(x, y)
    cv2.circle(img, center=(x, y), radius=6, color=(0, 0, 255), thickness=2)

for i in range(len(corners)):
    print(corners[i])  # -> [[203 342]]
    # c_i = (x_i, y_i) = np.ravel(corners[i])
    # c_i = tuple(corners[i])
    # print(c_i)  # -> (array([203, 342], dtype=int64),)
    c_i = tuple(corners[i][0])
    for j in range(i + 1, len(corners)):
        # c_j = (x_j, y_j) = np.ravel(corners[j])
        c_j = tuple(corners[j][0])
        # line_color = (randint(0, 255), randint(0, 255), randint(0, 255))
        line_color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
        cv2.line(img, c_i, c_j, color=line_color, thickness=1)


cv2.imshow('Image', img)
cv2.waitKey(0)  # Wait for any key press (milliseconds: 0 = infinite)
cv2.destroyAllWindows()
