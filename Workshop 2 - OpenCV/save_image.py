import cv2

#read image from the resource folder

path = "images/PPxNH.jpg"

image = cv2.imread(path)

#save image to the resource folder

cv2.imwrite('resources/newly_saved.png',image)
