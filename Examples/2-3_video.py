import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while (cap.isOpened()):
    ret, image = cap.read()

    # Code in here #

    cv2.line(image, (0,0), (255,255), (0, 0, 255), 5)
    text = 'Hello world!'
    cv2.putText(image, text, (40,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255, 255), 1, cv2.LINE_AA)

    #              #

    cv2.imshow('Video Capture', image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()