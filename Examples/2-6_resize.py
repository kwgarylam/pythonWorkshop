import cv2

image = cv2.imread('testImg.png')

resizedImg = cv2.resize(image, (400,400), interpolation = cv2.INTER_CUBIC)

cv2.imshow('Resized Image', resizedImg)

cv2.waitKey(0)
cv2.destroyAllWindows()