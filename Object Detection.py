import numpy as np
import cv2

#Image input
img = cv2.resize(cv2.imread(r'C:\Users\Ruchit Singh\Desktop\OpenCV\test_images\image.jpg', 0), (0,0),fx=0.8,fy=0.8)
#object to be detected input
object = cv2.resize(cv2.imread(r'C:\Users\Ruchit Singh\Desktop\OpenCV\test_images\mask.jpg', 0),(0,0),fx=0.8,fy=0.8)

#Get the height and weight of the object
h, w = object.shape

#List of different methods for template matching
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED,
           cv2.TM_CCORR, cv2.TM_CCORR_NORMED,
           cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

"""
We use the sliding window with stride one and map which creates a  certain dimensional array,
with values that signifies the accuracy of how close the object is similar to the respective frame
"""

for i in methods:
    img2 = img.copy() #Copy the image
    result = cv2.matchTemplate(img2, object, i)
    # Result includes the floating points of template matching
    #print(result)
    # Gets the min value, max_value,location of min value and max value
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(min_loc,max_loc)
    """
    For cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED templates:: We use minimum location
    For cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED,
        cv2.TM_CCORR, cv2.TM_CCORR_NORMED templates:: We use maximum location
       
    """
    if i in [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc
    #define the bottom location cordinates of the rectangle
    bottom_location = (location[0] + w, location[1]+ h)
    #draw the rectangle on the object detected
    cv2.rectangle(img2,location,bottom_location,255, 1)
    #displays the object detected for 6 different templates
    cv2.imshow('Match',img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

