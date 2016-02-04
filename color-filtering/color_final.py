import numpy as np
import cv2

# Load a color image
img = cv2.imread('pokemon.png', cv2.IMREAD_COLOR)

# Convert BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

def nothing(x):
    pass

# Create a UI Window
cv2.namedWindow('Color Filter Parameters');

# Create trackbars
cv2.createTrackbar('H Max','Color Filter Parameters',0,255,nothing)
cv2.createTrackbar('H Min','Color Filter Parameters',0,255,nothing)
cv2.createTrackbar('S Max','Color Filter Parameters',0,255,nothing)
cv2.createTrackbar('S Min','Color Filter Parameters',0,255,nothing)
cv2.createTrackbar('V Max','Color Filter Parameters',0,255,nothing)
cv2.createTrackbar('V Min','Color Filter Parameters',0,255,nothing)

# Set the trackbar positions (default 0)
cv2.setTrackbarPos('H Max','Color Filter Parameters', 255)
cv2.setTrackbarPos('V Max','Color Filter Parameters', 255)
cv2.setTrackbarPos('S Max','Color Filter Parameters', 255)

while True :

    # Get all trackbar positions for filtering.
    h_max = cv2.getTrackbarPos('H Max','Color Filter Parameters')
    h_min = cv2.getTrackbarPos('H Min','Color Filter Parameters')
    s_max = cv2.getTrackbarPos('S Max','Color Filter Parameters')
    s_min = cv2.getTrackbarPos('S Min','Color Filter Parameters')
    v_max = cv2.getTrackbarPos('V Max','Color Filter Parameters')
    v_min = cv2.getTrackbarPos('V Min','Color Filter Parameters')

    # Threshold the HSV image.  Lower bounds and upper bounds must be numpy arrays
    # Our binary thresholded image is saved into mask
    mask = cv2.inRange(hsv, np.array([h_min, s_min, v_min]), np.array([h_max, s_max, v_max]))

    img2 = img.copy();
    # Bitwise-AND mask and original image
    # res = cv2.bitwise_and(img,img, mask= mask)

    # To draw a rectangle - image, point1, point2, color, line thickness
    # cv2.rectangle(res, (0,0), (50,50), (0,255,0),3)

    # To find contours of the thresholded image
    # im2, contours, hierarchy = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    # Find the contours of our thresholded image
    im2, contours, hierarchy = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    areas = [cv2.contourArea(c) for c in contours]
    max_index = np.argmax(areas)
    cnt=contours[max_index]
    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(img2,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow('image',img2)
    # cv2.imshow('mask',mask)
    # cv2.imshow('res',res)
    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
