import cv2
import numpy as np

image = cv2.imread("testImg.png")

#讀取相片並裁切需要的區域 format Y1: Y2 X1: X2

cropped = image[100: 600, 920: 1490]
cv2.imshow("cropped", cropped)

# 將裁切的影像轉為灰階，再使用 Gaussian Blurring 將其模糊化，
# 減少相片中複雜的物體，讓它們較為圓滑一致。
imgTest = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
imgTestBlur = cv2.G aussianBlur(imgTest, (11,11), 0)

# 若超過 T 值，則將該點設為最大值，否則為 0
(T, thresh) = cv2.threshold(imgTestBlur, 35, 255, cv2.THRESH_BINARY)

cv2.imshow("Threshold Binary", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()