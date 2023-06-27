""" CONTOURS AND SHAPE DETECTION """

import cv2 as cv
import numpy as np

# creating a function to get contours
""" The findContours() function analyzes the image and identifies these contours, allowing further processing or analysis to be performed on them.some of the common optional parameters are:-

    Retrieval Mode (mode): The retrieval mode determines the relationship between contours and their hierarchical representation. It specifies how the contours will be retrieved from the image. The available retrieval modes are:

    1. cv2.RETR_EXTERNAL: This mode retrieves only the external contours, excluding         internal contours within objects.
    2. cv2.RETR_LIST: This mode retrieves all contours without establishing any hierarchical relationships. The contours are simply stored in a flat list.
    3. cv2.RETR_CCOMP: This mode retrieves all contours and organizes them into a two-level hierarchy based on their nested relationships. The hierarchy stores information about the contours' parents and their immediate children.
    4. cv2.RETR_TREE: This mode retrieves all contours and reconstructs a full hierarchy of nested contours. The hierarchy represents the complete nesting relationship between contours.

    Contour Approximation Method (method): The contour approximation method determines how contours are approximated from the original image points. It simplifies the contours by compressing segments into endpoints or applying more advanced algorithms. The available contour approximation methods are:

    1. cv2.CHAIN_APPROX_NONE: This method stores all the contour points without any approximation. The contour will have all the original points.
    2. cv2.CHAIN_APPROX_SIMPLE: This method compresses horizontal, vertical, and diagonal segments into their respective endpoints, discarding the intermediate points. It approximates the contour with fewer points, resulting in a simpler representation.
    3. cv2.CHAIN_APPROX_TC89_L1: This method applies the Teh-Chin chain approximation algorithm with the L1 distance metric. It is more accurate than CHAIN_APPROX_SIMPLE but slower.
    4. cv2.CHAIN_APPROX_TC89_KCOS: This method applies the Teh-Chin chain approximation algorithm with the K-cosine distance metric. It provides an even more accurate approximation but is slower than CHAIN_APPROX_SIMPLE. """

def getContours(img):
    contours,hierarchy = cv.findContours(img,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv.contourArea(cnt)
        print(area)
        if area>50:
            cv.drawContours(contour_img,cnt,-1,(255,0,0),3)



img = cv.imread("images/shapes.jpg")
contour_img = img.copy()

cv.namedWindow("original",cv.WINDOW_NORMAL)
cv.namedWindow("Blur",cv.WINDOW_NORMAL)
cv.namedWindow("Grey",cv.WINDOW_NORMAL)
# cv.namedWindow("Canny",cv.WINDOW_NORMAL)


#converting to grayscale
grey_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# making the image blur
blur_img = cv.GaussianBlur(grey_img,(7,7),1)

# using canny edge detector to detect the edge
canny_img = cv.Canny(blur_img,50,50)

getContours(canny_img)

cv.imshow("original",img)
cv.imshow("Grey",grey_img)
cv.imshow("Blur",blur_img)
cv.imshow("Canny",contour_img)

cv.waitKey(0)
cv.destroyAllWindows()