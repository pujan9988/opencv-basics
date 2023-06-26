""" RESIZING AND RESCALING IMAGES AND VIDEOS """

import cv2 as cv

# reading the image
img = cv.imread("images/cards.jpg")


# to rescale images or video frames, we create a function 
def rescaleFrame(frame,scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)

    """The cv.resize function takes three parameters: the frame to be resized, the dimensions (new width and height), and the interpolation method to be used for resizing.
    The interpolation argument (cv.INTER_AREA in this case) specifies the method used to calculate new pixel values when resizing the image. Different interpolation methods produce different results. The cv.INTER_AREA method is typically used for downsampling (reducing the size of the image) and can provide good quality results while reducing aliasing effects. """ 

    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)

capture = cv.VideoCapture('images/tech.mp4')

while True:
    isTrue,frame = capture.read()
    
    frame_resized = rescaleFrame(frame,scale=0.2)

    cv.imshow('resized_vide0',frame_resized)
    cv.imshow('video',frame)
    
    if cv.waitKey(20) & 0xFF==ord('q'):
        break


capture.release()
cv.destroyAllWindows()
