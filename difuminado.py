import cv2

# Read in image
image = cv2.imread('seb1.jpg')

# Create ROI coordinates
topLeft = (67, 109)
bottomRight = (137, 289)
x, y = topLeft[0], topLeft[1]
w, h = bottomRight[0] - topLeft[0], bottomRight[1] - topLeft[1]

topLeft1 = (51, 374)
bottomRight1 = (149, 549)
x1, y1 = topLeft1[0], topLeft1[1]
w1, h1 = bottomRight1[0] - topLeft1[0], bottomRight1[1] - topLeft1[1]

# Grab ROI with Numpy slicing and blur
ROI = image[y:y+h, x:x+w]
ROI2=image[y1:y1+h1, x1:x1+w1]

blur = cv2.GaussianBlur(ROI, (51,51), 0)
blur2 = cv2.GaussianBlur(ROI2, (51,51), 0)
# Insert ROI back into image
image[y:y+h, x:x+w] = blur
image[y1:y1+h1, x1:x1+w1] = blur2
#cv2.imshow('blur', blur)
cv2.imshow('image', image)
cv2.imwrite('C:/Users/5178886/PycharmProjects/dia18/venv/sebdif.jpg', image)
cv2.waitKey()