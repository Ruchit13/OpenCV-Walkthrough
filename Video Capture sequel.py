#import the libraries
import cv2
import numpy as np

#Accessing the camera
capture = cv2.VideoCapture(0)

while True:
    #read the input,get width and height of the window
    res, frame = capture.read()
    width = int(capture.get(3))
    height = int(capture.get(4))

    #Draw a line/Arguments - (input,starting position,ending position,color, thickness)
    img = cv2.line(frame,(0,0),(width//2,height//2),(255,0,0),5)
    img = cv2.line(frame,(width,0), (width//2,height//2),(255,0,0),5)
    img = cv2.line(frame,(0,height),(width//2,height//2),(255,0,0),5)
    img = cv2.line(frame,(width,height),(width//2,height//2),(255,0,0),5)

    #Draw a circle/Arguments - (input,starting position,radius,color,fill value)
    img = cv2.circle(frame,(width//2,height//2),height//4,(255,0,0),-1)


    #Add in Text in the circle/Agruments - (input,text,position,font,font scale,color,thickeness,linetype)
    img = cv2.putText(frame,'HELLO!',(width//2 - 5,height//2),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),2,cv2.LINE_AA,)
    cv2.imshow("Frame",frame)
    if cv2.waitKey(1) == ord('c'):
       break;

capture.release()
cv2.destroyAllWindows()
