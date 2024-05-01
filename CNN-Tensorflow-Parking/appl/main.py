import os
import cv2
import pickle
import cvzone
import numpy as np
ok = 0

width, height = 80, 145
with open('appl/CarParkPos', 'rb') as f:
    posList = pickle.load(f)

def checkParkingSpace():
    i=0
    for pos in posList:
        x,y = pos
        imgCrop = img[y:y+height,x:x+width]
        resize = cv2.resize(imgCrop,(256,256))
        filename = f'appl/asset/resized_livephotoes/{i}.jpg'
        cv2.imwrite(filename, resize)
        cv2.imshow(str(i),resize)
        i=i+1
   
def runfilter():
    global ok
    if ok == 0:
        os.system("filter_newParking.ipynb")
        ok = 1
        
def showparking():
    i = 0
    with open('appl/asset/predict_txt/predictions.txt', 'r') as f:  
        lines = f.readlines()  # Citeste liniile din fișier

    for pos in posList:
        if i < len(lines):
            prediction = int(lines[i].split()[1])
            color = (0, 255, 0)
            if prediction == 1:
                color = (0, 0, 255)

            cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, 2)
        i += 1

    cv2.imshow("Image", img)


running = True
while running:
    img = cv2.imread('appl/asset/parking_lot/parking.jpg')
    
    checkParkingSpace()
    #runfilter()
    
    showparking()
    
    
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # Dacă tasta apăsată este 'ESC'
        running = False
cv2.destroyAllWindows()