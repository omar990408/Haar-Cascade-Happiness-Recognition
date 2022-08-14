import cv2
#Importamos el archivo de la clase CascadeClassifier
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smileCascade = cv2.CascadeClassifier('haarcascade_smile.xml')
#Leemos la imagen
image = cv2.imread('Sonrisa2.png')
#Convertimos la imagen a escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#Detectamos los rostros en la imagen 
faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,      
)
#Recorremos todas las caras detectadas
for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
    #Detectamos las sonrisas en la imagen
    smile = smileCascade.detectMultiScale(
            gray,
            scaleFactor= 1.5,
            minNeighbors=20,
            minSize=(1, 1),
            maxSize=(400, 400)
            )
    #Etiquetamos los rostros con una sonrisa    
    for i in smile:
        if len(smile)>0:
            cv2.putText(image,"Alegre",(x,y+h+40),fontScale=3,fontFace=cv2.FONT_HERSHEY_PLAIN, color=(0,255,0),thickness=3)
    #Dibujamos un rectangulo en la sonrisa       
    for sx,sy,sw,sh in smile:
        cv2.rectangle(image,(sx,sy),((sx+sw),(sy+sh)),(0,255,0),3)
#Mostramos la imagen               
cv2.imshow('image', image)
k = cv2.waitKey(0)
cv2.destroyAllWindows()
