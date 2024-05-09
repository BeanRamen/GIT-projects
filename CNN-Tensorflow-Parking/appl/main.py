import os
import cv2
import pickle
import cvzone
import numpy as np
ok = 0
park_i=1

width, height = 80, 145


def checkParkingSpace():
    i=0
    for pos in posList:
        x,y = pos
        imgCrop = img[y:y+height,x:x+width]
        resize = cv2.resize(imgCrop,(256,256))
        filename = f'CNN-Tensorflow-Parking/appl/asset/resized_livephotoes/parking_spot_{park_i}/{i}.jpg'
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
    with open(f'CNN-Tensorflow-Parking/appl/asset/predict_txt/predictions_parking_{park_i}.txt', 'r') as f:  
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
    with open(f'CNN-Tensorflow-Parking/appl/asset/position/CarParkPos_{park_i}', 'rb') as f:
        posList = pickle.load(f)
        
    img = cv2.imread(f'CNN-Tensorflow-Parking/appl/asset/parking_lot/parking_{park_i}.jpg')
    
    checkParkingSpace()
    #runfilter()
    
    showparking()
    
    
    key = cv2.waitKey(1) & 0xFF
    if key == 13:
        park_i = park_i+1
        if park_i > 1:
            width, height = 125, 145
        
    if key == 27:  # Dacă tasta apăsată este 'ESC'
        running = False
cv2.destroyAllWindows()