import cv2
import numpy as np

image = cv2.imread('testImg.png')
cv2.imshow("Original", image)

AvgBlur = cv2.blur(image, (5,5))
cv2.imshow("Averaged blur", AvgBlur)

GausBlur = cv2.GaussianBlur(image, (5,5), 0)
cv2.imshow("Gaussian Blur", GausBlur)

cv2.waitKey(0)
cv2.destroyAllWindows()