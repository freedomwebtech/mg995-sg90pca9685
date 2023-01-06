from cvzone.HandTrackingModule import HandDetector
import cv2
from adafruit_servokit import ServoKit

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=1)
kit = ServoKit(channels=16)
while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    if hands:
        hands1=hands[0]
        fingers1 = detector.fingersUp(hands1)
        print(fingers1)
        if fingers1[0]==0:
            kit.servo[0].angle = 180
        elif fingers1[0]==1:
            kit.servo[0].angle = 0
___________________________________________________________________            
        if fingers1[0]==0:
            kit.servo[1].angle = 0
        elif fingers1[0]==1:
            kit.servo[1].angle = 90
___________________________________________________________________            
        if fingers1[1]==0:
            kit.servo[2].angle = 180
        elif fingers1[1]==1:
            kit.servo[2].angle = 0
____________________________________________________________________            
        if fingers1[2]==0:
            kit.servo[3].angle = 180
        elif fingers1[2]==1:
            kit.servo[3].angle = 0
____________________________________________________________________            
        if fingers1[3]==0:
            kit.servo[8].angle = 180
        elif fingers1[3]==1:
            kit.servo[8].angle = 0
_____________________________________________________________________            
        if fingers1[4]==0:
            kit.servo[11].angle = 180
        elif fingers1[4]==1:
            kit.servo[11].angle = 0        
                        
                    
                
            
    cv2.imshow("img",img)
    if cv2.waitKey(1)&0xFF==27:
        break
cv2.cap.release()
cv2.destroyAllWindows()