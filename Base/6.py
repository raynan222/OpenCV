import cv2
import numpy as np

img=cv2.imread("capacete-3.jpg")
retval, threshold=cv2.threshold(img,120 ,255,cv2.THRESH_BINARY)
grays=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval2, threshold2=cv2.threshold(grays,120 ,255,cv2.THRESH_BINARY)
gaus=cv2.adaptiveThreshold(grays,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)

cv2.imshow("original",img)
cv2.imshow("THRESHOLD",threshold)
cv2.imshow("THRESGRAY",threshold2)
cv2.imshow("GRAY",grays)
cv2.imshow("GUAS",gaus)
cv2.waitKey(0)

cv2.destroyAllWindows()