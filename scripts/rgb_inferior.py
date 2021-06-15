import cv2 
from time import time

nombre = input("Nombre_Apellido: ")

cap = cv2.VideoCapture(0,cv2.CAP_V4L)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
cap.set(3,1920) #3, 1910 // 1280
cap.set(4, 1080)
if not cap.isOpened():
    print("Camera not found!")
    exit(1)

#Camara RGB-1
k = 0
prev = time()

while True:
    cur = time()
    k += cur-prev
    prev=cur
    ret, frame = cap.read()
    if k>1:
        img_name = "../Pruebas/15-06-2021/angular/inferior_{}.png".format(nombre)
        ret, frame = cap.read() 
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        cv2.waitKey(123)
        break

cv2.destroyAllWindows()
