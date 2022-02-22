from cv2 import IMREAD_GRAYSCALE
import numpy as np
import cv2

img = cv2.imread("stars.jpg")
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt=contours[0]

#Method 1: Straight Rectangle
# x,y,w,h=cv2.boundingRect(cnt)
# cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
# cv2.imshow('Bounding rect',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#Method 2: Rotated Rectangle
# rect = cv2.minAreaRect(cnt)
# box = cv2.boxPoints(rect)
# box = np.int0(box)
# cv2.drawContours(img,[box],0,(0,0,255),2)
# cv2.imshow('Bounding rect',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#Method 3: Bounding circle
(x,y),radius = cv2.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
cv2.circle(img,center,radius,(0,255,0),2)
cv2.imshow('Bounding circ',img)
cv2.waitKey(0)
cv2.destroyAllWindows()