import cv2

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smileCascade = cv2.CascadeClassifier('haarcascade_smile.xml')
 
cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,      
        minSize=(30, 30)
    )

    smile = smileCascade.detectMultiScale(
    gray,
    scaleFactor= 1.7,
    minNeighbors=20
    )

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        for sx,sy,sw,sh in smile:
            cv2.rectangle(img,(sx,sy),((sx+sw),(sy+sh)),(0,255,0),3)
        if len(smile)>0:
            cv2.putText(img,"Alegre",(x,y+h+40),fontScale=3,fontFace=cv2.FONT_HERSHEY_PLAIN, color=(255,255,255),thickness=2)
      
    cv2.imshow('video', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27: 
        break

cap.release()
cv2.destroyAllWindows()
