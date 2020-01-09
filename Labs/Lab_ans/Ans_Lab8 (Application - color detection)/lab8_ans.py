import cv2
import numpy as np

img = cv2.imread('circles.png')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#original_rgb = np.uint8([[[50,255,255 ]]])
#hsv_color = cv2.cvtColor(original_rgb,cv2.COLOR_BGR2HSV)
#print("HSV: ",hsv_color)

original_hsv = np.uint8([[[0,255,255 ]]])
bgr_color = cv2.cvtColor(original_hsv,cv2.COLOR_HSV2BGR)
print("BGR: ",bgr_color)


circles = np.round(bgr_color[0,:][0,:]).astype("int")
b,g,r = int(circles[0]),int(circles[1]),int(circles[2])

lower_range = np.array([50,255,255])
upper_range = np.array([60,255,255])

mask = cv2.inRange(hsv, lower_range, upper_range)

cv2.circle(img,(10, 10), 10, (b,g,r), -1)
cv2.imshow('image', img)
cv2.imshow('mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()