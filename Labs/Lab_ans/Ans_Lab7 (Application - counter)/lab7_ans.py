import cv2
import numpy as np

img = cv2.imread('coin.jpg')
img_original = img.copy()

# cv2.HoughCircles function requires an 8-bit, single channel image,
# convert from the RGB color space to grayscale
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur_img = cv2.medianBlur(gray_img,9)

#
# Please edit the min/max radius eg. 10,50 / 50,120/ 30,150
# detect circles in the image
circles= cv2.HoughCircles(blur_img,cv2.HOUGH_GRADIENT,1.0,65,param1=90,param2=30,minRadius=30,maxRadius=280)


# convert the (x, y) coordinates and radius of the circles to integers
circles = np.round(circles[0, :]).astype("int")

count = 0

for (x,y,r) in circles:
    count = count + 1
    # Outer circle
    cv2.circle(img,(x,y),r,(0,255,0), 6)
    # Inner circle
    cv2.circle(img,(x,y),2,(0,0,255), 3)
    # Text for counting
    cv2.putText(img, str(count), (x+10, y+10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)

cv2.imshow("HoughCirlces", np.hstack([img_original, img]))

cv2.waitKey()
cv2.destroyAllWindows()

##
# cv2.HoughCircles(image, method, dp, minDist)

# image: 8-bit, single channel image. If working with a color image, convert to grayscale first.
# method: Defines the method to detect circles in images. Currently, the only implemented method is cv2.HOUGH_GRADIENT, which corresponds to the Yuen et al. paper.
# dp: This parameter is the inverse ratio of the accumulator resolution to the image resolution (see Yuen et al. for more details). Essentially, the larger the dp gets, the smaller the accumulator array gets.
# minDist: Minimum distance between the center (x, y) coordinates of detected circles. If the minDist is too small, multiple circles in the same neighborhood as the original may be (falsely) detected. If the minDist is too large, then some circles may not be detected at all.
# param1: Gradient value used to handle edge detection in the Yuen et al. method.
# param2: Accumulator threshold value for the cv2.HOUGH_GRADIENT method. The smaller the threshold is, the more circles will be detected (including false circles). The larger the threshold is, the more circles will potentially be returned.
# minRadius: Minimum size of the radius (in pixels).
# maxRadius: Maximum size of the radius (in pixels).
##
