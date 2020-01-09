import cv2
import numpy as np

imgT = cv2.imread("test_image.png", cv2.IMREAD_GRAYSCALE)
img1 = cv2.imread("image_1.png", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("image_2.png", cv2.IMREAD_GRAYSCALE)
img3 = cv2.imread("image_3.png", cv2.IMREAD_GRAYSCALE)

imgT = cv2.resize(imgT, None,fx=0.25, fy=0.25, interpolation = cv2.INTER_CUBIC)
img1 = cv2.resize(img1, None,fx=0.25, fy=0.25, interpolation = cv2.INTER_CUBIC)
img2 = cv2.resize(img2, None,fx=0.25, fy=0.25, interpolation = cv2.INTER_CUBIC)
img3 = cv2.resize(img3, None,fx=0.25, fy=0.25, interpolation = cv2.INTER_CUBIC)

bit_xor1 = cv2.bitwise_xor(imgT, img1)
bit_xor2 = cv2.bitwise_xor(imgT, img2)
bit_xor3 = cv2.bitwise_xor(imgT, img3)

diff1 = cv2.countNonZero(bit_xor1)
diff2 = cv2.countNonZero(bit_xor2)
diff3 = cv2.countNonZero(bit_xor3)

print("Test image and Image 1 ")
print("Error: ", diff1, end="\n\n")

print("Test image and Image 2 ")
print("Error: ", diff2, end="\n\n")

print("Test image and Image 3 ")
print("Error: ", diff3, end="\n\n")
