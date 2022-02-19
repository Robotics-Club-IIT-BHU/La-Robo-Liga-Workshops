import cv2
import numpy as np
img = cv2.imread("resources\pic.png")
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#red color
low_red = np.array([0, 140, 90])
high_red = np.array([10, 255, 255])
red_mask = cv2.inRange(hsv_img, low_red, high_red)

#blue color
lower_blue =np.array([115,90,90])
upper_blue =np.array([135,255,255])
blue_mask = cv2.inRange(hsv_img, lower_blue, upper_blue)

#pink color
low_pink = np.array([145, 90, 20])
high_pink = np.array([170, 255, 255])
pink_mask = cv2.inRange(hsv_img, low_pink, high_pink)
pink = cv2.bitwise_and(img, img, mask=pink_mask)

cv2.imshow("img",img)
cv2.imshow("red",red_mask)
cv2.imshow("blue",blue_mask)
cv2.imshow("pink_mask",pink_mask)
cv2.imshow("pink",pink)
cv2.waitKey(0)
cv2.destroyAllWindows()