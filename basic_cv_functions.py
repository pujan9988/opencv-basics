# BASIC FUNCTIONS IN OPENCV

import cv2
import numpy as np

#read the image
img = cv2.imread("images/cat.png")

#creating a matrix of 5x5 containing all ones of unsigned integer
kernel = np.ones((5,5),np.uint8)

# now we will convert the image into grayscale using cvtColor() function and it takes two positional argument img and the destination color
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# to blur the image, we can use GaussianBlur and it takes three positional arguments; imgsrc,kernelsize(ksize) and sigmaX
blur_img = cv2.GaussianBlur(imgGray,(7,7),0)


#to find out the edges in the images, we use edge detector methods and this method is known as canny edge detector 

canny_img = cv2.Canny(img,100,100)

#when detecting edges, there is gap or joint because of which edges will not be detected properly, so we can increase the thickness of edge using dilation
dilation_img = cv2.dilate(canny_img,kernel,iterations=1)

#to resize the image, we have resize() method
resized_canny_img = cv2.resize(canny_img,(250,250))

#cropping an image do not require function, we can simply use the matrix data
#height first and then width
cropped_img = img[0:200,150:300]


# display the image
# cv2.imshow("Dilate Image",dilation_img)
cv2.imshow("Canny Image",canny_img)

# cv2.imshow("cropped canny Image",resized_canny_img)
cv2.imshow("Cropped Image",cropped_img)

#for infinite delay of the image to be shown on the screen
cv2.waitKey(0)