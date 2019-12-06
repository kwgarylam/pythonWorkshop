import cv2
import numpy as np
# Read the image in gray scale
img1 = cv2.imread("drawing_1.png", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("drawing_2.png", cv2.IMREAD_GRAYSCALE)
# Resize the image to 1/4, in order to speed up the calculation
img1 = cv2.resize(img1, None,fx=0.25, fy=0.25, interpolation = cv2.INTER_CUBIC)
img2 = cv2.resize(img2, None,fx=0.25, fy=0.25, interpolation = cv2.INTER_CUBIC)

bit_and = cv2.bitwise_and(img2, img1)
bit_or = cv2.bitwise_or(img2, img1)
bit_xor = cv2.bitwise_xor(img1, img2)
bit_not = cv2.bitwise_not(img2)

# Remerber the image must be in binary format for non-zero counting
#diff = cv2.countNonZero(bit_xor)
#print("Image 3 and Image 4 ")
#print("Error: ", diff)

# Show the results
cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("bit_and", bit_and)
cv2.imshow("bit_or", bit_or)
cv2.imshow("bit_xor", bit_xor)
cv2.imshow("img2_bit_not", bit_not)

cv2.waitKey(0)
cv2.destroyAllWindows()