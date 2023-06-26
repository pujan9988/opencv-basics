""" CREATING TRACKBARS TO DETECT THE PARAMETERS LIKE HUE,SATURATION,ETC AND USING IT TO DETECT THE COLORS  """

import cv2,numpy as np
def empty(a):
    pass

#making a window for the trackbar and other images
cv2.namedWindow("Trackbar",cv2.WINDOW_NORMAL)
cv2.namedWindow("Image",cv2.WINDOW_NORMAL)
cv2.namedWindow("Mask",cv2.WINDOW_NORMAL)
cv2.namedWindow("newimg",cv2.WINDOW_NORMAL)

#creating a trackbar
cv2.createTrackbar("Hue min","Trackbar",0,179,empty)
cv2.createTrackbar("Hue max","Trackbar",148,179,empty)
cv2.createTrackbar("Sat min","Trackbar",119,255,empty)
cv2.createTrackbar("Sat max","Trackbar",255,255,empty)
cv2.createTrackbar("Val min","Trackbar",161,255,empty)
cv2.createTrackbar("Val max","Trackbar",255,255,empty)

while True:
    #reading the image
    img = cv2.imread("images/cards.jpg")

    #converting to hsv image
    hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    #applying the trackbar to read values in our image
    h_min = cv2.getTrackbarPos("Hue min","Trackbar")
    h_max = cv2.getTrackbarPos("Hue max","Trackbar")
    s_min = cv2.getTrackbarPos("Sat min","Trackbar")
    s_max = cv2.getTrackbarPos("Sat max","Trackbar")
    v_min = cv2.getTrackbarPos("Val min","Trackbar")
    v_max = cv2.getTrackbarPos("Val max","Trackbar")


    print(h_min,h_max,s_min,s_max,v_min,v_max)

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])

    #this will create the values
    mask = cv2.inRange(hsv_img,lower,upper)  

    #filling the img with desired colors only
    new_img = cv2.bitwise_and(img,img,mask=mask)


    # cv2.imshow("orginal image",img)
    cv2.imshow("Image",img)
    cv2.imshow("Mask",mask)
    cv2.imshow("newimg",new_img)

    cv2.waitKey(1)

