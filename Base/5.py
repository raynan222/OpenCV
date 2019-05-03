import cv2
import numpy as np

img1=cv2.imread("3D-Matplotlib.png")
img2=cv2.imread("mainlogo.png")

#add=img1+img2
#add=cv2.add(img1,img2)
#weigh=cv2.addWeighted(img1,0.6,img2,0.4,0)

rows,coluns,canais=img2.shape
roi=img1[0:rows ,0:coluns]
img2gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

ret,mask=cv2.threshold(img2gray,220,255,cv2.THRESH_BINARY_INV)
mask_inv=cv2.bitwise_not(mask)
img1_bg=cv2.bitwise_and(roi,roi,mask=mask_inv)
img2_fg=cv2.bitwise_and(img2,img2,mask=mask)

dst=cv2.add(img1_bg,img2_fg)
img1[0:rows,0:coluns]=dst
cv2.imshow("g",img1)
cv2.imshow("a",mask_inv)
cv2.imshow("b",dst)
cv2.imshow("h",mask)
cv2.imshow("i",img2_fg)
cv2.imshow("o",img1_bg)
cv2.waitKey(0)
cv2.destroyAllWindows()