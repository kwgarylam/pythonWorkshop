import numpy as np
from PIL import ImageGrab
import cv2
import time

def screen_record(): 
    last_time = time.time()
    while(True):
        # 800x600 windowed mode
        # 40 px accounts for title bar. 
        printscreen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))

        #print('loop took {} seconds'.format(time.time()-last_time))
        #print('Frame rate: {}'.format(round(1/(time.time()-last_time),2)))
        #last_time = time.time()

        img = cv2.resize(printscreen, None,fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        cv2.imshow('window',cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))

        
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

screen_record()