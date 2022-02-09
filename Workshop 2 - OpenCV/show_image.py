import cv2

#read image from the resource folder

path = "images/Demo_image.png"

image = cv2.imread(path, 1)


cv2.imshow('image', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
