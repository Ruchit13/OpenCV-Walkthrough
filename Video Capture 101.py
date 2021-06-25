#Import the required libraries
import numpy as  np
import cv2

#Gives access to cv2 to capture the Video/arguments include the number of devices connected to your computer
capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read() #read function reads the frames beign captured and stores it in frame variable. ret is used to monitor the errors generated
    width = int(capture.get(3)) #get function can give us the height of the window using the argument 3
    height = int(capture.get(4)) #get function can give us the height of the window using the argument 4

    image = np.zeros(frame.shape,np.uint8) # the shape of the frame is in float and explicitly converted to int
    smaller_frame = cv2.resize(frame,(0,0),fx=0.5,fy=0.5) #Resizing the frame

    """
    We are basically trying to create a four window capture with two sides flipped 180 
    """

    image[:height//2,:width//2] = cv2.rotate(smaller_frame,cv2.cv2.ROTATE_180)
    image[height//2:,:width//2] = smaller_frame
    image[:height//2, width//2:] = smaller_frame
    image[height//2:,width//2:] = cv2.rotate(smaller_frame,cv2.cv2.ROTATE_180)

    cv2.imshow('frame', image)
    #Waits for the user to press the c key to close the window
    if cv2.waitKey(1) == ord('c'):
        break

#Releases the access over your camera adn destroys all windows
cap.release()
cv2.destroyAllWindows()