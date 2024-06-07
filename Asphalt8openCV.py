import cv2
import cv2
import mediapipe as mp
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Key,Controller
import time                 
keyboard = Controller()
  
detector = HandDetector(detectionCon=0.8 , maxHands=1)

video = cv2.VideoCapture(0)
pressed=False

while True:
    ret,frame = video.read()
    hands,img=detector.findHands(frame)
    cv2.rectangle(img,(0,480),(300 , 425),(50,50,225),-2)                         
    cv2.rectangle(img,(640,480),(400 , 425),(50,50,225),-2)
    if hands:
        lmlist = hands[0]
        fingerup=detector.fingersUp(lmlist)
        print(fingerup)  
        if fingerup==[0,0,0,0,0]:
            cv2.putText(frame,'Finger Count: 0',(20,460), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
            cv2.putText(frame,'Nitro',(420,460), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
            keyboard.press(Key.space)
            pressed=True
        if fingerup==[0,1,0,0,0]:
            cv2.putText(frame,'Finger Count: 1',(20,460), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
            cv2.putText(frame,'Moving left',(420,460), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
            keyboard.press('a')
            pressed=True
        if fingerup==[0,1,1,0,0]:
            cv2.putText(frame,'Finger Count: 2',(20,460), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
            cv2.putText(frame,'Moving Right',(420,460), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
            keyboard.press('d')
            pressed=True
        # if fingerup==[0,1,1,1,0]:
        #     cv2.putText(frame,'Finger Count: 3',(20,460), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
        #     cv2.putText(frame,'not jumping',(420,460), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
        #     keyboard.release(Key.space)
        #     pressed=False                                                                       
        # if fingerup==[0,1,1,1,1]:
        #     cv2.putText(frame,'Finger Count: 4',(20,460), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
        #     cv2.putText(frame,'not jumping',(420,460), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
        #     keyboard.release(Key.space)
        #     pressed=False
        # if fingerup==[1,1,1,1,1]:
        #     cv2.putText(frame,'Finger Count: 5',(20,460), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
        #     cv2.putText(frame,'not jumping',(420,460), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
        #     keyboard.release(Key.right)
        #     pressed=False
        # if fingerup!=[0,0,0,0,0] and pressed==True:
        #     keyboard.release(Key.space)
        #     pressed=False


    cv2.imshow("Frame",frame)
    k= cv2.waitKey(1)
    if k==ord('q'):
        break

video.release()
cv2.destroyAllWindows()