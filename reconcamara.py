import cv2
import numpy

ValorGauss=1
ValorKernel=1
capturavideo=cv2.VideoCapture(1)
if not capturavideo.isOpened():
    print('no se encontro camara')
    exit()
while True:
    TipoCamara,camara=capturavideo.read()
    gris = cv2.cvtColor(camara, cv2.COLOR_BGR2GRAY) #pasa a grises
    gauss=cv2.GaussianBlur(gris, (ValorGauss,ValorGauss), 0) #difumina
    canny = cv2.Canny(gauss,60,100) 
    Kernel=numpy.ones((ValorKernel,ValorKernel),numpy.uint8)
    cierre=cv2.morphologyEx(canny,cv2.MORPH_CLOSE,Kernel)
    contornos,jerarquia = cv2.findContours(cierre.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(camara,contornos,-1,(0,0,255),2)    
    cv2.imshow('Live',camara)
    if cv2.waitKey(1)==ord('q'):
        break
capturavideo.release()
cv2.destroyAllWindows()

