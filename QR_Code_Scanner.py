import cv2
import numpy as np
from pyzbar.pyzbar import decode
from datetime import datetime 

# img_1 = cv2.imread("qr_code.png")
now = datetime.now()
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)



while True:
    success, img = cap.read()
    for barcode in decode(img):

        my_data = barcode.data.decode("utf-8")
        fh = open("Personal_Data.txt", "w")
        fh.write(f"{my_data}\n\n\n\nDate and Time read: {now}")
        print("Scanning Done")
        fh.close()

    cv2.imshow("Result", img)
    cv2.waitKey(1)
    


