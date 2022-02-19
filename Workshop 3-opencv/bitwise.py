import cv2
import numpy as np
img = cv2.imread("resources\pic.png")
img2 = cv2.imread("resources\imaze.png")

hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hsv_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)

cv2.imshow("img",img)
cv2.imshow("img2",img2)
res = cv2.bitwise_and(img, img2, mask= None)
cv2.imshow("result",res)
cv2.waitKey(0)
cv2.destroyAllWindows()