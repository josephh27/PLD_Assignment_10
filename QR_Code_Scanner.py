import cv2
import numpy as np
from pyzbar.pyzbar import decode
from datetime import datetime 

# img_1 = cv2.imread("qr_code.png")
now = datetime.now().replace(microsecond = 0)
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)



while True:
    success, img = cap.read()
    for barcode in decode(img):
        my_data = barcode.data.decode("utf-8")
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,(0,255,0),5)
        pts2 = barcode.rect
        cv2.putText(img,"SCANNING COMPLETE YEEHAW",(pts2[0],pts2[1]),cv2.FONT_HERSHEY_COMPLEX,0.9,(0,255,0),2)
        fh = open("Personal_Data.txt", "w")
        fh.write(f"{my_data}\n\n\n\nDate and Time read: {now}")
        print("Scanning Done")
        fh.close()

    cv2.imshow("Result", img)
    cv2.waitKey(1)
    


