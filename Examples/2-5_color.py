import cv2
image = cv2.imread('testImg.png')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray_image.png', gray_image)

cv2.imshow('color_image', image)
cv2.imshow('gray_image', gray_image)
# Waits forever until press any key
cv2.waitKey(0)

# Closes displayed windows
cv2.destroyAllWindows()