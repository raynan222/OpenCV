import cv2
import numpy as np
img=cv2.imread("capacete-3.jpg",1)
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lower_green=np.array([50,0,50])
upper_green=np.array([255,180,255])

mask=cv2.inRange(hsv,lower_green,upper_green)
res=cv2.bitwise_and(img,img,mask=mask)

cv2.imshow("a",img)
cv2.imshow("b",mask)
cv2.imshow("c",res)
cv2.waitKey(0)

cv2.destroyAllWindows()