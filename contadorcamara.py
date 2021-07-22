import cv2
import numpy

ValorGauss= 3
ValorKernel= 3

CapturaVideo=cv2.VideoCapture(1) # find the cameras, in my case 1 is droidcam and 0 webcam

if not CapturaVideo.isOpened():
    print ('no se encontro camara')
    exit()

while True:
    tipocamara,camara=CapturaVideo.read() #read the camera
    grises=cv2.cvtColor(camara,cv2.COLOR_BGR2GRAY)
    gausiano=cv2.GaussianBlur (grises,(ValorGauss,ValorGauss),0)
    Canny= cv2.Canny(gausiano,60,100)
    kernel=numpy.ones((ValorKernel,ValorKernel),numpy.uint8)
    cierre=cv2.morphologyEx(Canny,cv2.MORPH_CLOSE,kernel)
    contornos,jerarquias = cv2.findContours(cierre.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) # Create the contorn
    cv2.drawContours (camara,contornos,-1,(0,0,255),2) #Draw the contors 


    cv2.imshow('Camara original',camara)
    if cv2.waitKey(1)==ord('q'): break
CapturaVideo.release()
cv2.destroyAllWindows
