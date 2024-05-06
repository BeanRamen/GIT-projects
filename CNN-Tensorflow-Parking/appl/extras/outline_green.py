import cv2
import numpy as np

# Citirea imaginii
img = cv2.imread('appl/asset/parking_lot/parking.jpg')

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

# Identificarea contururilor în imaginea alb-negru
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Desenarea contururilor pe imaginea originală
for contour in contours:
    # Calcularea dreptunghiului care înconjoară conturul
    x, y, w, h = cv2.boundingRect(contour)
    # Desenarea dreptunghiului
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # culoarea verde, grosimea liniei 2

# Afisarea imaginii cu loturile de parcare conturate
cv2.imshow('Parking Lots', img)
cv2.waitKey(0)
cv2.destroyAllWindows()