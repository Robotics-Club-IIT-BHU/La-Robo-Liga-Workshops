import cv2
import numpy as np
img = cv2.imread("resources\white.png")
kernel=np.ones((3,3),np.uint8)

#Erosion
erosion= cv2.erode(img,kernel,iterations=1)

#Dilation
dilation= cv2.dilate(img,kernel,iterations=1)

cv2.imshow("img",img)
cv2.imshow("erosion",erosion)
cv2.imshow("dilation",dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()