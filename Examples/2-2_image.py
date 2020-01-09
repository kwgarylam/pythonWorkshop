import cv2
import numpy as np

# 讀取圖檔
img = cv2.imread('image.jpg')

# 以灰階的方式讀取圖檔 
img_gray = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# 顯示圖片
cv2.imshow('My Image', img_gray)

cv2.imwrite('output.jpg', img_gray)

# 按下任意鍵則關閉所有視窗
cv2.waitKey(0)
cv2.destroyAllWindows()