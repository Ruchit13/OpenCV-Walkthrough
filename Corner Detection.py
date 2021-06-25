#Import the libraries
import random
import numpy as np
import cv2

#Read the image
image = cv2.imread(r'C:\Users\Ruchit Singh\Desktop\OpenCV\test_images\flower.jpg')
#Resize the image
image = cv2.resize(image,(0,0),fx=0.5,fy=0.5)
#copy the image
img2 = image.copy()
#convert into grayscale
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


corners_detection = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10) # Algorithm to detect the corners
corners = np.int0(corners_detection) # turns the floating points into integers

for i in corners:
    x,y = i.ravel() # returns contiguous flattened array
    cv2.circle(image,(x,y),5,(255,0,0),-1) #Draw a circle

for i in range(len(corners)):
    for j in range(i+1,len(corners)):
        corner1 = tuple(corners[i][0]) #Create a starting point for the line
        corner2 = tuple(corners[j][0]) #Create a ending point for the line
        color = tuple(map(lambda x : int(x), np.random.randint(0,255,size=3))) # anonymous function that randomly assigns the color for every line
        cv2.line(image,corner1,corner2,color,1) #Draw the line

cv2.imshow("Original Image",img2)
cv2.imshow("GrayScale",gray)
cv2.imshow("Corner Detection",image)
cv2.waitKey(0)
cv2.destroyAllWindows()