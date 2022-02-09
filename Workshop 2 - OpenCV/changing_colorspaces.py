import cv2

img = cv2.imread('images/blocks.jpg')
cv2.imshow('image', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('gray', gray)
cv2.imshow('rgb', rgb)
cv2.imshow('hsv', hsv)

cv2.waitKey(0)
cv2.destroyAllWindows()