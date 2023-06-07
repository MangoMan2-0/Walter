from adafruit_servokit import ServoKit
from time import sleep
kit = ServoKit(channels=16)
def move(channel, inc, speed, angle):
    angle = angle+1
    i = 0
    i = int(kit.servo[channel].angle) + 1
    while not i == angle:
        kit.servo[channel].angle=i
        sleep(speed)
        i = i+inc
        print(i)
def stand():
    kit.servo[0].angle=90
    kit.servo[1].angle=90
    kit.servo[2].angle=90
    kit.servo[3].angle=130
    kit.servo[4].angle=90
    kit.servo[5].angle=130
    kit.servo[10].angle=70
    kit.servo[11].angle=90
    kit.servo[12].angle=10
    kit.servo[13].angle=90
    kit.servo[14].angle=90
    kit.servo[15].angle=90
def wave():
    kit.servo[2].angle=180
    sleep(1)
    kit.servo[1].angle=135
    sleep(0.5)
    kit.servo[1].angle=45
    sleep(0.5)
    kit.servo[1].angle=135
    sleep(0.5)
    kit.servo[1].angle=45
    sleep(0.5)
    kit.servo[1].angle=135
    sleep(0.5)
    kit.servo[1].angle=45
    sleep(0.5)
    kit.servo[1].angle=135
    sleep(0.5)
    kit.servo[1].angle=45
    sleep(0.5)
    kit.servo[1].angle=90
    sleep(0.5)
    kit.servo[2].angle=90
def step1():
    move(12, 1, 0.025, 30)
    move(5, 1, 0.005, 145)
    move(4, 1, 0.005, 135)
    move(12, -0.5, 0.025, 10)
def step2():
    move(4, -1, 0.0001,90)
    move(5, -1, 0.0001, 130)
    move(3, 0.5, 0.01, 150)
    move(11, -1, 0, 55)
    move(10, -1, 0, 40)
    move(3, -0.5, 0.01, 130)

def step3():
    move(11, 1, 0.0001, 90)
    move(10, 1, 0.0001,70)
    move(12, 0.5, 0.01, 30)
    move(4, 1, 0, 130)
    move(5, 1, 0, 155)
    move(12, -1, 0.01, 10)
def ok():
    kit.servo[2].angle=180
    sleep(0.3)
    kit.servo[1].angle=45
    sleep(1)
    kit.servo[1].angle=90
    sleep(0.3)
    kit.servo[2].angle=90
    

stand()
sleep(3)
wave()
sleep(3)
ok()
sleep(5)
while True:
    step3()
    step2()
        
        
    