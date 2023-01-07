#Major Project Face Detection In an Image
import cv2

face_cascade= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img=cv2.imread('xwitch.webp')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces= face_cascade.detectMultiScale(gray,1.5,9)
#1.5 is scale factor-tuning parameters
for x,y,w,h in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(135,50,80),5)
    #cv2.rectangle(src,start point, end point, color, thickness)

    cv2.imshow('Face Detection',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

