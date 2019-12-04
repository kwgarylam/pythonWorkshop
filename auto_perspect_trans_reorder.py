import cv2
import numpy as np

img = cv2.imread('perspective.png')
img = cv2.resize(img, None,fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   

ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)   
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  

def find_vertix(contours):
    # Find the biggest contour
    cnt = contours[0]
    max_area = cv2.contourArea(cnt)
    for cont in contours:
        pts = cv2.approxPolyDP(cont,30,True)
        if len(pts) == 4:
            if cv2.contourArea(cont) > max_area:
                points = pts
                max_area = cv2.contourArea(cont)
    
    return points


def order_points(pts):
        # initialzie a list of coordinates 
        # first entry in the list is the top-left, the second entry is the top-right, 
		# the third is the bottom-right, and the fourth is the bottom-left
        rect = np.zeros((4, 2), dtype = "float32")

        # the top-left point will have the smallest sum, whereas
        # the bottom-right point will have the largest sum
        s = np.sum(pts, axis = 1)
        print ("Sum: ", s, "Index: ", np.argmin(s),np.argmax(s), end='\n\n')
        rect[0] = pts[np.argmin(s)]
        rect[2] = pts[np.argmax(s)]

        # top-right point will have the smallest difference,
        # whereas the bottom-left will have the largest difference
        diff = np.diff(pts, axis = 1)
        print ("Diff: ", diff.reshape(1,4), "Index: ", np.argmin(diff),np.argmax(diff), end='\n\n')
        rect[1] = pts[np.argmin(diff)]
        rect[3] = pts[np.argmax(diff)]

        # return the ordered coordinates
        return rect

vertix = find_vertix(contours)
# Since the returned vertixs are wrapped by 3 taples (x,y,z),
# it can be simplified to a 4 by 2 matrix (x,y)
reshapedVertix = vertix.reshape(4, 2)
print ("Original Order:")
print ("0:", reshapedVertix[0],"  1:",reshapedVertix[1],"  2:",reshapedVertix[2],"  3:",reshapedVertix[3], end='\n\n')

pts = order_points(reshapedVertix)
print ("Re-ordered:")
print ("0:", pts[0],"1:",pts[1],"2:",pts[2],"3:",pts[3], end='\n\n')

# Label the vertix on the image
cv2.circle(img, (pts[0][0], pts[0][1]), 5, (0, 0, 255), -1)
cv2.circle(img, (pts[1][0], pts[1][1]), 5, (0, 0, 255), -1)
cv2.circle(img, (pts[2][0], pts[2][1]), 5, (0, 0, 255), -1)
cv2.circle(img, (pts[3][0], pts[3][1]), 5, (0, 0, 255), -1)

cv2.imshow("Contours", img)    
cv2.waitKey(0)  
cv2.destroyAllWindows()  
