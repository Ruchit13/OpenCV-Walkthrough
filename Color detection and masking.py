#Import the libraries
import cv2
import numpy as np

capture = cv2.VideoCapture(0)

while True:
    res, frame = capture.read()
    width = int(capture.get(3))
    height = int(capture.get(4))

    #Create a hsv capture by converting our input/Arguments - (input,color_conversioncode)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #Define the range of the blue or any other color you'd prefer to highlight in the capture
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])

    #Create a mask that masks the hsv frame between upper and lower blue
    mask = cv2.inRange(hsv,lower_blue,upper_blue)

    #Create the resultant frame using bitwise and
    result = cv2.bitwise_and(frame,frame,mask = mask)

    #Display the frame and the masked frame
    cv2.imshow("Resultant", result)
    cv2.imshow("Masked frame",mask)

    #Wait infinitely until c key is clicked
    if cv2.waitKey(1) == ord('c'):
        break

cap.release()
cv2.destroyAllWindows()