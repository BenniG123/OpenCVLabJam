import numpy as np
import cv2

# Load a color image
img = cv2.imread('pokemon.png', cv2.IMREAD_COLOR)

# Convert BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

def nothing(x):
    pass

cv2.namedWindow('Color Filter Parameters');

# Create trackbars
cv2.createTrackbar('H Max','Color Filter Parameters',0,255,nothing)
cv2.createTrackbar('S Max','Color Filter Parameters',0,255,nothing)
cv2.createTrackbar('V Max','Color Filter Parameters',0,255,nothing)
cv2.createTrackbar('H Min','Color Filter Parameters',0,255,nothing)
cv2.createTrackbar('S Min','Color Filter Parameters',0,255,nothing)
cv2.createTrackbar('V Min','Color Filter Parameters',0,255,nothing)

# lower_bounds = np.array([50,50,50])
# upper_bounds = np.array([130,255,255])

while True :

    h_max = cv2.getTrackbarPos('H Max','Color Filter Parameters')
    h_min = cv2.getTrackbarPos('H Mix','Color Filter Parameters')
    s_max = cv2.getTrackbarPos('S Max','Color Filter Parameters')
    s_min = cv2.getTrackbarPos('S Min','Color Filter Parameters')
    v_max = cv2.getTrackbarPos('V Max','Color Filter Parameters')
    v_min = cv2.getTrackbarPos('V Min','Color Filter Parameters')

    # Threshold the HSV image
    mask = cv2.inRange(hsv, np.array([h_min, s_min, v_min]), np.array([h_max, s_max, v_max]))

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(img,img, mask= mask)

    # cv2.imshow('image',img)
    # cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
