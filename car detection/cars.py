import numpy as np
import cv2

car_cascade = cv2.CascadeClassifier('haarcascade_car.xml')

car = cv2.VideoCapture("C:\\Users\\Majed\\Downloads\\cars.mp4")

while car.isOpened():
    success, img = car.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray,scaleFactor= 1.3,minNeighbors= 4)

    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)

    cv2.imshow("Car Detector",img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break



car.release()
cv2.destroyAllWindows()