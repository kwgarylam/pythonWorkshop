import cv2
import numpy as np

# An image with 1024 * 768
img = cv2.imread('engine.png')

img_resized = cv2.resize(img, None,fx=0.1, fy=0.1, interpolation = cv2.INTER_CUBIC)

imgGrayscale = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)                 # grayscale

imgBlurred = cv2.GaussianBlur(imgGrayscale, (5, 5), 0)                       # blur
    
imgCanny = cv2.Canny(imgBlurred, 100, 200)                                   # Canny edges

# Extra algorithm
(T, thresh) = cv2.threshold(imgGrayscale, 50, 255, cv2.THRESH_BINARY)        # Binary

imgBlend = cv2.divide(imgGrayscale, imgBlurred, scale=256)


# show windows
cv2.imshow("Original", img_resized)
cv2.imshow("Gray", imgGrayscale)
cv2.imshow("Blurred", imgBlurred)
cv2.imshow("Canny", imgCanny)
cv2.imshow("Binary", thresh)
cv2.imshow("Blend", imgBlend)

# hold windows open until user presses a key
cv2.waitKey()                               
cv2.destroyAllWindows() 