import cv2
import numpy as np
img = cv2.imread("resources\cool.jpg")

#line
cv2.line(img,(0,0),(150,150),(255,0,0),20)

#rectangle
cv2.rectangle(img,(150,150),(300,300),(0,255,0),10)

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
