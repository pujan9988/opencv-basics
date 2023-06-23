import cv2,numpy as np

#create an matrix filled with zeros i.e a black image
img = np.zeros((512,512,3),np.uint8)

#to color the image completely
img[:] = 255,0,0 #this gives the color blue

#to create line we have define the starting point and ending point with color and thickness(optional)
cv2.line(img,(0,0),(300,300),(0,255,0),3)

#to create a rectangle and it follows the same convention as line
cv2.rectangle(img,(0,0),(250,350),(0,0,255),3)

#to draw the circle we have to define the center point and radius
cv2.circle(img,(450,50),30,(255,255,0),5)

#to put text on image
cv2.putText(img,"opencv text feature",(300,100),cv2.FONT_HERSHEY_PLAIN,1,(0,255,0)) 

 

#to show the image
cv2.imshow("Image",img)


# to create infinite delay for image to show
cv2.waitKey(0)