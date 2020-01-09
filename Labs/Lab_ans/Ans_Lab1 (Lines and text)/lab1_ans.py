import cv2
import numpy as np

# An image with 1024 * 768
img = cv2.imread('rocket.png')

cv2.line(img, (800, 0), (800, 1024), (0, 0, 255), 5)
cv2.line(img, (0, 500), (1024, 500), (0, 0, 255), 5)

cv2.rectangle(img, (20, 60), (120, 160), (0, 255, 0), 2)
cv2.rectangle(img, (40, 70), (130, 180), (0, 255, 0), 2)
cv2.rectangle(img, (40, 80), (100, 140), (0, 255, 0), -1) 

text = 'Hello world!'
cv2.putText(img, text, (50, 600), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA) 

cv2.imshow("Image", img)
cv2.waitKey()                               # hold windows open until user presses a key
cv2.destroyAllWindows() 
