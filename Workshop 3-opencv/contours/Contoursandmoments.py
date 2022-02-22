import numpy as np
import cv2

# This is the example code for finding contours.

img = cv2.imread("contours.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# print(contours[0])
# cv2.imshow("img", img)
# cv2.imshow("gray", gray)
# cv2.imshow("thresh", thresh)           
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# This is the example of drawing contours.
# Drawing all the contours at once

# cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
# cv2.imshow("img", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#Drawing a single contour at once
#method 1

# cv2.drawContours(img, contours, 3, (0, 255, 0), 3)
# cv2.imshow("img", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
 
#method 2

cnt= contours[3]
cv2.drawContours(img, [cnt], 0, (0, 255, 0), 3)
# cv2.imshow("img", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#This is an example of Moments
M=cv2.moments(cnt)

#This is an example of Centroid calculation
# cx = int(M['m10']/M['m00'])
# cy = int(M['m01']/M['m00'])
# print(cx, cy)
# cv2.circle(img, (cx, cy), 3, (0, 0, 255), -1)
# cv2.imshow("img", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#This is an example of Area calculation
# area=cv2.contourArea(cnt)
# print(area, M['m00'])

#This is an example of Perimeter calculation
perimeter= cv2.arcLength(cnt, True)
print(perimeter)





