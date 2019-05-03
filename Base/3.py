import cv2
import numpy as np

img= cv2.imread("caro.PNG", cv2.IMREAD_COLOR)

#                                 B  G R
cv2.line(img, (0,0), (150,150), (255,122,102), 15)
cv2.rectangle(img, (15,25),(200,150),(0,125,50), 5)
cv2.circle(img, (100,63), 55, (0,0,250), 1)


pts = np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
cv2.polylines(img,[pts], True, (255,255,0), 2)
font=cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, "teste@",(200,200),font,1,(120,60,255),2,cv2.LINE_AA)

cv2.imshow("@@@@",img)
cv2.waitKey(0)
cv2.destroyAllWindows()