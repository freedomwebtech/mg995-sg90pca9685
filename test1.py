from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
while True:
    a=input('enter:-')
    kit.servo[0].angle = int(a)   
