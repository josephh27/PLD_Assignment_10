#The importing of the necessary modules.
import cv2
import numpy as np
from pyzbar.pyzbar import decode
from datetime import datetime 

#The setup of the camera and the time of scan
now = datetime.now().replace(microsecond = 0)
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)



#Enclosing it into a while True loop so the webcam stays and doesn't have a short duration.
while True:
    success, img = cap.read()
    for barcode in decode(img):
        #To remove the {b} when decoding.
        my_data = barcode.data.decode("utf-8")
        #To add the bounding box
        #Using polygon instead of rectangle since using rectangle might cause visual bounding problem when camera is rotated.
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))

        #This is the part where we put the texts shown when the scan is successful.
        cv2.polylines(img,[pts],True,(0,255,0),5)
        pts2 = barcode.rect
        #Customizing the thickness, color, font, and scale of the text.
        cv2.putText(img,"SCANNING COMPLETE YEEHAW",(pts2[0],pts2[1]),cv2.FONT_HERSHEY_COMPLEX,0.9,(0,255,0),2)
        #Opening the text file on write mode
        fh = open("Personal_Data.txt", "w")
        fh.write(f"{my_data}\n\n\n\nDate and Time read: {now}")
        print("Scanning Done")
        fh.close()

    cv2.imshow("Result", img)
    cv2.waitKey(1)
    


