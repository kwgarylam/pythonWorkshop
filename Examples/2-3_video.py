import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while (cap.isOpened()):
    ret, image = cap.read()

    cv2.imshow('Video Capture', image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()