import cv2
import numpy as np
# load the image we want to transform
img = cv2.imread('perspective.png')
img = cv2.resize(img, None,fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)

# We need to select 4 points, in order: top-left, top-right, bottom-left, bottom-right
cv2.circle(img, (243, 24), 5, (0, 0, 255), -1)
cv2.circle(img, (116, 267), 5, (0, 0, 255), -1)
cv2.circle(img, (572, 408), 5, (0, 0, 255), -1)
cv2.circle(img, (633, 124), 5, (0, 0, 255), -1)

# The points to apply the transformation
old_pts = np.float32([[243, 24], [116, 267], [572, 408], [633, 124]])

# The points (size of windows) to display the image transformed
# The size of an A4 paper is 297 x 210 mm
new_pts = np.float32([[0, 0], [0, 124], [221, 124], [221, 0]])

# Apply the perspective transform to create the matrix
matrix = cv2.getPerspectiveTransform(old_pts, new_pts)

# Warp the image into using the original frame and the matrix
result = cv2.warpPerspective(img, matrix, (297, 210))

# Show it on the screen
cv2.imshow("Image", img)
cv2.imshow("Perspective transformation", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
