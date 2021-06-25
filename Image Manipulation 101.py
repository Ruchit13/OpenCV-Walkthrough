#Import the OpenCV Library
import cv2

"""
  cv::IMREAD_UNCHANGED = -1,
  cv::IMREAD_GRAYSCALE = 0,
  cv::IMREAD_COLOR = 1,
"""
# Read the image via imread/Arguments include directory and a flag value
image = cv2.imread(r'C:\Users\Ruchit Singh\Desktop\OpenCV\test_images\flower.jpg',-1)

#Resizing the image/Arguments include the img,(window_width,window_height),additional args: (fx,fy)
image = cv2.resize(image,(0,0),fx= 0.5,fy=0.5)

#Rotating the image/Arguments include the img,rotation specification
image = cv2.rotate(image,cv2.cv2.ROTATE_90_CLOCKWISE)

#Write the new manipulated image to new img/Arguments include new file name and the manipulated img
cv2.imwrite('Flower_edited.jpg',image)

#imshow displays the image/Arguments include the window name and the img
window_name = 'Test_Window'
cv2.imshow(window_name,image)

#Used to wait for a brief amount of seconds before exiting. If 0 is used, then it waits infinitely,until a key is pressed
cv2.waitKey(0)

#Destroys all the windows
cv2.destroyAllWindows()