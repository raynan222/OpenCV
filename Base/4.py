import numpy as np
import cv2

img = cv2.imread("capacete-3.jpg", cv2.IMREAD_COLOR)

img[200,200]=[0,0,0]
img[199,199]=[0,0,0]
img[198,198]=[0,0,0]
img[197,197]=[0,0,0]
img[196,196]=[0,0,0]

px = img [200,200]
print(px)

maqcario = img[100:150, 100:150]
img[200:250, 200:250] = maqcario


cv2.imshow("capacete-3.jpg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()