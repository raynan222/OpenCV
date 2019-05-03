import matplotlib.pyplot as plt
import cv2
import numpy as np

img = cv2.imread("caro.PNG", 0)


cv2.imshow("nome da janela",img)
cv2.waitKey(0)
cv2.destroyAllWindows()



cv2.imwrite("novo.png",img)