import cv2
import numpy as np

class filtros(object):

    def __init__(self, foto):
        self.path_gray = cv2.imread(foto, 0)
        self.path_color = cv2.imread(foto, 1)

    def guassiano(self, matriz_size):
        self.matriz = (matriz_size, matriz_size)
        self.gaussiada_gray = cv2.GaussianBlur(self.path_gray, self.matriz, 0)
        self.gaussiada_color = cv2.GaussianBlur(self.path_color, self.matriz, 0)

        cv2.imshow("Guassiano GRAY", self.gaussiada_gray)
        cv2.imshow("Guassiano COLOR", self.gaussiada_color)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def mediana(self, matriz_size):
        self.mediana_gray = cv2.medianBlur(self.path_gray, ksize=matriz_size)
        self.mediana_color = cv2.medianBlur(self.path_color, ksize=matriz_size)

        cv2.imshow("Mediana GRAY", self.mediana_gray)
        cv2.imshow("Mediana COLOR", self.mediana_color)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def laplaciano(self, matriz_size):
        self.matriz = (matriz_size, matriz_size)
        self.ddepth = cv2.CV_16UC3
        self.kernel_size = 3
        self.gaussiada_gray = cv2.GaussianBlur(self.path_gray, self.matriz, 0)
        self.filtro= np.array([[1,1,1],[1,-8,1],[1,1,1]])
        self.laplace_matriz = cv2.filter2D(self.gaussiada_gray,-1,self.filtro)
        self.lpc = cv2.Laplacian(self.gaussiada_gray, self.ddepth, self.kernel_size)
        self.laplace_funcao = cv2.convertScaleAbs(self.lpc)

        cv2.imshow("Laplaciana Matriz", self.laplace_matriz)
        cv2.imshow("Laplaciana Função", self.laplace_funcao)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def prewitt(self, matriz_size):
        self.matriz = (matriz_size, matriz_size)
        self.gaussiada_gray = cv2.GaussianBlur(self.path_gray, self.matriz, 0)
        x = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
        y = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
        self.prt_x = cv2.filter2D(self.gaussiada_gray, -1, x)
        self.prt_y = cv2.filter2D(self.gaussiada_gray, -1, y)
        self.prt = self.prt_x + self.prt_y

        cv2.imshow("Prewitt", self.prt)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def media(self, matriz_size):
        self.matriz = (matriz_size, matriz_size)
        self.gaussiada_gray = cv2.GaussianBlur(self.path_gray, self.matriz, 0)
        self.gaussiada_color = cv2.GaussianBlur(self.path_color, self.matriz, 0)
        self.mediax = np.ones([matriz_size, matriz_size]) / (matriz_size ** 2)
        self.mdi_gray = cv2.filter2D(self.gaussiada_gray, -1, self.mediax)
        self.mdi_color = cv2.filter2D(self.gaussiada_color, -1, self.mediax)

        cv2.imshow("Media GRAY", self.mdi_gray)
        cv2.imshow("Media COLOR", self.mdi_color)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def sobel(self, matriz_size):
        self.kernel_size = 3
        self.matriz = (matriz_size, matriz_size)
        self.gaussiada_gray = cv2.GaussianBlur(self.path_gray, self.matriz, 0)
        self.sbl_x = cv2.Sobel(self.gaussiada_gray, cv2.CV_8UC1, 1, 0, self.kernel_size)
        self.sbl_y = cv2.Sobel(self.gaussiada_gray, cv2.CV_8UC1, 0, 1, self.kernel_size)
        self.sbl = self.sbl_x + self.sbl_y

        cv2.imshow("Sobel", self.sbl)
        cv2.waitKey(0)
        cv2.destroyAllWindows()