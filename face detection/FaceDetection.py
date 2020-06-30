import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
img = cv2.imread ("klopp2.jpg", 1)
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img, scaleFactor= 1.05, minNeighbors=5)

for x,y,w,h in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

cv2.imshow("Legend",img)
cv2.waitKey(0)
cv2.destroyAllWindows()