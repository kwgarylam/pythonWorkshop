import cv2
import numpy as np

# Function for color space conversion
# eg. HSV: 0,255,255 is BGR: 0, 0, 255(Red)
def HSV2BGR(H,S,V):
    original_hsv = np.uint8([[[H,S,V]]])
    bgr_color = cv2.cvtColor(original_hsv,cv2.COLOR_HSV2BGR)
    print("HSV to BGR: ",bgr_color[0,:][0,:])
    return bgr_color

def BGR2HSV(B,G,R):
    original_rgb = np.uint8([[[B,G,R ]]])
    hsv_color = cv2.cvtColor(original_rgb,cv2.COLOR_BGR2HSV)
    print("BGR to HSV: ",hsv_color[0,:][0,:])
    return hsv_color

img = cv2.imread('circles.png')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Color space conversion
B = 255
G = 0
R = 0
hsv_color = BGR2HSV(B,G,R)

# Convert the space conversion to int type and single list
circles = np.round(hsv_color[0,:][0,:]).astype("int")
h,s,v = int(circles[0]),int(circles[1]),int(circles[2])
lower_range = np.array([h,s,v])
upper_range = np.array([h+10,s,v])

mask = cv2.inRange(hsv, lower_range, upper_range)
contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0, 128, 255), 3)

cv2.imshow('image', img)
cv2.imshow('mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
