# AN INTRODUCTION TO OPENCV TO READ AND DISPLAY IMAGES AND VIDEOS

import cv2
# to read images imread is used and it takes path as an argument
img = cv2.imread("images/cat.png")

# # to show the images, imshow takes two arguments name of the output to display and the image
cv2.imshow("Cat Image",img)

# #to create a delay and 0 means infinite time and some value means millisecond
cv2.waitKey(0)

#to capture videos, videocapture is used and it takes path as an argument 

cap = cv2.VideoCapture("images/tech.mp4")

#to read the webcames we can use 0,1,2.. as an argument if there is only one camera 0 is used
cap = cv2.VideoCapture(0)

#there are different id for the set method and we define the width which is id no 3 to 640
cap.set(3,640)

#we define the height which is id no 4 to 480
cap.set(4,480)
#we define the brightness which is id no 10
cap.set(10,200)


#since videos are sequences of images so we need to loop through each frame of videos
while True:

    #video_frame.read will return a boolean value and a single frame of video
    single_frame_success,single_frame = cap.read()
    cv2.imshow("Tech video",single_frame)

    #it waits for the delay and waits for key 'q' to be pressed to exit video
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break;