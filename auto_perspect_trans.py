import cv2
import numpy as np
# load the image we want to transform  
img = cv2.imread('perspective.png')
img = cv2.resize(img, None,fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)

# Find the contours
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)   
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  

# Find the largest contour with 4 vertix
def find_vertix(contours):
    cnt = contours[0]
    max_area = cv2.contourArea(cnt)

    for cont in contours:
        pts = cv2.approxPolyDP(cont,30,True)
        # If the contours have 4 vertix
        if len(pts) == 4:
            # Find the biggest contour
            if cv2.contourArea(cont) > max_area:
                points = pts
                max_area = cv2.contourArea(cont)
    return points

vertix = find_vertix(contours)
# Since the contours returned are wrapped by 3 taples (x,y,z),
# it can be simplified to a 4 by 2 matrix (x,y)
reshapedVertix = vertix.reshape(4, 2)

# Label the vertix on the image
cv2.circle(img, (reshapedVertix[0][0], reshapedVertix[0][1]), 5, (0, 0, 255), -1)
cv2.circle(img, (reshapedVertix[1][0], reshapedVertix[1][1]), 5, (0, 0, 255), -1)
cv2.circle(img, (reshapedVertix[2][0], reshapedVertix[2][1]), 5, (0, 0, 255), -1)
cv2.circle(img, (reshapedVertix[3][0], reshapedVertix[3][1]), 5, (0, 0, 255), -1)

cv2.imshow("Contours", img)    
cv2.waitKey(0)  
cv2.destroyAllWindows()  
