#Import the libraries
import cv2
import random

#Read the image
image = cv2.resize(cv2.imread(r'C:\Users\Ruchit Singh\Desktop\OpenCV\test_images\NEW_IMG.jpg', 1),(0,0), fx=0.3,fy=0.3)

#Show the image
cv2.imshow('Image',image)
cv2.waitKey(0)

#Print the shape of the array
print(image.shape)

#The Number of rows and columns and channels in the image
print(image[0])
print(image[1])
print(image[2])

"""
3 Different ways the channels exist are : 
RGB - Red Green Blue
HSV - Hue Saturation Value
BGR - Blue Green Red
"""

# Edit the original image
for i in range(100): #Loops through only first 100 rows
    for j in range(image.shape[1]): # Loops throughout the width
        image[i][j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)] 

#Save the image as a new file/Arguments are the new file image and the original image
cv2.imwrite('NEW_IMG_EDIT.jpg',image)

#Display the original image and destroy the window on a click of a key
cv2.imshow('Image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()