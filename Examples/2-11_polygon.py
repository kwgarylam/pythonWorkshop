import numpy as np
import cv2
# Read the image and convert to gray tone
img = cv2.imread('polygon.png')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# Find the contours
ret,thresh = cv2.threshold(imgray,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

print ("there are " + str(len(contours)) + " contours")
# The first polygon
cnt = contours[0]
print ("there are " + str(len(cnt)) + " points in contours[0]")
approx = cv2.approxPolyDP(cnt,30,True)
print ("after approx, there are " + str(len(approx)) + " points")
print (approx)
#cv2.drawContours(img,[approx],0,(0,255,0),-1)

 # The second polygon
cnt = contours[1]
print ("there are " + str(len(cnt)) + " points in contours[1]")
approx = cv2.approxPolyDP(cnt,30,True)
print ("after approx, there are " + str(len(approx)) + " points")
print (approx)
#cv2.drawContours(img,[approx],0,(0,0,255),-1)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()