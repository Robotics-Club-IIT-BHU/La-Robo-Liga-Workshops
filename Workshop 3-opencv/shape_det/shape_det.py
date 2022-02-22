import numpy as np
import cv2

#Contour Approximation Demo

# img = cv2.imread("approximate.png")
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
# contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# #cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
# #cv2.imshow("img1", img)
# epsilon=0.1*cv2.arcLength(contours[0], True)
# approx=cv2.approxPolyDP(contours[0], epsilon, True)
# cv2.drawContours(img, [approx], -1, (0, 255, 0), 3)
# cv2.imshow("img", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#Shape Detection Example

img = cv2.imread('shapes.png')
cv2.imshow("img", img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, threshold = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
i=1
for contour in contours:
    if i==1:
        i=2
        continue
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [contour], 0, (0, 0, 255), 5)
    M = cv2.moments(contour)
    if M['m00'] != 0.0:
        x = int(M['m10']/M['m00'])
        y = int(M['m01']/M['m00'])
  
    if len(approx) == 3:
        cv2.putText(img, 'Triangle', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
  
    elif len(approx) == 4:
        cv2.putText(img, 'Quadrilateral', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
    else:
        cv2.putText(img, 'circle', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
cv2.imshow("shape_detected", img)
cv2.waitKey(0)
cv2.destroyAllWindows()