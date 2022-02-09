import cv2
import numpy as np

img = cv2.imread('images/campus.jpeg')
cv2.imshow('image', img)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

red_mask = cv2.inRange(hsv, np.array([0, 80, 142]), np.array([179, 255, 255]))
cv2.imshow('red_mask', red_mask)

red_part = cv2.bitwise_and(img, img, mask = red_mask)
cv2.imshow('red_part', red_part)

cv2.waitKey(0)
cv2.destroyAllWindows()