import cv2
import pickle
park_i=1
width, height = 80, 145

try:
    with open(f'CNN-Tensorflow-Parking/appl/asset/position/CarParkPos_{park_i}', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []
    
def mouseClick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                posList.pop(i)
    with open(f'CNN-Tensorflow-Parking/appl/asset/position/CarParkPos_{park_i}', 'wb') as f:
        pickle.dump(posList, f)

running = True
while running:
    try:
        with open(f'CNN-Tensorflow-Parking/appl/asset/position/CarParkPos_{park_i}', 'rb') as f:
            posList = pickle.load(f)
    except:
        posList = []

    img = cv2.imread(f'CNN-Tensorflow-Parking/appl/asset/parking_lot/parking_{park_i}.jpg')
    for pos in posList:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)

    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", mouseClick)
    key = cv2.waitKey(1) & 0xFF
    
    if key == 13:
        park_i=park_i+1
        if park_i > 1:
            width, height = 125, 145
        
    
    if key == 27:  # Dacă tasta apăsată este 'ESC'
        running = False

cv2.destroyAllWindows() 