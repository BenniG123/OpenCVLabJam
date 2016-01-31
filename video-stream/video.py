import numpy as np
import cv2

# This should grab from your webcam.  If you have multiple web cams,
# you can change the index to get video from a different one.
# To take in footage from a video file, change the index to the relative path of
# your video file aka 'test_footage.mp4'
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
