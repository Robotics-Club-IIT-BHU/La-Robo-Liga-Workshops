import cv2

img = cv2.imread('images/blocks.jpg', 0)
cv2.imshow('image', img)

_, binary_thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('binary_thresh', binary_thresh)

_, binary_inv_thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('binary_inv_thresh', binary_inv_thresh)

_, trunc_thresh = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
cv2.imshow('trunc_thresh', trunc_thresh)

_, tozero_thresh = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
cv2.imshow('tozero_thresh', tozero_thresh)

_, tozero_inv_thresh = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
cv2.imshow('tozero_inv_thresh', tozero_inv_thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()