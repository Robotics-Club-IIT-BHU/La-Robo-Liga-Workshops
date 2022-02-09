import cv2
import numpy as np

img = cv2.imread('images/blocks.jpg')
cv2.imshow('image', img)

# RESIZE

resized_img = cv2.resize(img, (300, 200))
cv2.imshow('resized_img', resized_img)

resized_img = cv2.resize(img, (0, 0), fx = 0.5, fy = 0.5)
cv2.imshow('resized_img', resized_img)

# CROPPING
cropped_img = img[100 : 500 , 200 : 500]
cv2.imshow('cropped_img', cropped_img)

cv2.waitKey(0)
cv2.destroyAllWindows()