""" warp perspective refers to a geometric transformation technique used to manipulate the perspective of an image. It involves changing the position and orientation of the pixels in an image to create a new view that appears as if the image was captured from a different viewpoint. """

import cv2
import numpy as np

#read the images
img = cv2.imread("images/cards.jpg")


# Define the desired window size
window_width = 500
window_height = 500

# Create a named window with the specified size
cv2.namedWindow("Card image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Card image", window_width, window_height)

width,height = 250,350

#setting the fours corner points of ace of hearts
points1 = np.float32([[1541,409],[2816,888],[918,2082],[2089,2566]])

#giving the values for four corner points
points2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

#we require transformation matrix for warp perspective
matrix = cv2.getPerspectiveTransform(points1,points2)

imgoutput = cv2.warpPerspective(img,matrix,(width,height)) 

#display the images
cv2.imshow("Card image",img)
cv2.imshow("output",imgoutput)

# create an infinite delay
cv2.waitKey(0)