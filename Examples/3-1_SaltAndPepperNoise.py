import numpy as np  
import cv2 
img = cv2.imread('SaltAndPepperNoise.jpg') 
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

median = cv2.medianBlur(imgray,5)

cv2.imshow("Salt_PepperNoise", img)
cv2.imshow("Median filter", median)

cv2.waitKey(0)
cv2.destroyAllWindows()
