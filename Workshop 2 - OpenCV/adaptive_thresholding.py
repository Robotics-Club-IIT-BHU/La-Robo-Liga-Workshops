import cv2

img = cv2.imread('images/blocks.jpg', 0)
cv2.imshow('image', img)

mean_thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
gaussian_thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
cv2.imshow('mean_thresh', mean_thresh)
cv2.imshow('gaussian_thresh', gaussian_thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()