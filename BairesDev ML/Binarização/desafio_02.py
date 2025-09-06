import cv2
import numpy as np

imagem = cv2.imread('montanha.jpg')
cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
suavizada = cv2.GaussianBlur(cinza, (7, 7), 0)

_, binaria = cv2.threshold(suavizada, 160, 255, cv2.THRESH_BINARY)
_, binaria_invertida = cv2.threshold(suavizada, 160, 255, cv2.THRESH_BINARY_INV)

combinada = np.vstack([
    np.hstack([suavizada, binaria]),
    np.hstack([binaria, cv2.bitwise_and(cinza, cinza, mask=binaria)])
])

cv2.imshow("Resultado da Binarização", combinada)
cv2.waitKey(0)
cv2.destroyAllWindows()
