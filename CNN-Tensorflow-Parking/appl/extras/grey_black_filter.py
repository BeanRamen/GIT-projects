import cv2
import numpy as np

# Citirea imaginii
img = cv2.imread('D:/downloads/ANUL 3/SEM2/PSK/asset/parking_lot/parking.jpg')

# Redimensionarea imaginii la jumătate
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

# Convertirea imaginii la spațiul de culoare HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Definirea intervalului de culoare pentru culoarea albă
lower_white = np.array([0, 0, 200])
upper_white = np.array([180, 50, 255])

# Crearea unei măști pentru culorile care se încadrează în intervalul definit
mask = cv2.inRange(hsv, lower_white, upper_white)

# Aplicarea măștii pe imaginea originală pentru a izola zonele albe
parking_lots = cv2.bitwise_and(img, img, mask=mask)

# Afisarea imaginii cu loturile de parcare evidențiate
cv2.imshow('Parking Lots', parking_lots)
cv2.waitKey(0)
cv2.destroyAllWindows()