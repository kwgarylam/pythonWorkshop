import cv2
import numpy as np


img = cv2.imread('pattern.png')

img_resized = cv2.resize(img, None,fx=0.8, fy=0.8, interpolation = cv2.INTER_CUBIC)
    
imgGrayscale = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)                 # grayscale
    
imgBlurred = cv2.GaussianBlur(imgGrayscale, (5, 5), 0)                       # blur
    
ret, binary = cv2.threshold(imgBlurred, 127, 255, cv2.THRESH_BINARY)   
    
cv2.imshow("binary", binary)
    
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)   
    
# Numbers of contours in the image
print ("Total Numbers of contours:", str(len(contours)), end="\n\n")
    
index = 0

for cnt in contours:
    # 0.01: very high precision
    approxVertex = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)

    if len(approxVertex)==4:

        cv2.drawContours(img_resized, [approxVertex], -1, (0, 0, 255), 3)

        index = index + 1

        print ("There are " + str(len(cnt)) + " points in contour", index)
        print ("There are " + str(len(approxVertex)) + " vertics in contour", index)

        area = cv2.contourArea(cnt)
        print ("The area is: ", area, " in contour", end="\n\n")

            
            
cv2.imshow('Output', img_resized)
cv2.waitKey()                               
cv2.destroyAllWindows() 
